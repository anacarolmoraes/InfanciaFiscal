# Parte 2 - Classificador Especializado GSPI-M

Esta pasta contem os artefatos entregaveis para uso de um classificador especializado baseado em LLM para a classificacao de acoes orcamentarias segundo o GSPI-M.

Para uso por cliente final, consulte primeiro o README principal do repositorio:

```text
README.md
```

Ele explica instalacao, formato da planilha de entrada, comandos de execucao, arquivos de resultado e exemplos de prompts para uso com Codex.

## Arquitetura Do Experimento

O experimento separa tres camadas:

* `knowledge_bundle/`: conhecimento normativo estruturado derivado do Guia UNICEF/GSPI-M.
* `fonte_parte_2.xlsx`: arquivo operacional com exemplos humanos e linhas a classificar.
* `prompts/`: protocolo padronizado que orienta como a LLM deve usar o bundle e o Excel.

O bundle define as regras. O Excel fornece exemplos e casos-alvo. Os prompts tornam o procedimento reproduzivel.

## Conteudo

* `guia_unicef.md`: Guia UNICEF convertido localmente de PDF para Markdown.
* `knowledge_bundle/`: Knowledge Bundle em formato OKF.
* `manuals/`: manuais de operacao humana e da LLM.
* `prompts/`: prompts padronizados de classificacao, avaliacao e revisao.
* `workflow/`: fluxo operacional de classificacao e avaliacao.
* `municipios_base/`: exemplos humanos de referencia e base expandida em XLSX.
* `resultados/`: saidas de classificacao e avaliacao.

## Arquivo Operacional

O arquivo operacional definitivo fica na raiz do projeto:

```text
fonte_parte_2.xlsx
```

Ele contem:

* `municipios_classificados`: exemplos humanos previamente classificados;
* `classificacao_automatizada`: linhas que a IA devera classificar.

Nesta etapa, devem ser preenchidas apenas as colunas `Area Tematica` e `Gasto E ou NE`. A coluna `Indicador` fica fora do escopo.

## Expansao De Municipios-Base

Para adicionar novos exemplos humanos revisados, use a skill:

```text
skills/gspi-municipios-base/
```

O fluxo recomendado e:

```text
criar modelo XLSX -> preencher novos exemplos -> validar -> expandir base -> sincronizar com workbook de classificacao
```

Arquivos principais:

```text
parte2/modelos/modelo_municipios_base.xlsx
parte2/municipios_base/municipios_base_expandido.xlsx
```

## Nota Sobre Metodologia Proprietaria

O Knowledge Bundle foi produzido por metodologia proprietaria de engenharia de conhecimento. Esta pasta contem o produto operacional necessario ao uso do classificador, sem expor a implementacao interna do metodo de construcao.
