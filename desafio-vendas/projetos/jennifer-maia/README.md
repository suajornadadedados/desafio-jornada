---
projeto: Nexum Sales Assistant
autor: Jennifer Maia
usuario: jennifer-maia
dominio: Equipamentos industriais B2B (manutenção, operação e monitoramento)
repositorio: https://github.com/Jennifer-Maia/nexum-sales-assistant
linkedin: https://lnkd.in/p/dfRwkNyr
---

# Nexum Sales Assistant

Assistente de vendas B2B da **Nexum Industrial**, uma empresa fictícia de equipamentos para manutenção, operação e monitoramento industrial. O cliente descreve a necessidade em linguagem natural ("preciso monitorar 20 máquinas entre 0 °C e 150 °C") e o agente leva a conversa até a recomendação de produto, a cotação aprovada por um humano, o pagamento simulado e o documento simulado. Tudo roda sobre **Databricks**.

## A regra central

O LLM **interpreta** a conversa, e o código **valida, consulta, calcula e controla estados**. O modelo nunca inventa dado comercial: ele só pode pedir uma das **seis ferramentas aprovadas**. Qualquer outra chamada é bloqueada e registrada.

| Ferramenta | O que faz |
|---|---|
| `search_products` | Busca produtos ativos e compatíveis |
| `check_inventory` | Consulta disponibilidade sem alterar o estoque |
| `create_quote` | Cria a cotação em rascunho, com preços congelados |
| `request_human_approval` | Pede e registra a aprovação humana |
| `simulate_payment` | Pagamento exclusivamente simulado |
| `generate_document` | Documento simulado, sem validade fiscal |

## Arquitetura

- **Dados em medalhão (Bronze → Silver → Gold)** com Delta e Declarative Automation Bundles. Registro inválido é sinalizado em `_quality_status`, nunca corrigido em silêncio.
- **Agente** com Foundation Model API do Databricks e um loop de tool calling próprio e determinístico.
- **Aprovação humana obrigatória** antes do pagamento, garantida por uma máquina de estados: `draft → pending_approval → approved → paid → completed`. Transição inválida é barrada pelo código.
- **Ações sensíveis** (cotação, aprovação, pagamento, documento) exigem confirmação explícita do cliente.
- **Auditoria completa** de cada turno: latência, tokens, modelo, status e erro.
- **Chat local em Streamlit** via Databricks Connect (serverless) e **dashboard Lakeview** com funil, operação do agente, qualidade, custo e atualização dos dados, lendo só a camada Gold.

## Qualidade

Mais de 175 testes unitários em memória, com um LLM falso determinístico: rodam sem API externa, sem segredo e sem custo de modelo. Prompt injection e pedidos de segredo são recusados e registrados.

---

Código, PRD, specs e ADRs no [repositório do projeto](https://github.com/Jennifer-Maia/nexum-sales-assistant).
