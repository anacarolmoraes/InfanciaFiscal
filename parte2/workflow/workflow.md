# Workflow Operacional - Classificador GSPI-M

## 1. Preparacao

1. Confirmar que o Knowledge Bundle esta disponivel em `parte2/knowledge_bundle/`.
2. Confirmar que os municipios-base estao disponiveis em `parte2/municipios_base/`.
3. Confirmar que a planilha de entrada contem Programa, Funcao, Subfuncao e Acao Orcamentaria.
4. Registrar modelo LLM, data, versao do bundle e prompt utilizado.

## 2. Classificacao

1. Para cada linha, enviar ao classificador os campos orcamentarios necessarios.
2. Incluir trechos relevantes do Knowledge Bundle.
3. Incluir exemplos-base semelhantes, quando houver.
4. Receber decisao GSPI, area, subarea, E/NE, ponderador, confianca e justificativa.

## 3. Revisao Inicial

Marcar para revisao linhas com:

* baixa confianca;
* campos faltantes;
* beneficio indireto;
* conflito entre campos;
* classificacao em area normalmente excluida;
* divergencia com exemplos-base;
* gasto ampliado sem ponderador.

## 4. Comparacao Com Classificacao Humana

1. Comparar classificacao LLM com classificacao humana.
2. Registrar concordancia total, parcial ou divergente.
3. Separar divergencias por tipo: GSPI, area, subarea, E/NE, ponderador.

## 5. Revisao De Divergencias

1. Reprocessar linhas divergentes com prompt de revisao.
2. Registrar motivo da divergencia.
3. Encaminhar casos persistentes para decisao humana.

## 6. Resultado Experimental

Documentar:

* quantidade de linhas classificadas;
* taxa de concordancia geral;
* taxa de concordancia por campo;
* principais causas de divergencia;
* limites observados;
* recomendacoes para nova rodada.
