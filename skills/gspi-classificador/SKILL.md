---
name: gspi-classificador
description: "Execute, audit, validate, and maintain the GSPI-M budget-action classification workflow for this project. Use this skill whenever the user wants to classify fonte_parte_2.xlsx or a similar GSPI-M workbook, prepare a work copy, fill only Area Tematica and Gasto E ou NE, preserve Indicador, generate validation samples, apply human review corrections, produce audit reports, or organize the GSPI-M classification project for non-technical users."
---

# GSPI-M Classificador

Use this skill to run the GSPI-M classification workflow as a clean, repeatable operation.

## Core Rule

Preserve the original workbook. Work on a copy.

Fill only:

```text
Area Tematica
Gasto E ou NE
```

Do not fill or modify:

```text
Indicador
```

## Standard Files

Default original workbook:

```text
fonte_parte_2.xlsx
```

Default working workbook:

```text
parte2/resultados/fonte_parte_2_trabalho.xlsx
```

Default classification sheet:

```text
classificacao_automatizada
```

Default human examples sheet:

```text
municipios_classificados
```

If the user wants to add new human examples or expand municipios-base before classification, use the separate `gspi-municipios-base` skill first. This classifier should consume the resulting workbook/base, not manage base expansion itself.

## Main Tool

Use the bundled CLI instead of creating new one-off scripts:

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py <command> [options]
```

If `.venv` is unavailable, use the available Python with `openpyxl` installed.

## Commands

### 1. Run

Use this as the default user-facing command. It prepares the working copy when needed, classifies blank rows, creates the log, creates the summary, and creates the report.

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py run --source fonte_parte_2.xlsx
```

Use `--force` only when intentionally replacing the current working copy.

### 2. Status

Inspect workbook progress.

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py status --workbook parte2\resultados\fonte_parte_2_trabalho.xlsx
```

### 3. Prepare

Create a working copy while preserving the original.

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py prepare --source fonte_parte_2.xlsx --output parte2\resultados\fonte_parte_2_trabalho.xlsx
```

### 4. Classify

Classify blank rows in the target sheet and create audit logs.

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py classify --workbook parte2\resultados\fonte_parte_2_trabalho.xlsx
```

### 5. Sample

Create a validation sample containing all review-flagged rows plus a stratified high-confidence sample.

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py sample --log parte2\resultados\classificacao_automatica_supervisionada_log.xlsx --output parte2\resultados\amostra_validacao_classificacao.xlsx
```

### 6. Apply Review

Apply human review decisions from an XLSX review workbook containing:

```text
Revisao
Area Tematica Revisada
Gasto E ou NE Revisado
Comentario Revisor
```

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py apply-review --workbook parte2\resultados\fonte_parte_2_trabalho.xlsx --review parte2\resultados\amostra_validacao_classificacao.xlsx
```

### 7. Report

Generate a compact Markdown report from the workbook and log.

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py report --workbook parte2\resultados\fonte_parte_2_trabalho.xlsx --log parte2\resultados\classificacao_automatica_supervisionada_log.xlsx --output parte2\resultados\relatorio_final_validacao.md
```

## Human Review Values

Use:

```text
OK
Corrigir
Duvida
```

Meaning:

* `OK`: keep the automated classification.
* `Corrigir`: apply `Area Tematica Revisada` and/or `Gasto E ou NE Revisado`.
* `Duvida`: do not auto-correct; group for methodological decision.

## References

Read only when needed:

* `references/regras-operacionais.md`: classification policy and review logic.
* `references/estrutura-projeto.md`: expected project files and folder layout.
