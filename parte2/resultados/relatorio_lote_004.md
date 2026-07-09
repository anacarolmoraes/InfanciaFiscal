# Relatorio Do Lote 004

## Escopo

Lote executado sobre as linhas Excel 62 a 81 da aba `classificacao_automatizada` da copia de trabalho `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

Municipio do lote:

* Alvorada.

Arquivos usados e gerados:

* entrada do lote: `parte2/resultados/lote_004.csv`;
* resultado classificado: `parte2/resultados/lote_004_classificado.csv`;
* copia de trabalho preenchida: `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

## Regras Aplicadas

Foram preenchidas apenas:

* `Area Tematica`;
* `Gasto E ou NE`.

A coluna `Indicador` nao foi preenchida nem alterada.

As classificacoes mantiveram o padrao aprovado no lote piloto, no lote 002 e no lote 003.

## Resultado Quantitativo

Total de linhas classificadas:

```text
20
```

Distribuicao por `Area Tematica`:

```text
nao se aplica: 8
Assistencia Social: 5
Educacao Infantil: 3
Saude Materno-infantil: 2
Saneamento e Agua: 1
```

Distribuicao por `Gasto E ou NE`:

```text
Nao Especifico: 11
-: 8
Especifico: 1
```

Distribuicao por confianca:

```text
Alta: 17
Media: 3
Baixa: 0
```

Linhas marcadas para revisao humana:

```text
3
```

## Linhas Revisadas

* Linha Excel 69: `MANUTENCAO DO TRANSPORTE ESCOLAR - FUNDEB 30%`.
  * Classificacao aplicada: `Educacao Infantil` / `Nao Especifico`.
  * Motivo: transporte escolar em programa de educacao pode abranger educacao infantil, mas a linha nao explicita etapa infantil.
* Linha Excel 72: `MANUTENCAO DO TRANSPORTE ESCOLAR`.
  * Classificacao aplicada: `Educacao Infantil` / `Nao Especifico`.
  * Motivo: transporte escolar generico pode abranger educacao infantil, mas a etapa nao esta explicita.
* Linha Excel 77: `MANUTENCAO DO ATERRO SANITARIO`.
  * Classificacao aplicada: `Saneamento e Agua` / `Nao Especifico`.
  * Motivo: aterro sanitario se relaciona a manejo de residuos solidos, mas aparece sob funcao de gestao ambiental, tornando o enquadramento menos direto.

## Revisao Humana

O usuario revisou o lote 004 e registrou a decisao:

```text
Perfeito, pode continuar.
```

Assim, as 3 linhas inicialmente marcadas para revisao foram consideradas conformes, e o lote 004 fica aprovado integralmente.

## Observacao Metodologica

O lote 004 manteve o padrao aprovado nos lotes anteriores. As linhas de CRAS, CREAS, FMAS, FMS, ACS, ensino infantil explicito, ensino fundamental, administracao geral, meio ambiente generico e estradas vicinais seguiram padroes ja estabilizados.

A revisao humana confirmou conformidade integral do lote 004, inclusive nos casos de beneficio indireto ou enquadramento por objeto da acao.
