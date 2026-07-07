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

## Entradas Necessarias

Para cada linha, disponibilize ao classificador:

* Programa;
* Funcao;
* Subfuncao;
* Acao Orcamentaria;
* finalidade ou descricao da acao, quando disponivel;
* municipio e ano, quando disponiveis;
* exemplos de municipios-base aplicaveis, quando houver.

## Unidade De Inferencia

A classificacao deve considerar Programa, Funcao, Subfuncao e Acao Orcamentaria conjuntamente.

Nao aceite classificacoes feitas apenas por palavra-chave da acao.

## Saidas Esperadas

Para cada linha, o classificador deve retornar:

* decisao GSPI: `GSPI` ou `Nao GSPI`;
* area tematica, se `GSPI`;
* subarea tematica, se identificavel;
* classificacao E/NE: `Especifico` ou `Ampliado`;
* ponderador sugerido, se `Ampliado`;
* justificativa curta;
* nivel de confianca;
* campos que faltaram ou geraram duvida.

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

## Registro

Mantenha registro da versao do bundle, prompt usado, modelo LLM, data da classificacao e eventuais revisoes humanas.
