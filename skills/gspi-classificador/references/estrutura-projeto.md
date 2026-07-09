# Estrutura Do Projeto GSPI-M

## Entradas

```text
fonte_parte_2.xlsx
parte2/knowledge_bundle/
parte2/guia_unicef.md
```

## Saidas Operacionais

```text
parte2/resultados/fonte_parte_2_trabalho.xlsx
parte2/resultados/classificacao_automatica_supervisionada_log.xlsx
parte2/resultados/classificacao_automatica_supervisionada_resumo.json
```

## Campos Obrigatorios Da Aba `classificacao_automatizada`

```text
Id
nomeMunicipio
nomePrograma
nomeFuncao
nomeSubFuncao
nomeAcaoOrcamentaria
Area Tematica
Gasto E ou NE
Indicador
```

O cabecalho de `Area Tematica` pode aparecer com problema de acentuacao. Detecte por aproximacao quando necessario.

## Campos De Revisao Sugeridos

```text
Revisao
Area Tematica Revisada
Gasto E ou NE Revisado
Comentario Revisor
```
