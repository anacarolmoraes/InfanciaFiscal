---
okf_version: "0.1"
title: Knowledge Bundle GSPI-M
description: Conhecimento operacional para classificar acoes orcamentarias segundo a metodologia GSPI-M.
---

# Knowledge Bundle GSPI-M

Este bundle organiza conhecimento normativo e operacional extraido do Guia de Apuracao do Gasto Social com a Primeira Infancia para Municipios (GSPI-M), com o objetivo de apoiar um classificador baseado em LLM.

O bundle foi produzido a partir de metodologia proprietaria de engenharia de conhecimento, voltada a transformar documentos normativos em conhecimento operacional consumivel por modelos de linguagem. Este entregavel contem o conhecimento necessario ao uso do classificador, sem expor prompts internos, heuristicas proprietarias, scripts de compilacao ou o pipeline operacional de construcao.

# Metodologia

* [Unidade de inferencia](metodologia/unidade-de-inferencia.md) - Define os campos que devem ser interpretados conjuntamente.
* [Criterios de inclusao](metodologia/criterios-inclusao.md) - Define quando uma acao entra no GSPI-M.
* [Criterios de exclusao](metodologia/criterios-exclusao.md) - Define despesas e politicas que nao entram no GSPI-M.
* [Despesas-meio e despesas finalisticas](metodologia/despesas-meio.md) - Define quando despesas administrativas podem ser consideradas.
* [Gasto especifico ou ampliado](metodologia/gasto-especifico-ampliado.md) - Define a classificacao E/NE.
* [Ponderadores](metodologia/ponderadores.md) - Define como tratar gasto ampliado.
* [Planilha de classificacao](metodologia/planilha-classificacao.md) - Define campos relevantes para classificar linhas orcamentarias.

# Areas Tematicas

* [Educacao Infantil](areas/educacao-infantil.md)
* [Saude Materno-infantil](areas/saude-materno-infantil.md)
* [Assistencia Social](areas/assistencia-social.md)
* [Protecao dos Direitos da Crianca e da Familia](areas/protecao-direitos-crianca-familia.md)
* [Direito a Cidade e Habitacao](areas/direito-cidade-habitacao.md)
* [Saneamento e Agua](areas/saneamento-agua.md)
* [Cultura e Direito de Brincar](areas/cultura-direito-brincar.md)
* [Seguranca Alimentar](areas/seguranca-alimentar.md)
* [Enfrentamento da Pobreza](areas/enfrentamento-pobreza.md)

# Fonte Normativa

Guia de Apuracao do Gasto Social com a Primeira Infancia para Municipios (GSPI-M), convertido localmente para Markdown em `parte2/guia_unicef.md`.
