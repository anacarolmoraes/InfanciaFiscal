# Relatorio Do Lote 005

## Escopo

Lote executado sobre as linhas Excel 82 a 101 da aba `classificacao_automatizada` da copia de trabalho `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

Municipio do lote:

* Alvorada.

Arquivos usados e gerados:

* entrada do lote: `parte2/resultados/lote_005.csv`;
* resultado classificado: `parte2/resultados/lote_005_classificado.csv`;
* copia de trabalho preenchida: `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

## Regras Aplicadas

Foram preenchidas apenas:

* `Area Tematica`;
* `Gasto E ou NE`.

A coluna `Indicador` nao foi preenchida nem alterada.

As classificacoes mantiveram o padrao aprovado nos lotes anteriores.

## Resultado Quantitativo

Total de linhas classificadas:

```text
20
```

Distribuicao por `Area Tematica`:

```text
Saude Materno-infantil: 5
Educacao Infantil: 5
nao se aplica: 6
Assistencia Social: 2
Saneamento e Agua: 1
Protecao dos Direitos da Crianca e da Familia: 1
```

Distribuicao por `Gasto E ou NE`:

```text
Nao Especifico: 12
-: 6
Especifico: 2
```

Distribuicao por confianca:

```text
Alta: 15
Media: 5
Baixa: 0
```

Linhas marcadas para revisao humana:

```text
5
```

## Linhas Revisadas

* Linha Excel 84: `GESTAO DA SECRETARIA MUNICIPAL DE POLITICAS PARA MULHERES`.
  * Classificacao aplicada: `Protecao dos Direitos da Crianca e da Familia` / `Nao Especifico`.
  * Motivo: padrao aprovado no piloto, mas a linha nao explicita primeira infancia, gestantes ou lactantes.
* Linha Excel 86: `MANUTENCAO DA ALIMENTACAO ESCOLAR`.
  * Classificacao aplicada: `Educacao Infantil` / `Nao Especifico`.
  * Motivo: alimentacao escolar pode abranger educacao infantil, mas a etapa nao esta explicita.
* Linha Excel 89: `MANUTENCAO DO FUNDO MUNICIPAL DE EDUCACAO - FME`.
  * Classificacao aplicada: `Educacao Infantil` / `Nao Especifico`.
  * Motivo: padrao aprovado no piloto para FME em administracao geral, mas a linha nao explicita etapa infantil.
* Linha Excel 90: `MANUTENCAO DOS SERVICOS DE LIMPEZA PUBLICA`.
  * Classificacao aplicada: `Saneamento e Agua` / `Nao Especifico`.
  * Motivo: limpeza publica se relaciona a saneamento/residuos, mas aparece em gestao ambiental.
* Linha Excel 91: `MANUTENCAO DO TRANSPORTE ESCOLAR`.
  * Classificacao aplicada: `Educacao Infantil` / `Nao Especifico`.
  * Motivo: transporte escolar generico pode abranger educacao infantil, mas a etapa nao esta explicita.

## Revisao Humana

O usuario revisou o lote 005 e registrou a decisao:

```text
Perfeito, pode continuar.
```

Assim, as 5 linhas inicialmente marcadas para revisao foram consideradas conformes, e o lote 005 fica aprovado integralmente.

## Observacao Metodologica

O lote 005 manteve o padrao aprovado nos lotes anteriores. As linhas de saude, CRAS, educacao infantil explicita, ensino fundamental, cultura geral, financas, planejamento e iluminacao publica seguiram padroes ja estabilizados.

A revisao humana confirmou conformidade integral do lote 005, inclusive nos casos de beneficio indireto ou area ampla sem publico-alvo explicitado.
