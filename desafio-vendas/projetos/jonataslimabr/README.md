---
projeto: RevenueFlow AI
autor: Jonatas Lima da Costa
usuario: jonataslimabr
dominio: Vendas B2B via WhatsApp
repositorio: https://github.com/JonatasLimaBR/revenueflow-ai
linkedin: https://lnkd.in/p/dQvFxpf6
---

# RevenueFlow AI

**Um agente comercial B2B via WhatsApp que nunca decide preço, estoque ou pagamento sozinho.**

O RevenueFlow AI atende, negocia, fecha pedido e reabre conversas por iniciativa própria. O LLM interpreta a mensagem; um **Policy Engine determinístico** decide o que é permitido; a API executa. Toda decisão que mexe com dinheiro passa por uma policy em Python puro, testável sem nenhuma chamada de modelo. O que sai da alçada da policy pausa o fluxo e espera um humano.

## O que foi entregue

17 fatias em produção no GCP, cada uma com ADR próprio:

- **Atendimento:** webhook do WhatsApp autenticado por HMAC → Pub/Sub → grafo LangGraph que classifica a intenção e responde ancorado em catálogo, preço e estoque reais, usando Vertex AI / Gemini
- **Negociação:** desconto fora da política pausa o grafo (`interrupt()`) e cria uma aprovação pendente; a decisão humana retoma o grafo exatamente de onde parou
- **Pedido e pagamento:** pedido idempotente, estoque revalidado na hora e pagamento só em sandbox
- **Inteligência de cliente:** Customer 360, ciclo de vida do lead e um Opportunity Engine que detecta recompra atrasada e proposta parada
- **Governança:** handoff humano com 3 gatilhos determinísticos, auditoria por turno (tokens, custo, latência), CPF mascarado em log e uma suíte que prova que mensagem adversária não muda preço nem pula aprovação
- **Venda ativa e analytics:** campanhas com Policy Gate (opt-out sempre vence), sync para BigQuery e um servidor MCP para consultar o sistema pelo Claude

## Stack

Python 3.12 · FastAPI · LangGraph (checkpoint em PostgreSQL) · Vertex AI / Gemini · Cloud Run · Cloud SQL · Pub/Sub · BigQuery · Terraform · GitHub Actions com Workload Identity Federation · OpenTelemetry + Cloud Monitoring

## Processo

A `main` é protegida: tudo entra por pull request, com 7 checks obrigatórios e merge squash-only. O projeto tem 16 PRDs, 37 specs e 63 ADRs. Usa Codex como harness oficial, com um kit completo também para Claude Code (hooks que bloqueiam ações destrutivas no GCP).

---

Código, diagramas e toda a documentação no [repositório do projeto](https://github.com/JonatasLimaBR/revenueflow-ai).
