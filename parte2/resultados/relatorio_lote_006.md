# Relatorio Do Lote 006

## Escopo

Lote executado sobre as linhas Excel 102 a 121 da aba `classificacao_automatizada` da copia de trabalho `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

Municipio do lote:

* Alvorada.

Arquivos usados e gerados:

* entrada do lote: `parte2/resultados/lote_006.csv`;
* resultado classificado: `parte2/resultados/lote_006_classificado.csv`;
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
nao se aplica: 8
Educacao Infantil: 4
Assistencia Social: 4
Saude Materno-infantil: 2
Protecao dos Direitos da Crianca e da Familia: 2
```

Distribuicao por `Gasto E ou NE`:

```text
Nao Especifico: 9
-: 8
Especifico: 3
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

## Linhas Que Requerem Revisao

* Linha Excel 110: `MANUTENCAO DO FUNDO MUNICIPAL DE EDUCACAO - FME`.
  * Classificacao aplicada: `Educacao Infantil` / `Nao Especifico`.
  * Motivo: padrao aprovado para FME em administracao geral, mas a linha nao explicita etapa infantil.
* Linha Excel 113: `GESTAO DA SECRETARIA MUNICIPAL DE POLITICAS PARA MULHERES`.
  * Classificacao aplicada: `Protecao dos Direitos da Crianca e da Familia` / `Nao Especifico`.
  * Motivo: padrao aprovado para politicas para mulheres, mas a linha nao explicita primeira infancia, gestantes ou lactantes.
* Linha Excel 121: `MANUTENCAO DO CONSELHO TUTELAR`.
  * Classificacao aplicada: `Protecao dos Direitos da Crianca e da Familia` / `Nao Especifico`.
  * Motivo: Conselho Tutelar protege direitos de criancas e adolescentes, incluindo primeira infancia, mas nao e exclusivo de criancas de 0 a 6 anos.

## Observacao Metodologica

O lote 006 manteve o padrao aprovado nos lotes anteriores. As linhas de saude, ensino infantil explicito, CRAS, beneficio eventual, legislativo, agricultura, iluminacao publica, cultura geral, administracao geral e sentencas judiciais seguiram padroes ja estabilizados.

As linhas marcadas para revisao concentram casos de beneficio ampliado ou despesa-meio sem publico-alvo exclusivo.
