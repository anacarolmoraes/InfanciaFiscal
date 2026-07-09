# Relatorio Do Lote 003

## Escopo

Lote executado sobre as linhas Excel 42 a 61 da aba `classificacao_automatizada` da copia de trabalho `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

Municipio do lote:

* Alvorada.

Arquivos usados e gerados:

* entrada do lote: `parte2/resultados/lote_003.csv`;
* resultado classificado: `parte2/resultados/lote_003_classificado.csv`;
* copia de trabalho preenchida: `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

## Regras Aplicadas

Foram preenchidas apenas:

* `Area Tematica`;
* `Gasto E ou NE`.

A coluna `Indicador` nao foi preenchida nem alterada.

As classificacoes mantiveram o padrao aprovado no lote piloto e no lote 002, com base em:

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
Educacao Infantil: 6
Saude Materno-infantil: 6
nao se aplica: 5
Assistencia Social: 3
```

Distribuicao por `Gasto E ou NE`:

```text
Nao Especifico: 13
-: 5
Especifico: 2
```

Distribuicao por confianca:

```text
Alta: 16
Media: 4
Baixa: 0
```

Linhas marcadas para revisao humana:

```text
4
```

## Linhas Revisadas

* Linha Excel 43: `AQUISICAO DE VEICULO`.
  * Classificacao aplicada: `Educacao Infantil` / `Nao Especifico`.
  * Motivo: acao em programa de educacao que pode apoiar a rede educacional, incluindo educacao infantil, mas nao explicita etapa, transporte escolar ou uso exclusivo.
* Linha Excel 44: `AQUISICAO DE VEICULO`.
  * Classificacao aplicada: `Educacao Infantil` / `Nao Especifico`.
  * Motivo: mesmo padrao da linha 43.
* Linha Excel 50: `CONSTRUCAO DO TERMINAL DE ENERGIA FOTOVOLTAICA EM PREDIOS PUBLICOS - FME`.
  * Classificacao aplicada: `Educacao Infantil` / `Nao Especifico`.
  * Motivo: despesa-meio vinculada ao FME pode sustentar infraestrutura educacional, mas o objeto e indireto e nao explicita unidade de educacao infantil.
* Linha Excel 55: `MANUTENCAO DA ALIMENTACAO ESCOLAR`.
  * Classificacao aplicada: `Educacao Infantil` / `Nao Especifico`.
  * Motivo: alimentacao escolar pode abranger educacao infantil, mas a linha nao explicita etapa infantil nem exclusividade.

## Revisao Humana

O usuario revisou o lote 003 e registrou a decisao:

```text
Continue assim, esta perfeito.
```

Assim, as 4 linhas inicialmente marcadas para revisao foram consideradas conformes, e o lote 003 fica aprovado integralmente.

## Observacao Metodologica

O lote 003 manteve o padrao aprovado anteriormente. As linhas de saude, assistencia social, ensino infantil explicito, ensino fundamental e infraestrutura urbana generica seguiram padroes ja estabilizados.

A revisao humana confirmou conformidade integral do lote 003, inclusive nos casos educacionais genericos ou indiretos.
