# Workflow Operacional - Classificador GSPI-M

## 1. Preparacao

1. Confirmar que o Knowledge Bundle esta disponivel em `parte2/knowledge_bundle/`.
2. Confirmar que o arquivo operacional definitivo `fonte_parte_2.xlsx` esta disponivel na raiz do projeto.
3. Confirmar que a aba `municipios_classificados` contem os exemplos humanos.
4. Confirmar que a aba `classificacao_automatizada` contem as linhas-alvo.
5. Confirmar que a planilha contem `nomePrograma`, `nomeFuncao`, `nomeSubFuncao` e `nomeAcaoOrcamentaria`.
6. Criar copia de trabalho ou arquivo derivado em `parte2/resultados/`, preservando a planilha original.
7. Registrar modelo LLM, data, versao do bundle e prompt utilizado.

## 2. Classificacao

1. Para cada linha, enviar ao classificador os campos orcamentarios necessarios.
2. Incluir trechos relevantes do Knowledge Bundle.
3. Incluir exemplos humanos semelhantes da aba `municipios_classificados`, quando houver.
4. Receber `Area Tematica`, `Gasto E ou NE`, confianca e justificativa.
5. Preencher apenas `Area Tematica` e `Gasto E ou NE` como saidas de classificacao.
6. Registrar confianca, justificativa e duvidas em log ou arquivo derivado.
7. Manter `Indicador` fora do escopo desta etapa.

## 3. Revisao Inicial

Marcar para revisao linhas com:

* baixa confianca;
* campos faltantes;
* beneficio indireto;
* conflito entre campos;
* classificacao em area normalmente excluida;
* divergencia com exemplos humanos;
* divergencia entre Knowledge Bundle e padrao observado nos exemplos.

## 4. Comparacao Com Classificacao Humana

1. Normalizar rotulos antes da comparacao.
2. Comparar classificacao LLM com classificacao humana.
3. Registrar concordancia total, parcial ou divergente.
4. Separar divergencias por tipo: `Area Tematica` e `Gasto E ou NE`.
5. Nao avaliar `Indicador`, subarea, ponderador ou valores ponderados nesta etapa.

## 5. Revisao De Divergencias

1. Reprocessar linhas divergentes com prompt de revisao.
2. Registrar motivo da divergencia.
3. Encaminhar casos persistentes para decisao humana.

## 6. Resultado Experimental

Documentar:

* quantidade de linhas classificadas;
* taxa de concordancia geral;
* taxa de concordancia para `Area Tematica`;
* taxa de concordancia para `Gasto E ou NE`;
* taxa de concordancia conjunta das duas colunas;
* principais causas de divergencia;
* limites observados;
* recomendacoes para nova rodada.
