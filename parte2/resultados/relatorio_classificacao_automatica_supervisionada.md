# Relatorio Da Classificacao Automatica Supervisionada

## Escopo

Execucao em modo automatico supervisionado sobre a aba `classificacao_automatizada` da copia de trabalho:

```text
parte2/resultados/fonte_parte_2_trabalho.xlsx
```

Foram classificadas as linhas ainda nao preenchidas apos os lotes manuais/supervisionados iniciais.

Intervalo aplicado:

```text
linhas Excel 122 a 7011
```

Total aplicado nesta execucao:

```text
6890 linhas
```

Antes desta execucao ja estavam preenchidas:

```text
120 linhas
```

Total previsto da aba:

```text
7010 linhas de dados
```

## Arquivos Gerados

* `parte2/resultados/classificacao_automatica_supervisionada_log.csv`;
* `parte2/resultados/classificacao_automatica_supervisionada_resumo.json`;
* `parte2/resultados/relatorio_classificacao_automatica_supervisionada.md`;
* `parte2/resultados/fonte_parte_2_trabalho.xlsx` atualizado.

## Regras Aplicadas

Foram preenchidas apenas:

* `Area Tematica`;
* `Gasto E ou NE`.

A coluna `Indicador` nao foi preenchida nem alterada.

A planilha original `fonte_parte_2.xlsx` nao foi alterada.

## Distribuicao Da Execucao Automatica

Distribuicao por `Area Tematica` nas 6890 linhas aplicadas:

```text
nao se aplica: 3471
Saude Materno-infantil: 1724
Assistencia Social: 1010
Educacao Infantil: 509
Saneamento e Agua: 114
Protecao dos Direitos da Crianca e da Familia: 60
Seguranca Alimentar: 2
```

Distribuicao por `Gasto E ou NE`:

```text
-: 3471
Nao Especifico: 2958
Especifico: 461
```

Distribuicao por confianca:

```text
Alta: 6332
Media: 558
Baixa: 0
```

Linhas marcadas para revisao humana:

```text
558
```

## Distribuicao Por Municipio

```text
Gurupi: 1174
Araguacu: 1109
Formoso do Araguaia: 949
Figueiropolis: 769
Santa Rita do Tocantins: 702
Parana: 604
Cariri do Tocantins: 510
Sucupira: 386
Oliveira de Fatima: 375
Alvorada: 312
```

## Observacao Metodologica

A execucao automatica supervisionada aplicou os padroes estabilizados nos lotes iniciais, preservando trilha de auditoria em CSV.

As linhas marcadas para revisao humana nao foram bloqueadas; elas foram classificadas e aplicadas na copia de trabalho, mas permaneceram identificadas no log para revisao posterior por amostragem ou por excecao.

As principais classes de revisao sao:

* despesas-meio de educacao sem etapa infantil explicita;
* transporte/alimentacao escolar sem etapa explicitada;
* politicas para mulheres;
* conselhos tutelares e protecao ampla de criancas/adolescentes;
* saneamento/residuos quando aparecem em funcao ambiental;
* acoes de renda, seguranca alimentar ou direito a cidade com publico-alvo amplo.

## Resultado

A classificacao da aba `classificacao_automatizada` foi completada na copia de trabalho.

O arquivo definitivo para continuidade operacional e:

```text
parte2/resultados/fonte_parte_2_trabalho.xlsx
```
