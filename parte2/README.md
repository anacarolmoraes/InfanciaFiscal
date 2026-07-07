# Parte 2 - Classificador Especializado GSPI-M

Esta pasta contem os artefatos entregaveis para uso de um classificador especializado baseado em LLM para a classificacao de acoes orcamentarias segundo o GSPI-M.

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
* `municipios_base/`: exemplos humanos de referencia.
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

## Nota Sobre Metodologia Proprietaria

O Knowledge Bundle foi produzido por metodologia proprietaria de engenharia de conhecimento. Esta pasta contem o produto operacional necessario ao uso do classificador, sem expor a implementacao interna do metodo de construcao.
