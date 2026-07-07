# Operating Manual Humano - Classificador GSPI-M

## Finalidade

Este manual orienta o operador humano a usar o classificador especializado baseado em LLM para classificar acoes orcamentarias segundo o GSPI-M.

O classificador utiliza:

* Knowledge Bundle GSPI-M;
* exemplos humanos de municipios-base;
* prompt padronizado;
* workflow operacional;
* template de classificacao.

O Knowledge Bundle foi produzido por metodologia proprietaria de engenharia de conhecimento. O entregavel contem o conhecimento operacional necessario ao uso do classificador, mas nao inclui prompts internos, heuristicas proprietarias, scripts de compilacao ou pipeline de construcao.

## Natureza Experimental

Esta etapa deve ser entendida como um experimento cientifico de classificacao assistida por LLM.

O objetivo nao e treinar uma LLM por ajuste de parametros. O objetivo e testar se uma LLM consegue reproduzir a classificacao humana quando recebe:

* conhecimento normativo estruturado no `Knowledge Bundle`;
* exemplos humanos previamente classificados;
* prompts padronizados de uso;
* um workflow de classificacao, revisao e avaliacao.

O termo metodologico mais preciso e aprendizado em contexto ou inferencia orientada por conhecimento estruturado.

## Papel Dos Artefatos

O procedimento usa tres tipos de artefatos, com funcoes diferentes.

### Knowledge Bundle

O `parte2/knowledge_bundle/` e a base normativa e operacional estruturada.

Ele contem as regras macro derivadas do Guia UNICEF/GSPI-M:

* areas tematicas;
* criterios de inclusao;
* criterios de exclusao;
* regras de gasto especifico ou ampliado;
* restricoes sobre despesas-meio;
* orientacoes sobre ponderadores, ainda que o `Indicador` nao seja classificado nesta etapa.

O bundle responde a pergunta: **quais regras a LLM deve seguir?**

### Arquivo Excel

O arquivo operacional do experimento e `fonte_parte_2.xlsx`.

Ele contem:

* aba `municipios_classificados`: exemplos humanos ja classificados;
* aba `classificacao_automatizada`: linhas que a IA devera classificar.

O Excel responde a pergunta: **quais exemplos a LLM deve observar e quais linhas ela deve classificar?**

### Prompts

Os prompts em `parte2/prompts/` sao o protocolo de uso do bundle.

Eles nao substituem o conhecimento do bundle. Eles dizem a LLM **como usar** o bundle e os exemplos humanos em cada etapa do experimento.

Os prompts respondem a pergunta: **qual procedimento a LLM deve seguir?**

## Papel Dos Prompts No Procedimento

Os prompts funcionam como instrumentos experimentais padronizados.

Eles reduzem improvisacao, tornam a execucao mais reproduzivel e permitem que terceiros entendam como a LLM foi orientada.

No procedimento, eles participam assim:

1. **Carregamento ou estudo do bundle**: a LLM deve tratar o `Knowledge Bundle` como fonte normativa principal.
2. **Estudo dos municipios-base**: a LLM deve observar a aba `municipios_classificados` como exemplos humanos de aplicacao pratica.
3. **Classificacao**: a LLM deve classificar a aba `classificacao_automatizada`, preenchendo apenas `Area Tematica` e `Gasto E ou NE`.
4. **Revisao**: linhas ambiguas, baixa confianca ou divergentes devem ser reavaliadas com prompt proprio.
5. **Avaliacao**: os resultados devem ser comparados com referencia humana nas colunas avaliaveis.

Essa separacao e importante para o experimento: o bundle e o conteudo normativo; os prompts sao o protocolo; o Excel e o campo empirico.

## Entradas Necessarias

Para cada linha, disponibilize ao classificador:

* Programa;
* Funcao;
* Subfuncao;
* Acao Orcamentaria;
* finalidade ou descricao da acao, quando disponivel;
* municipio e ano, quando disponiveis;
* exemplos de municipios-base aplicaveis, quando houver.

No uso em lote, essas entradas devem ser extraidas da aba `classificacao_automatizada` do arquivo `fonte_parte_2.xlsx`. Os exemplos humanos devem ser extraidos da aba `municipios_classificados`.

## Unidade De Inferencia

A classificacao deve considerar Programa, Funcao, Subfuncao e Acao Orcamentaria conjuntamente.

Nao aceite classificacoes feitas apenas por palavra-chave da acao.

## Saidas Esperadas

Para cada linha, o classificador deve retornar:

* area tematica;
* classificacao `Gasto E ou NE`;
* justificativa curta;
* nivel de confianca;
* campos que faltaram ou geraram duvida.

Nesta etapa, a coluna `Indicador` nao deve ser classificada. Ela deve permanecer em branco ou receber a marcacao operacional `Nao classificado nesta etapa`, se for necessario preencher algo.

## Controle De Qualidade

Revise manualmente linhas com:

* baixa confianca;
* justificativa baseada em beneficio indireto;
* conflito entre funcao/subfuncao e descricao da acao;
* classificacao em area normalmente excluida;
* gasto ampliado sem ponderador plausivel;
* divergencia em relacao aos municipios-base.

## Precedencia

Em caso de conflito:

1. prevalece o Guia UNICEF/GSPI-M;
2. depois o Knowledge Bundle;
3. depois exemplos humanos dos municipios-base;
4. por ultimo a inferencia da LLM.

Na pratica, como o Guia foi transformado em bundle, o operador deve tratar o `Knowledge Bundle` como representacao estruturada da fonte normativa principal. Os exemplos humanos ajudam a interpretar, mas nao podem revogar a regra do bundle.

## Registro

Mantenha registro da versao do bundle, prompt usado, modelo LLM, data da classificacao e eventuais revisoes humanas.

Para fins cientificos, registre tambem:

* arquivo Excel utilizado;
* abas utilizadas;
* quantidade de linhas classificadas;
* quantidade de linhas revisadas;
* criterio de normalizacao de rotulos;
* metrica de concordancia usada;
* divergencias qualitativas identificadas.
