# Classificador GSPI-M - Parte 2

Ferramenta para classificar acoes orcamentarias municipais segundo a metodologia GSPI-M, com foco em Gasto Social com a Primeira Infancia.

O uso principal e simples: o usuario fornece uma planilha Excel no formato esperado, roda a classificacao e recebe uma copia classificada com as colunas `Area Tematica` e `Gasto E ou NE` preenchidas.

## O Que A Ferramenta Faz

A ferramenta le as linhas da aba `classificacao_automatizada` e classifica cada acao orcamentaria usando os campos:

```text
nomePrograma
nomeFuncao
nomeSubFuncao
nomeAcaoOrcamentaria
```

Ela preenche:

```text
Area Tematica
Gasto E ou NE
```

Ela nao preenche e nao deve alterar:

```text
Indicador
```

## Arquivos Mais Importantes

```text
fonte_parte_2.xlsx
```

Arquivo original de entrada, quando usado o nome padrao.

```text
parte2/resultados/fonte_parte_2_trabalho.xlsx
```

Copia de trabalho classificada. Este e o principal arquivo de resultado no fluxo padrao.

```text
parte2/resultados/classificacao_automatica_supervisionada_log.xlsx
```

Log da classificacao em Excel. Pode ser usado para auditoria, revisao e rastreabilidade.

```text
parte2/resultados/classificacao_automatica_supervisionada_resumo.json
```

Resumo tecnico da execucao.

```text
parte2/resultados/relatorio_final_classificacao.md
```

Relatorio final em Markdown com totais e distribuicoes.

```text
parte2/modelos/modelo_entrada_gspi.xlsx
```

Modelo de planilha para novos municipios.

```text
parte2/modelos/modelo_municipios_base.xlsx
```

Modelo de planilha para adicionar novos exemplos humanos aos municipios-base.

```text
parte2/municipios_base/municipios_base_expandido.xlsx
```

Base expandida de exemplos humanos. Ela nasce a partir da aba `municipios_classificados` e pode receber novos exemplos revisados.

## Instalacao

### 1. Instalar Python

Instale Python 3.10 ou superior.

No Windows, marque a opcao de adicionar Python ao `PATH` durante a instalacao.

### 2. Baixar Este Repositorio

Baixe ou clone este repositorio para o computador.

Exemplo:

```powershell
git clone <URL_DO_REPOSITORIO>
cd InfanciaFiscal
```

### 3. Criar Ambiente Virtual

No PowerShell:

```powershell
python -m venv .venv
```

Ative o ambiente:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instalar Dependencias

```powershell
pip install -r requirements.txt
```

## Formato Do Arquivo De Entrada

O arquivo deve ser uma planilha `.xlsx`.

Ele precisa ter uma aba chamada:

```text
classificacao_automatizada
```

Essa aba deve conter, no minimo, as colunas abaixo:

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

### Como Preencher A Entrada

Preencha as colunas de identificacao e descricao da acao:

```text
Id
nomeMunicipio
nomePrograma
nomeFuncao
nomeSubFuncao
nomeAcaoOrcamentaria
```

Deixe em branco as colunas que a ferramenta vai preencher:

```text
Area Tematica
Gasto E ou NE
```

Deixe tambem em branco:

```text
Indicador
```

Nesta etapa, `Indicador` fica fora do escopo.

### Aba Opcional De Exemplos Humanos

O arquivo pode conter uma aba chamada:

```text
municipios_classificados
```

Essa aba pode guardar exemplos humanos ja classificados. Ela ajuda a documentar a base de referencia, mas o uso principal da ferramenta depende da aba `classificacao_automatizada`.

## Como Rodar A Classificacao

### Opcao Mais Simples

Coloque o arquivo de entrada na raiz do projeto com o nome:

```text
fonte_parte_2.xlsx
```

Depois execute:

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py run --source fonte_parte_2.xlsx
```

O resultado sera gravado em:

```text
parte2/resultados/fonte_parte_2_trabalho.xlsx
```

O arquivo original `fonte_parte_2.xlsx` nao e alterado.

### Classificar Um Arquivo Com Outro Nome

Se o arquivo se chamar, por exemplo, `entrada_novos_municipios.xlsx`, execute:

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py run --source entrada_novos_municipios.xlsx --workbook parte2/resultados/entrada_novos_municipios_classificada.xlsx
```

O resultado ficara em:

```text
parte2/resultados/entrada_novos_municipios_classificada.xlsx
```

### Se O Arquivo De Resultado Ja Existir

Por seguranca, a ferramenta evita sobrescrever sem necessidade.

Se o arquivo de resultado ja existir, a ferramenta usa esse arquivo e classifica apenas linhas ainda em branco.

Para recriar o resultado a partir da entrada, use:

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py run --source entrada_novos_municipios.xlsx --workbook parte2/resultados/entrada_novos_municipios_classificada.xlsx --force
```

Use `--force` somente quando quiser substituir o arquivo de resultado existente.

## Onde Ver Os Resultados

Depois da execucao, confira:

```text
parte2/resultados/fonte_parte_2_trabalho.xlsx
```

ou o arquivo informado em `--workbook`.

Na aba `classificacao_automatizada`, verifique as colunas:

```text
Area Tematica
Gasto E ou NE
```

A coluna `Indicador` deve continuar vazia.

Tambem serao gerados:

```text
parte2/resultados/classificacao_automatica_supervisionada_log.xlsx
parte2/resultados/classificacao_automatica_supervisionada_resumo.json
parte2/resultados/relatorio_final_classificacao.md
```

## Como Conferir Se Deu Certo

Execute:

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py status --workbook parte2/resultados/fonte_parte_2_trabalho.xlsx
```

O resultado deve mostrar:

```text
rows: total de linhas da planilha
area_filled: linhas com Area Tematica preenchida
gasto_filled: linhas com Gasto E ou NE preenchido
indicador_filled: deve ser 0 nesta etapa
```

## Revisao Humana

Para revisar uma amostra:

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py sample --output parte2/resultados/amostra_validacao_classificacao.xlsx
```

No arquivo gerado, use as colunas:

```text
Revisao
Area Tematica Revisada
Gasto E ou NE Revisado
Comentario Revisor
```

Valores aceitos para `Revisao`:

```text
OK
Corrigir
Duvida
```

Use `OK` quando a classificacao estiver correta.

Use `Corrigir` quando quiser substituir `Area Tematica` e/ou `Gasto E ou NE`.

Use `Duvida` quando a decisao depender de discussao metodologica.

Para aplicar as correcoes:

```powershell
.venv\Scripts\python.exe skills\gspi-classificador\scripts\gspi.py apply-review --workbook parte2/resultados/fonte_parte_2_trabalho.xlsx --review parte2/resultados/amostra_validacao_classificacao.xlsx
```

## Expandir Municipios-Base

Municipios-base sao exemplos humanos ja classificados. Eles ajudam a ferramenta a manter coerencia em casos parecidos.

Eles nao substituem a metodologia GSPI-M e nao alteram automaticamente o `knowledge_bundle/`.

### Quando Expandir

Expanda a base quando houver exemplos humanos novos e revisados, por exemplo:

```text
novos municipios classificados por especialista
correcoes feitas em revisao humana
decisoes metodologicas ja consolidadas
padroes recorrentes que devem ficar documentados
```

Nao inclua linhas ainda marcadas como `Duvida`.

### 1. Criar O Modelo Para Novos Exemplos

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py template
```

O arquivo gerado fica em:

```text
parte2/modelos/modelo_municipios_base.xlsx
```

O usuario deve preencher a aba:

```text
novos_exemplos
```

Colunas principais:

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

### 2. Validar O Arquivo Preenchido

Exemplo:

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py validate --input novos_municipios_base.xlsx
```

A validacao confere:

```text
colunas obrigatorias
areas tematicas validas
tipos de gasto validos
linhas incompletas
duplicidades dentro do arquivo
combinacao nao se aplica / -
```

Se houver problemas, a ferramenta gera um Excel de validacao para o usuario corrigir.

### 3. Expandir A Base

Depois que o arquivo estiver correto:

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py expand --input novos_municipios_base.xlsx
```

O resultado fica em:

```text
parte2/municipios_base/municipios_base_expandido.xlsx
```

A ferramenta evita adicionar exemplos duplicados.

### 4. Sincronizar A Base Expandida Com Um Arquivo De Classificacao

Antes de classificar um novo arquivo, se quiser usar a base expandida como aba de exemplos humanos:

```powershell
.venv\Scripts\python.exe skills\gspi-municipios-base\scripts\municipios_base.py sync --workbook entrada_novos_municipios.xlsx
```

Isso atualiza ou cria a aba:

```text
municipios_classificados
```

no arquivo informado.

Use esse comando em uma copia do arquivo de trabalho quando quiser preservar o original intacto.

## Exemplos De Prompts Para Usar Com Codex

Use frases simples. Exemplos:

```text
Use a skill gspi-classificador e rode a classificacao do arquivo fonte_parte_2.xlsx.
```

```text
Classifique o arquivo entrada_novos_municipios.xlsx e salve o resultado em parte2/resultados/entrada_novos_municipios_classificada.xlsx.
```

```text
Verifique se a classificacao foi concluida e confirme se a coluna Indicador continua vazia.
```

```text
Gere uma amostra de validacao para revisao humana.
```

```text
Aplique as correcoes do arquivo amostra_validacao_classificacao.xlsx.
```

```text
Explique o relatorio final da classificacao em linguagem simples.
```

```text
Use a skill gspi-municipios-base e crie o modelo para eu adicionar novos municipios-base.
```

```text
Valide o arquivo novos_municipios_base.xlsx antes de expandir a base.
```

```text
Expanda os municipios-base com os exemplos revisados do arquivo novos_municipios_base.xlsx.
```

```text
Sincronize a base expandida no arquivo entrada_novos_municipios.xlsx antes de classificar.
```

## Areas Tematicas Possiveis

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

## Tipos De Gasto Possiveis

```text
Especifico
Nao Especifico
-
```

Use `-` quando a linha for classificada como `nao se aplica`.

## Cuidados Importantes

Nao edite o arquivo original sem manter copia.

Nao preencha `Indicador` nesta etapa.

Nao altere nomes das colunas obrigatorias.

Nao remova a aba `classificacao_automatizada`.

Ao classificar novos municipios, prefira gerar um novo arquivo de resultado em `parte2/resultados/`.

## Estrutura Para Explicar A Terceiros

Uma forma simples de explicar:

```text
A ferramenta recebe uma planilha de acoes orcamentarias municipais.
Ela interpreta programa, funcao, subfuncao e acao orcamentaria.
Com base na metodologia GSPI-M, ela preenche Area Tematica e Tipo de Gasto.
O arquivo original e preservado.
O resultado fica em uma copia classificada.
A coluna Indicador nao e preenchida nesta etapa.
Linhas duvidosas podem ser revisadas depois por uma pessoa.
```
