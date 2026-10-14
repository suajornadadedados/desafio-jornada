---
projeto: Lakehouse Mecamecanica
autor: Diego Souza de Medeiros
usuario: dimedeiros
dominio: Rede de autopeças
repositorio: https://github.com/DiMedeiros/lakehouse_mecamecanica
linkedin: https://lnkd.in/p/dnwbsyTR
---

# Lakehouse Mecamecanica

Lakehouse de ponta a ponta sobre **Databricks** (Unity Catalog + Declarative Automation Bundles) simulando a operação comercial de uma rede de autopeças. Os dados saem do ERP e do CRM, passam pelas camadas do medalhão e viram um dashboard de BI, espaços Genie para perguntas em linguagem natural e um modelo de ML que **prioriza a fila semanal de ligações dos vendedores**.

## Arquitetura de dados

| Camada | Conteúdo |
|---|---|
| **raw** | CSVs do ERP e do CRM, exatamente como chegaram, num Volume do Unity Catalog |
| **bronze** | Tabelas cruas + controle que confere se os 10 arquivos esperados chegaram |
| **silver** | Dados limpos, tipados e com contrato |
| **gold** | Dimensões, `fato_vendas`, marts e métricas de negócio (clientes em risco, ranking de marcas, margem por categoria, ruptura por marca...) |

Schemas, volumes, jobs e dashboard são definidos como código e sobem com `databricks bundle deploy`, nada criado à mão na interface.

## Pipeline

Um job orquestrado roda da conferência dos arquivos até a camada de ML, agendado todo dia às 06:00. Dois portões quebram o job se algo estiver errado: **9 testes de qualidade** na gold e uma **auditoria de metadado** que exige `COMMENT` em toda tabela, view e coluna. É isso que sustenta a confiabilidade do Genie.

## Para quem é

- **Dashboard comercial (Lakeview):** receita, margem, pedidos, ticket médio, tendências e top 20 clientes
- **Três espaços Genie**, um por público: perguntas gerais de negócio, a visão da direção comercial (valor da fila, saúde do modelo, conversão) e a do vendedor (quem ligar essa semana, por quê e o que oferecer)

## A fila de ligações

- **Modelo:** gradient boosting (scikit-learn) que prevê se o cliente compra em 7 dias, registrado no MLflow/Unity Catalog. Só é aceito se superar os baselines e atingir `lift_top200 >= 2.5x`
- **Fila final:** ordenada por valor esperado (`score × ticket médio × margem`), não só pelo score
- **Sugestão de produto:** 100% regra em SQL (histórico, estoque e categoria), sem ML

---

Código e detalhes de como rodar no [repositório do projeto](https://github.com/DiMedeiros/lakehouse_mecamecanica).
