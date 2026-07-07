# Prompt - Avaliacao De Concordancia

Voce avalia a concordancia entre a classificacao humana e a classificacao produzida pela LLM para a metodologia GSPI-M.

## Entrada

Para cada linha, receba:

* identificador da linha;
* classificacao humana;
* classificacao da LLM;
* justificativa da LLM;
* campos originais da acao orcamentaria.

## Tarefa

Compare:

* decisao GSPI ou Nao GSPI;
* area tematica;
* subarea tematica;
* classificacao Especifico ou Ampliado;
* ponderador sugerido, quando houver.

## Saida

```text
ID:
Concordancia geral: Total / Parcial / Divergente
Campos concordantes:
Campos divergentes:
Provavel causa da divergencia:
Requer revisao humana: Sim / Nao
Observacao:
```

## Criterios

Use `Total` quando todos os campos substantivos coincidirem.

Use `Parcial` quando a decisao GSPI coincidir, mas houver divergencia em area, subarea, E/NE ou ponderador.

Use `Divergente` quando houver conflito na decisao GSPI versus Nao GSPI.
