# Prompt - Revisao De Classificacao GSPI-M

Voce revisa classificacoes GSPI-M marcadas como duvidosas, divergentes ou de baixa confianca.

Nesta etapa, a revisao deve limitar a classificacao a `Area Tematica` e `Gasto E ou NE`.

## Entrada

```text
Linha:
Area Tematica original:
Gasto E ou NE original:
Justificativa original:
Classificacao humana, se houver:
Trechos relevantes do Knowledge Bundle:
Exemplos humanos semelhantes da aba municipios_classificados:
```

## Tarefa

1. Reavalie a linha usando `nomePrograma`, `nomeFuncao`, `nomeSubFuncao` e `nomeAcaoOrcamentaria`.
2. Aplique criterios de inclusao e exclusao.
3. Verifique `Area Tematica` e `Gasto E ou NE`.
4. Identifique a fonte da divergencia.
5. Proponha classificacao revisada.

Nao revise `Indicador`, subarea tematica, ponderador ou valor ponderado nesta etapa.

Em caso de conflito entre Knowledge Bundle e exemplos humanos, prevalece o Knowledge Bundle.

## Saida

```text
Area tematica:
Gasto E ou NE:
Motivo da revisao:
Evidencia usada:
Confianca:
Necessita decisao humana: Sim / Nao
```
