---
projeto: Vendinha — Agente de Vendas de Ponta a Ponta
autor: Caio Machado
usuario: caiomoliveira
dominio: Loja de conveniência de bairro
repositorio: https://github.com/caiomoliveira/vendinha
linkedin: https://www.linkedin.com/posts/caio-moliveira_vendinha-desafio-jornada-activity-7490415422425698304-LuUl
plataforma: https://suajornadadedados.curseduca.pro/m/community/posts/a773a771-9319-4f51-8340-2358d8d9832d
video: https://youtu.be/dQw4w9WgXcQ
---

# Vendinha — Agente de Vendas de Ponta a Ponta

A Vendinha é uma loja de conveniência de bairro que vende pelo WhatsApp e perde venda porque
uma pessoa só responde a todo mundo. O agente atende o cliente do "o que você tem de bebida
gelada?" até o pedido pago, sem nunca afirmar preço ou estoque de memória.

## Arquitetura

Um supervisor e dois subagents, separados por permissão e não por prompt:

```
                        ┌── RECOMENDAÇÃO ──── tools read-only ──── Qdrant · Postgres
 cliente ──chat(SSE)──▶ supervisor ──┤
                        └── CHECKOUT ──────── tools de escrita ─── Postgres · gateway (sandbox)
                                     │
                        ⏸ interrupt ──▶ fila do operador ──▶ aprova / rejeita
```

O subagent de recomendação não tem tool de escrita registrada — não é proibido de usar, ele
não tem. E o grafo pausa antes de qualquer ação irreversível, com estado persistido no
Postgres: sem registro de aprovação, não existe caminho de volta.

## Stack

| Camada | Escolha | Por quê |
|---|---|---|
| Orquestração | LangGraph | `interrupt` com estado persistido em checkpointer — a pausa é primitivo, não UX |
| Observabilidade | Langfuse (self-hosted) | trace por sessão desde o commit 1, PII mascarada na origem |
| API | FastAPI | Pydantic → OpenAPI → cliente TypeScript gerado |
| Dados | Postgres + Qdrant | Postgres é fonte da verdade de preço *e* checkpointer; Qdrant carrega o catálogo semântico |
| Frontend | React + Vite | dois consumidores da mesma API: chat do cliente e fila do operador |

## Harness

Claude Code, com o harness versionado junto do código: `CLAUDE.md` enxuto (só o que é verdade
em toda sessão), quatro rituais como slash commands e skills vendorizadas com SHA fixado. O
comando que mais mudou o resultado foi o `/verificar-spec`: uma sessão nova, que nunca viu a
implementação, lê a spec e emite veredito — e não tem permissão de corrigir o código, porque
revisor que conserta virou autor.

## As três decisões mais difíceis

1. **Preço nunca sai do modelo.** Recusei colocar o catálogo no prompt: o agente chama uma tool
   que lê o Postgres no momento da criação do pedido.
2. **Desconto não existe como ação disponível.** A solução óbvia era escrever "nunca dê
   desconto" no prompt — isso some no diff e não garante nada. Segurança por arquitetura.
3. **Observabilidade na S-02, não na S-08.** Inversão deliberada da ordem das specs: depurar
   agente sem trace é adivinhação.

## O que eu aprendi

Que a arquitetura é a parte fácil. Ela cai por gravidade depois que você decide o que o modelo
**não** tem permissão de fazer — e essa decisão vem da matriz de riscos, não do framework da
moda. O que mais me custou foi aceitar que risco sem verificação automatizada é desejo, não
requisito: enquanto o eval não estava no CI bloqueando merge, o documento envelhecia em
silêncio dizendo que estava tudo mitigado.