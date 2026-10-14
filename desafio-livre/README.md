# Desafio Jornada de Dados — Desafio Livre: Você Escolhe o Problema

## O que é este desafio

No desafio anterior, você recebeu o pedido de um cliente. Neste, **o pedido é seu.**

Não existe enunciado de produto, lista de funcionalidades nem domínio obrigatório. Você escolhe o problema, o negócio e o recorte. O que este desafio cobra é outra coisa: **como você constrói.** Discovery bem feito, decisões registradas, repositório configurado como o de um time de verdade e um agente de código trabalhando dentro de limites que você definiu.

É isso que o mercado está usando hoje. Times que entregam bem com IA não são os que geram mais código: são os que sabem dirigir o agente, decidir o que fica de fora e explicar por que cada escolha foi feita.

> **Regra nº 1 do desafio: o problema é seu, e é real o suficiente para exigir decisões.**
> Não vale um "app de tarefas" genérico. Escolha um problema em que exista pelo menos uma etapa em que errar custa caro, e sustente esse problema com nome próprio: negócio, cliente, usuário e produto.

---

# Parte 1 — O problema, à sua escolha

## De onde tirar a ideia

A enquete da comunidade trouxe quatro áreas, e qualquer uma delas é um ótimo ponto de partida:

| Área | Exemplos de dor que rendem um bom projeto |
|---|---|
| **Jurídico** | Triagem de documentos, prazos que não podem ser perdidos, pesquisa em contratos e jurisprudência |
| **Marketing** | Geração e revisão de campanhas, análise de desempenho, conteúdo que precisa respeitar a marca |
| **Gestão de projetos** | Status que ninguém atualiza, riscos que aparecem tarde demais, relatórios que consomem horas |
| **Contabilidade** | Conciliação, classificação de lançamentos, conferência de obrigações e documentos |

Essas áreas são **sugestão, não regra.** Se outro problema te move mais, vá nele. O que importa é que você consiga defender por que escolheu esse problema e por que ele precisa de engenharia de verdade.

## Invente o case, com nome e sobrenome

Seja qual for a área, dê nome a tudo:

- **O negócio** em que o problema acontece
- **O cliente** que te contratou: quem é, o que faz, do que tem medo
- **Quem usa** o produto no dia a dia
- **O produto** que você está construindo

Case genérico gera documento genérico e código genérico. Case com nome próprio força decisão concreta.

> Sem cliente para te entrevistar, você faz os dois papéis. Escreva a conversa com o cliente que você imaginou, com os desejos **e os medos** dele. Isso vira a base do seu discovery.

**Duas restrições valem para todo mundo:** nada de dado real ou sensível (use dados sintéticos) e nada que tenha efeito real fora do projeto, como dinheiro, documento com validade ou envio para terceiros. Uma simulação fiel resolve.

---

# Parte 2 — O projeto de engenharia

Aqui está o coração do desafio. Formato, ferramenta e nível de detalhe são seus: o que segue é o que cada peça precisa responder, não um modelo para preencher.

## 1. Discovery e tomada de decisão

Antes de qualquer linha de código, queremos ver o seu pensamento registrado:

| Documento | O que ele responde |
|---|---|
| **Discovery** | Qual é o problema, para quem, como ele é resolvido hoje e onde dói |
| **PRD** — documento de produto | O que entra na primeira versão, **o que fica de fora** e como o sucesso será medido |
| **SPECs** — especificações | O comportamento esperado, escrito sem ambiguidade, para que outra pessoa (ou um agente de código) implemente sem adivinhar |
| **ADRs** — registro de decisões | Cada decisão importante, com as alternativas consideradas e as consequências que você aceitou |

O ADR é o documento que mais vale no seu portfólio. Decisão sem alternativa descartada não é decisão, é acaso.

## 2. Configuração do repositório

O seu repositório deve parecer o de um time profissional, não uma pasta pessoal:

- Branch principal protegida, com mudanças entrando por pull request
- Commits que se entendem e PRs que contam o que mudou e por quê
- Validações automáticas que rodam em todo PR e **bloqueiam** o que não deveria passar. Quais rodar (testes, lint, tipos, segurança, docs) é escolha sua; que elas existam, não
- Um README que permite a outra pessoa rodar o projeto sem te perguntar nada
- Segredos fora do repositório, sempre

## 3. O seu Agent Harness

Você vai construir este projeto com agentes de código, e queremos ver isso explícito. Escolha o seu harness — **Claude Code, Codex, Cursor, Kimi, Gemini CLI, Aider, o que for** — e deixe o repositório preparado para ele:

- Qual harness você escolheu e por quê
- O arquivo de contexto do projeto (`CLAUDE.md`, `AGENTS.md` ou o equivalente): o que um agente precisa saber para não quebrar o seu projeto
- O que você automatizou para o agente (comandos, skills, hooks, regras) e o que você deliberadamente **não** deixou na mão dele
- Como você revisa o que o agente escreve antes de entrar na `main`

Saber dirigir um agente de código, com contexto e limites bem definidos, é a habilidade que este desafio existe para treinar.

## 4. Arquitetura explicada

Um desenho e um texto curto explicando como o sistema se sustenta: os componentes, onde ficam os dados, onde entra IA (se entrar), onde entra o humano e o que acontece quando algo falha no meio do caminho.

Não existe arquitetura certa. Existe arquitetura **explicada**.

---

## Antes de codar: as perguntas que valem mais que o código

- [ ] Que problema eu escolhi, e por que ele vale a pena ser resolvido?
- [ ] Quem sofre com esse problema hoje, e como ele é resolvido sem o meu produto?
- [ ] Onde, no fluxo, errar é inaceitável? O que é **irreversível**, e quem deveria aprovar antes?
- [ ] Onde IA gera **valor** e onde gera **risco**?
- [ ] Como vou saber, **com números**, que o produto funciona?
- [ ] O que fica de fora da primeira versão? (Escopo é decisão de risco, não preguiça)
- [ ] O que o meu agente de código pode fazer sozinho, e o que precisa passar por mim?

---

## Aulas de apoio na plataforma

O [**módulo de desafios na plataforma da Jornada**](https://suajornadadedados.curseduca.pro/m/lessons/desafios?moduleId=818&classId=2742) reúne, na mesma página, as aulas que ajudam a estruturar cada etapa. Escolha a aula na lista do módulo:

- **Estruturação do projeto**
- **Discovery e tomada de decisões**
- **Agent Harness**
- **Projeto completo do desafio Agosto–Setembro:** um projeto inteiro, do discovery à entrega

Os projetos do desafio anterior também são uma boa referência: veja o [mural de projetos](../PROJETOS.md).

## Como participar

1. **Escolha o seu problema** e invente o case: negócio, cliente, usuário e produto, com nome próprio
2. **Crie o seu repositório público.** Este repositório aqui é o enunciado; o trabalho acontece no seu
3. **Faça o discovery e registre as decisões** antes de codar
4. **Configure o repositório e o harness**, e construa
5. **Submeta o cartão do seu projeto à galeria** deste repositório, seguindo o [COMO-SUBMETER.md](../COMO-SUBMETER.md)
6. **Dúvidas?** Pergunte na categoria [**Como construir**](https://github.com/suajornadadedados/desafio-jornada/discussions/new?category=como-construir) das Discussions

## Datas e o que acontece com os projetos

| Período | O que acontece |
|---|---|
| Outubro/2026 | Desafio aberto |
| Ao longo do desafio | Perguntas respondidas nas Discussions; projetos na galeria podem ser comentados na live exclusiva para alunos |
| Fim de novembro/2026 | Data de referência: submeta o seu cartão à galeria e avance o quanto conseguir |
| Depois | O desafio continua aberto, com a galeria recebendo cartões. A data existe para dar ritmo; o método fica |

Projetos em diferentes estágios são bem-vindos. Um discovery bem feito, com PRD e ADRs sólidos, já é uma entrega valiosa mesmo com a implementação no começo.

---

Boa construção. E lembre da regra que costura tudo:

> **O agente escreve o código. As decisões são suas.**
