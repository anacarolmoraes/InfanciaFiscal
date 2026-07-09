# Infancia Fiscal - Instrucoes Para Agentes

Este arquivo orienta agentes de IA que trabalham neste repositorio. Use caminhos relativos ao projeto. Nao registre caminhos absolutos de maquina local.

## Objetivo Do Projeto

O Infancia Fiscal classifica acoes orcamentarias municipais segundo a metodologia GSPI-M, com foco em primeira infancia.

Na etapa atual, a classificacao operacional preenche somente:

```text
Area Tematica
Gasto E ou NE
```

Nao preencher, inferir ou alterar:

```text
Indicador
```

## Arquivos E Pastas Principais

Entrada original padrao:

```text
fonte_parte_2.xlsx
```

Copia de trabalho classificada:

```text
parte2/resultados/fonte_parte_2_trabalho.xlsx
```

Modelo para novos municipios:

```text
parte2/modelos/modelo_entrada_gspi.xlsx
```

Modelo para expandir municipios-base:

```text
parte2/modelos/modelo_municipios_base.xlsx
```

Base expandida de exemplos humanos:

```text
parte2/municipios_base/municipios_base_expandido.xlsx
```

Base normativa:

```text
parte2/knowledge_bundle/
```

Skills locais:

```text
skills/
```

## Skills Obrigatorias Quando Aplicavel

Use `skills/gspi-classificador/` quando a tarefa envolver:

```text
classificar planilha GSPI-M
gerar resultado classificado
gerar log, resumo ou relatorio
criar amostra de validacao
aplicar revisao humana
verificar status da classificacao
```

Use `skills/gspi-municipios-base/` quando a tarefa envolver:

```text
criar modelo para novos exemplos humanos
validar novos municipios-base
expandir municipios-base
sincronizar municipios_classificados em um workbook
```

Use `skills/xlsx/` quando a tarefa tiver planilha como entrada ou saida principal. Para usuario leigo, prefira XLSX em vez de CSV.

Use `skills/skill-creator/` quando for necessario criar ou alterar uma skill.

## Comandos Padrao

Classificacao simples:

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py run --source fonte_parte_2.xlsx
```

Verificar status:

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py status --workbook parte2\resultados\fonte_parte_2_trabalho.xlsx
```

Criar modelo de municipios-base:

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py template
```

Expandir municipios-base:

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py expand --input novos_municipios_base.xlsx
```

## Regras De Conformidade

1. Preserve o arquivo original sempre que possivel.
2. Trabalhe em copia quando houver risco de sobrescrita.
3. Nao altere `Indicador` nesta etapa.
4. Nao misture exemplos empiricos com a base normativa.
5. `parte2/knowledge_bundle/` e fonte normativa; municipios-base sao exemplos humanos.
6. Novas regras operacionais so devem ser incorporadas apos validacao humana ou decisao metodologica.
7. Para entregas a usuarios leigos, priorize arquivos `.xlsx`, README claro e comandos simples.
8. Evite scripts soltos; quando a automacao for recorrente, coloque-a em uma skill existente ou crie uma nova skill.
9. Nao use caminhos absolutos em documentacao, prompts, skills ou README.
10. Nao use unidades externas ou locais fora do repositorio para armazenar, instalar ou manipular arquivos do projeto.

## Rotulos Validamente Aceitos

Areas tematicas:

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

Tipos de gasto:

```text
Especifico
Nao Especifico
-
```

Use `-` quando `Area Tematica` for `nao se aplica`.

## Validacao Antes De Entregar

Quando alterar codigo Python:

```powershell
.venv\Scripts\python.exe -m py_compile caminho\do\arquivo.py
```

Quando alterar uma skill:

```powershell
python skills\skill-creator\scripts\quick_validate.py skills\nome-da-skill
```

Quando alterar classificacao:

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py status --workbook parte2\resultados\fonte_parte_2_trabalho.xlsx
```

Resultado esperado nesta etapa:

```text
area_filled = total de linhas classificadas
gasto_filled = total de linhas classificadas
indicador_filled = 0
```

## Postura Do Agente

Seja preciso, direto e transparente sobre incertezas. Nao apresente suposicoes como fatos. Se precisar de informacao atual, arquivo especifico ou fonte primaria, verifique antes de afirmar.

Ao responder sobre o projeto, diferencie claramente:

```text
metodologia normativa
exemplos humanos
regras operacionais validadas
classificacao automatica
revisao humana
```

Para usuarios leigos, explique o resultado em linguagem simples e indique exatamente quais arquivos foram gerados ou atualizados.
