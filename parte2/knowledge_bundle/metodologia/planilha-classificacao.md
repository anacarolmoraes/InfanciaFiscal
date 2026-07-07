---
type: Reference
title: Planilha de classificacao
description: Campos relevantes para estruturar e classificar acoes orcamentarias no GSPI-M.
tags: [metodologia, planilha, campos]
source: parte2/guia_unicef.md
---

# Unidade Da Planilha

A planilha deve ter uma linha por acao orcamentaria do Executivo municipal.

# Campos Necessarios Para Classificacao

Campos essenciais para o classificador:

* ano de exercicio;
* unidade orcamentaria;
* codigo e nome da funcao;
* codigo e nome da subfuncao;
* nome ou codigo do programa;
* objetivo do programa, quando disponivel;
* nome ou codigo da acao;
* finalidade ou descricao da acao, quando disponivel;
* area tematica;
* classificacao do GSPI como gasto especifico ou ampliado;

No arquivo operacional da Parte 2, esses campos correspondem principalmente a:

* `nomePrograma`;
* `nomeFuncao`;
* `nomeSubFuncao`;
* `nomeAcaoOrcamentaria`;
* `Area Tematica`;
* `Gasto E ou NE`.

Nesta etapa, a LLM deve preencher apenas `Area Tematica` e `Gasto E ou NE`.

A coluna `Indicador`, subarea tematica, ponderadores e valores ponderados ficam fora do escopo desta etapa.

# Campos Financeiros

Campos financeiros recomendados:

* valor previsto na LOA;
* valor previsto ponderado;
* valor empenhado;
* valor empenhado ponderado;
* valor liquidado;
* valor liquidado ponderado;
* valor pago;
* valor pago ponderado.

# Uso Pelo Classificador

Na ausencia de campos de finalidade ou objetivo, a decisao deve explicitar menor confianca e usar a combinacao de programa, funcao, subfuncao e acao para inferencia.

O arquivo operacional definitivo e `fonte_parte_2.xlsx`.

A aba `municipios_classificados` contem exemplos humanos.

A aba `classificacao_automatizada` contem as linhas a classificar pela IA.

Os exemplos humanos ajudam a calibrar a aplicacao pratica da regra, mas nao prevalecem sobre o Knowledge Bundle.

Confianca, justificativa e divergencias devem ser registradas em log ou arquivo derivado, sem alterar desnecessariamente a planilha original.
