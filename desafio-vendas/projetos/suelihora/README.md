---
projeto: "Rash Rolamentos: Agente de Vendas Técnicas com LangGraph & HITL"
autor: Sueli Hora
usuario: suelihora
dominio: Distribuidora de rolamentos industriais B2B
repositorio: https://github.com/SueliHora/rash-rolamentos
linkedin: https://www.linkedin.com/posts/sueli-da-hora_jornadadedados-inteligenciaartificial-engenhariadedados-ugcPost-7496332845825548288-Thb_
plataforma: https://suajornadadedados.curseduca.pro/m/community/posts/suelihora-rash-rolamentos
---

# Rash Rolamentos Industriais — Agente Autônomo de Vendas Técnicas B2B

Sabe quando você precisa comprar uma peça industrial, mas não faz ideia do código do modelo e chega só com umas medidas na cabeça ou dizendo algo como *"preciso de uma peça para um motor de 15 CV"*? Filtros tradicionais de sites não ajudam nessas horas. Foi para resolver essa dor real que nasceu o projeto da **Rash Rolamentos Industriais**.

Desenvolvi um assistente com Inteligência Artificial que conversa de verdade com o cliente, compreende a necessidade técnica (mesmo sem jargões exatos) e conduz o atendimento até a cotação estruturada.

## 🛡️ Pilares de Segurança & Engenharia

Como no setor industrial um erro de milímetro pode parar uma fábrica inteira, o projeto foi construído com rigor arquitetural estrito:

1. **Fim das Alucinações (Catálogo Determinístico):** A IA não tem permissão para inventar preços ou tamanhos. Ela é estritamente obrigada a consultar um banco de dados relacional real (SQLite) via ferramentas parametrizadas.
2. **Aprovação Humana (Human-in-the-Loop - HITL):** Se o cliente fizer um pedido de alto volume (ex: $\ge 10$ unidades) ou solicitar desconto especial, a IA não toma a decisão sozinha: o pedido é retido para aprovação do Diretor Comercial em um painel gerencial dedicado.

## Stack Tecnológica & Harness

* **Orquestração de IA:** LangGraph / LangChain com modelo primário `Gemini 1.5 Flash` (`langchain-google-genai`).
* **Gerenciamento de Dependências:** `uv` e `pyproject.toml` para controle determinístico de pacotes Python.
* **Camada de Dados:** SQLite 3 (normalizado com seeds determinísticos e testes automatizados de consistência).
* **Interface do Usuário:** Aplicação web interativa em Streamlit (hospedada ao vivo).
* **Harness de Desenvolvimento:** Gemini / Antigravity para suporte na estruturação da engenharia de software e automação de commits.

## O que Aprendi & Decisões de Engenharia

O maior desafio foi garantir que o modelo de linguagem (LLM) nunca inventasse códigos dimensionais de peças mecânicas. A solução foi isolar completamente a tomada de decisão de medidas e estoque para dentro de funções Python determinísticas (`src/tools.py`), usando o LLM estritamente como um tradutor de linguagem natural para a intenção de busca. O fluxo HITL completou a barreira de governança que o Diretor Comercial exigia.

## Links Oficiais

* Aplicação ao Vivo: https://rash-rolamentos.streamlit.app/
* Repositório do Código Fonte: https://github.com/SueliHora/rash-rolamentos
