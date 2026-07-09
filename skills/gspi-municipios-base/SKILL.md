---
name: gspi-municipios-base
description: "Expand, validate, consolidate, and sync GSPI-M municipios-base examples for this project. Use this skill whenever the user wants to add new human-classified municipalities, expand municipios_base, import reviewed classifications into the base, create an XLSX template for new base examples, validate Area Tematica/Gasto E ou NE labels, deduplicate examples, or update the municipios_classificados sheet used by the GSPI-M classifier."
---

# GSPI-M Municipios-Base

Use this skill when the user wants to expand the human example base used by the GSPI-M classifier.

The goal is to make base expansion safe for non-technical users:

1. the user fills an XLSX template;
2. the tool validates the examples;
3. valid examples are consolidated into an expanded base workbook;
4. the expanded base can be synced into a working classification workbook.

## Core Rule

Do not update the normative `knowledge_bundle/` just because examples were added.

Municipios-base are empirical examples. They help calibrate interpretation, but they do not override the GSPI-M methodology.

## Standard Files

Default original source workbook:

```text
fonte_parte_2.xlsx
```

Default expanded base:

```text
parte2/municipios_base/municipios_base_expandido.xlsx
```

Default new examples template:

```text
parte2/modelos/modelo_municipios_base.xlsx
```

Default workbook sheet that stores human examples:

```text
municipios_classificados
```

## Main Tool

Use the bundled CLI instead of creating one-off scripts:

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py <command> [options]
```

## Commands

### 1. Init Base

Create the initial expanded base from the existing `municipios_classificados` sheet.

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py init
```

### 2. Create Template

Create an XLSX file for the user to fill with new human-classified examples.

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py template
```

### 3. Validate New Examples

Check whether the XLSX filled by the user has required columns, accepted labels, and usable examples.

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py validate --input parte2\modelos\modelo_municipios_base.xlsx
```

### 4. Expand Base

Append valid examples from a reviewed XLSX into the expanded base workbook.

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py expand --input novos_municipios_base.xlsx
```

### 5. Sync To Workbook

Copy the expanded base into the `municipios_classificados` sheet of a workbook used by the classifier.

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py sync --workbook fonte_parte_2.xlsx
```

## Input Requirements

The user-facing XLSX must contain a sheet named:

```text
novos_exemplos
```

Required columns:

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
Fonte Revisao
Comentario Revisor
```

`Fonte Revisao` should say where the human decision came from, such as:

```text
revisao humana
ata metodologica
validacao cliente
```

## Accepted Labels

Accepted `Area Tematica` values:

```text
Educacao Infantil
Saude Materno-infantil
Assistencia Social
Protecao dos Direitos da Crianca e da Familia
Direito a Cidade e Habitacao
Saneamento e Agua
Cultura e Direito de Brincar
Seguranca Alimentar
Enfrentamento da Pobreza
nao se aplica
```

Accepted `Gasto E ou NE` values:

```text
Especifico
Nao Especifico
-
```

Use `-` when `Area Tematica` is `nao se aplica`.

## Review Logic

Only add examples that have both:

```text
Area Tematica
Gasto E ou NE
```

Keep `Indicador` exactly as supplied by the reviewer. If the current project stage still does not use `Indicador`, it may remain blank.

When a row is incomplete or uses an invalid label, do not add it silently. Generate a validation workbook/report so the user can fix it in Excel.

## References

Read only when needed:

* `references/fluxo-expansao.md`: user-facing workflow and decision rules.
