# Prompt - Avaliacao De Concordancia

Voce avalia a concordancia entre a classificacao humana e a classificacao produzida pela LLM para a metodologia GSPI-M.

A avaliacao desta etapa usa o arquivo operacional `fonte_parte_2.xlsx` e compara apenas as colunas de classificacao previstas para a etapa atual.

## Entrada

Para cada linha, receba:

* identificador da linha;
* `Area Tematica` humana;
* `Gasto E ou NE` humano;
* `Area Tematica` da LLM;
* `Gasto E ou NE` da LLM;
* justificativa da LLM;
* campos originais da acao orcamentaria.

## Tarefa

Compare:

* `Area Tematica`;
* `Gasto E ou NE`.

Nao avalie `Indicador`, subarea tematica, ponderador ou valores ponderados nesta etapa.

Antes da comparacao, normalize rotulos para reduzir divergencias artificiais por caixa, acentuacao, espacos, erros de digitacao conhecidos, valores vazios, tracos ou `nao se aplica`.

## Saida

```text
ID:
Concordancia geral: Total / Parcial / Divergente
Area Tematica: Concordante / Divergente
Gasto E ou NE: Concordante / Divergente
Provavel causa da divergencia:
Requer revisao humana: Sim / Nao
Observacao:
```

## Criterios

Use `Total` quando todos os campos substantivos coincidirem.

Use `Parcial` quando apenas uma das duas colunas avaliadas coincidir.

Use `Divergente` quando as duas colunas avaliadas divergirem ou quando a divergencia alterar o enquadramento substantivo da linha.

A normalizacao deve ser aplicada na avaliacao ou em arquivo derivado, sem alterar a planilha original sem registro.
