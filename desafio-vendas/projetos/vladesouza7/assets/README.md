# Imagens do README

Capturas das telas, exibidas na galeria do [README](../../README.md#as-telas).

## Convenção de nome

`tela-NN-nome.png` — `NN` é a ordem da **jornada**, não a do menu: quem abre o README lê de cima
para baixo, e a sequência conta a história do lead até o desfecho.

| Arquivo | Rota | Perfil |
|---|---|---|
| `tela-01-landing.png` | `/` | pública |
| `tela-02-catalogo.png` | `/catalogo` | pública |
| `tela-03-entrar.png` | `/entrar` | pública |
| `tela-04-aprovacoes.png` *(falta — fila vazia)* | `/aprovacoes` | `dono`, `gerente` |
| `tela-05-atendimentos.png` *(falta — nome real na lista)* | `/atendimentos` | `dono`, `gerente` |
| `tela-06-test-drive.png` | `/test-drive` | `dono`, `gerente`, `vendedor` |
| `tela-07-desfecho.png` *(falta — sem test drive)* | `/desfecho` | `dono`, `gerente`, `vendedor` |
| `tela-08-custo.png` | `/custo` | `dono`, `gerente` |
| `tela-09-configuracoes.png` | `/configuracoes` | só `dono` |

Viewport **1440x900**, página inteira, `deviceScaleFactor` 2 — o GitHub reduz a imagem na
galeria, e captura 1x fica borrada.

## Antes de recapturar

**Nenhum nome ou telefone real pode entrar aqui.** Estas imagens vão para um repositório público, e
o `/atendimentos` lista lead por nome. Semeie dados de demonstração antes
(`uv --project backend run python scripts/seed.py`) e confira cada captura antes de commitar —
é a [invariante 5](../../CLAUDE.md) valendo também fora do código.

Tela com estado vazio — fila sem pedido, agenda sem test drive — não entra na galeria: ela mostra
o contorno da aplicação e nada do que ela faz.

**Três ainda não existem**, e a tabela acima diz qual e por quê: a fila e o desfecho estavam
vazios, e o `/atendimentos` listava um lead com nome de pessoa real. As três entram quando o
banco tiver um pedido de aprovação, um test drive marcado e leads de demonstração.
