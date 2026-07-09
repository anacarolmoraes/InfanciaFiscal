# Relatorio Do Lote 002

## Escopo

Lote executado sobre as linhas Excel 22 a 41 da aba `classificacao_automatizada` da copia de trabalho `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

Municipio do lote:

* Alvorada.

Arquivos usados e gerados:

* entrada do lote: `parte2/resultados/lote_002.csv`;
* resultado classificado: `parte2/resultados/lote_002_classificado.csv`;
* copia de trabalho preenchida: `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

## Regras Aplicadas

Foram preenchidas apenas:

* `Area Tematica`;
* `Gasto E ou NE`.

A coluna `Indicador` nao foi preenchida nem alterada.

As classificacoes mantiveram o padrao aprovado no lote piloto, com base em:

* `parte2/knowledge_bundle/`;
* exemplos humanos da aba `municipios_classificados`;
* hierarquia `nomePrograma` + `nomeFuncao` + `nomeSubFuncao` + `nomeAcaoOrcamentaria`.

## Resultado Quantitativo

Total de linhas classificadas:

```text
20
```

Distribuicao por `Area Tematica`:

```text
nao se aplica: 13
Saude Materno-infantil: 6
Assistencia Social: 1
```

Distribuicao por `Gasto E ou NE`:

```text
-: 13
Nao Especifico: 7
```

Distribuicao por confianca:

```text
Alta: 19
Media: 1
Baixa: 0
```

Linhas marcadas para revisao humana:

```text
1
```

## Linha Revisada

* Linha Excel 36: `CONSTRUCAO DO TERMINAL DE ENERGIA FOTOVOLTAICA EM PREDIOS PUBLICOS - FMS`.
  * Classificacao aplicada: `Saude Materno-infantil` / `Nao Especifico`.
  * Motivo: despesa-meio vinculada ao FMS pode sustentar infraestrutura de saude, mas o objeto de energia fotovoltaica e indireto e nao explicita unidade de atendimento.

## Revisao Humana

O usuario revisou o lote 002 e registrou a decisao:

```text
Classificacao perfeita.
```

Assim, a classificacao da linha Excel 36 foi considerada conforme, e o lote 002 fica aprovado integralmente.

## Observacao Metodologica

O lote 002 manteve o padrao aprovado no piloto. A maior parte das linhas foi classificada por repeticao de padroes ja observados: vigilancia sanitaria, CRAS, ACS, legislativo, administracao geral e ensino fundamental.

A revisao humana confirmou conformidade integral do lote 002.
