#!/usr/bin/env python3
"""
Leitura do cartão de submissão da galeria.

O cartão é markdown livre: o aluno escreve, organiza e ilustra como quiser.
Se ele tiver um bloco de metadados no topo (delimitado por `---`), o gerador
do mural usa esses dados para montar a linha do projeto. Nada aqui é
validado: o que faltar é preenchido com um valor padrão.
"""

import os
import sys
import unicodedata


def utf8_no_console():
    """O relatório usa emoji e acento; sem isto quebra em console Windows."""
    for fluxo in (sys.stdout, sys.stderr):
        if hasattr(fluxo, "reconfigure"):
            fluxo.reconfigure(encoding="utf-8", errors="replace")


def sem_acento(texto):
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower()


def le_metadados(caminho):
    """Lê o bloco de metadados do topo de um cartão, se houver.

    Aceita o subconjunto plano de YAML: uma `chave: valor` por linha. Cartão
    sem bloco, ou com bloco malformado, devolve um dicionário vazio — o mural
    se vira com o nome da pasta.
    """
    try:
        linhas = open(caminho, encoding="utf-8").read().splitlines()
    except OSError:
        return {}

    if not linhas or linhas[0].strip() != "---":
        return {}

    dados = {}
    for linha in linhas[1:]:
        if linha.strip() == "---":
            return dados
        if not linha.strip() or linha.lstrip().startswith("#") or ":" not in linha:
            continue
        chave, valor = linha.split(":", 1)
        valor = valor.strip()
        # Valor com dois-pontos precisa vir entre aspas para o GitHub renderizar
        # o bloco; aqui as aspas são só embalagem e saem antes de usar.
        if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in "\"'":
            valor = valor[1:-1]
        dados[sem_acento(chave.strip())] = valor.strip()

    # O bloco abriu e nunca fechou: não dá para saber onde termina.
    return {}


def procura_cartoes(raiz="."):
    """Encontra todos os cartões do repositório: <desafio>/projetos/<usuario>/README.md."""
    achados = []
    for desafio in sorted(os.listdir(raiz)):
        pasta_projetos = os.path.join(raiz, desafio, "projetos")
        if not os.path.isdir(pasta_projetos):
            continue
        for usuario in sorted(os.listdir(pasta_projetos)):
            pasta = os.path.join(pasta_projetos, usuario)
            cartao = os.path.join(pasta, "README.md")
            if os.path.isdir(pasta) and os.path.isfile(cartao):
                achados.append((desafio, usuario, cartao.replace(os.sep, "/")))
    return achados
