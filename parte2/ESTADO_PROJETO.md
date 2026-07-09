# Estado Do Projeto - Parte 2 GSPI-M

## 1. Objetivo

Construir e aplicar um classificador especializado baseado em LLM para classificar acoes orcamentarias municipais segundo a metodologia GSPI-M, usando:

* `parte2/knowledge_bundle/` como base normativa e metodologica;
* `fonte_parte_2.xlsx` como arquivo operacional original;
* `parte2/resultados/fonte_parte_2_trabalho.xlsx` como copia de trabalho classificada;
* logs e relatorios para auditoria da classificacao.

Nesta etapa, foram preenchidas apenas:

* `Area Tematica`;
* `Gasto E ou NE`.

A coluna `Indicador` ficou fora do escopo e nao foi preenchida.

## 2. Arquivos Principais

### Entrada

* `fonte_parte_2.xlsx`: arquivo original, preservado sem alteracao.
* `parte2/knowledge_bundle/`: base normativa/metodologica estruturada.
* `parte2/guia_unicef.md`: Guia UNICEF convertido para Markdown.

### Saida Principal

* `parte2/resultados/fonte_parte_2_trabalho.xlsx`: copia de trabalho com a aba `classificacao_automatizada` classificada.

### Auditoria E Relatorios

* `parte2/resultados/classificacao_automatica_supervisionada_log.csv`;
* `parte2/resultados/classificacao_automatica_supervisionada_resumo.json`;
* `parte2/resultados/relatorio_classificacao_automatica_supervisionada.md`;
* `parte2/resultados/relatorio_lote_piloto_001.md`;
* `parte2/resultados/relatorio_lote_002.md`;
* `parte2/resultados/relatorio_lote_003.md`;
* `parte2/resultados/relatorio_lote_004.md`;
* `parte2/resultados/relatorio_lote_005.md`;
* `parte2/resultados/relatorio_lote_006.md`.

## 3. O Que Foi Feito

### 3.1 Preparacao Metodologica

Foram criados e/ou alinhados:

* conversao do Guia UNICEF para Markdown;
* Knowledge Bundle GSPI-M em `parte2/knowledge_bundle/`;
* manuais de operacao humana e da LLM;
* prompts de classificacao, avaliacao e revisao;
* workflow operacional;
* scripts de preparacao, aplicacao e classificacao.

O Knowledge Bundle cobre:

* criterios de inclusao;
* criterios de exclusao;
* despesas-meio e despesas finalisticas;
* gasto especifico ou ampliado;
* ponderadores;
* estrutura da planilha;
* nove areas tematicas GSPI-M.

### 3.2 Inspecao Do Excel

Foi confirmado que `fonte_parte_2.xlsx` possui:

* aba `municipios_classificados`: exemplos humanos;
* aba `classificacao_automatizada`: linhas-alvo.

Dimensoes observadas:

* `municipios_classificados`: 2.956 linhas de dados;
* `classificacao_automatizada`: 7.010 linhas de dados.

### 3.3 Lotes Iniciais

Foram executados lotes manuais/supervisionados de calibracao:

* lote piloto 001: linhas Excel 2 a 21;
* lote 002: linhas Excel 22 a 41;
* lote 003: linhas Excel 42 a 61;
* lote 004: linhas Excel 62 a 81;
* lote 005: linhas Excel 82 a 101;
* lote 006: linhas Excel 102 a 121.

Total nos lotes iniciais:

```text
120 linhas classificadas
```

As validacoes humanas registradas aprovaram os padroes aplicados nos lotes iniciais.

### 3.4 Execucao Automatica Supervisionada

Apos aprovacao do usuario, foi executado modo automatico supervisionado para classificar o restante da aba.

Resultado:

```text
linhas ja preenchidas antes da execucao automatica: 120
linhas aplicadas na execucao automatica: 6890
total de linhas de dados classificadas: 7010
Indicador preenchido: 0
```

Validador final confirmou:

```text
rows: 7010
area_filled: 7010
gasto_filled: 7010
indicador_filled: 0
```

## 4. Estado Atual

O projeto esta com a classificacao operacional completa na copia de trabalho:

```text
parte2/resultados/fonte_parte_2_trabalho.xlsx
```

Status:

* `fonte_parte_2.xlsx` original preservado;
* `classificacao_automatizada` completamente classificada na copia de trabalho;
* `Area Tematica` preenchida em 7.010 linhas;
* `Gasto E ou NE` preenchido em 7.010 linhas;
* `Indicador` sem preenchimento;
* log consolidado criado;
* 558 linhas marcadas para revisao humana posterior.

## 5. Distribuicao Da Classificacao Automatica

Distribuicao por `Area Tematica` nas 6.890 linhas aplicadas automaticamente:

```text
nao se aplica: 3471
Saude Materno-infantil: 1724
Assistencia Social: 1010
Educacao Infantil: 509
Saneamento e Agua: 114
Protecao dos Direitos da Crianca e da Familia: 60
Seguranca Alimentar: 2
```

Distribuicao por `Gasto E ou NE`:

```text
-: 3471
Nao Especifico: 2958
Especifico: 461
```

Distribuicao por confianca:

```text
Alta: 6332
Media: 558
Baixa: 0
```

Linhas marcadas para revisao humana:

```text
558
```

## 6. Decisoes Metodologicas Ativas

* O arquivo original `fonte_parte_2.xlsx` deve permanecer preservado.
* A copia operacional classificada e `parte2/resultados/fonte_parte_2_trabalho.xlsx`.
* Nesta etapa, classificar apenas `Area Tematica` e `Gasto E ou NE`.
* Nao preencher `Indicador` nesta etapa.
* O Knowledge Bundle permanece como base normativa.
* Padroes aprendidos na classificacao automatica devem ser tratados como camada operacional/empirica ate validacao humana.
* Atualizacoes no Knowledge Bundle devem ocorrer apenas depois de decisao metodologica consolidada, para evitar misturar regra normativa com comportamento empirico ainda nao auditado.

## 7. Sobre Municipios-Base

Os municipios-base atuais foram suficientes para estabilizar muitos padroes recorrentes, como:

* saude geral, FMS, UBS, vigilancia, ACS e assistencia farmaceutica;
* CRAS, CREAS, FMAS e beneficios eventuais;
* educacao infantil explicita;
* ensino fundamental fora do escopo;
* legislativo, administracao geral, fincas/planejamento e iluminacao publica fora do escopo;
* saneamento, aterro, limpeza publica e residuos como casos de saneamento/agua quando cabivel.

Ainda assim, pode ser util ampliar municipios-base depois da validacao, especialmente se houver divergencias sistematicas nas 558 linhas marcadas para revisao.

Recomendacao atual:

* nao aumentar municipios-base antes da primeira validacao;
* primeiro revisar excecoes e amostra de alta confianca;
* aumentar municipios-base apenas se a revisao revelar padroes locais nao cobertos.

## 8. Sobre Atualizacao Do Bundle

Nao e recomendado atualizar diretamente o `knowledge_bundle/` com todo o conhecimento gerado pela classificacao automatica.

Melhor abordagem:

1. manter `knowledge_bundle/` como fonte normativa limpa;
2. criar uma camada separada de decisoes operacionais validadas;
3. transformar apenas decisoes humanas consolidadas em regras complementares;
4. depois, se fizer sentido, incorporar essas regras ao bundle como conhecimento operacional validado.

Possivel arquivo futuro:

```text
parte2/knowledge_bundle/metodologia/regras-operacionais-validadas.md
```

Mas ele so deve ser criado depois da revisao humana das excecoes ou de uma amostra suficiente.

## 9. Trabalhos Futuros

### 9.1 Validacao Por Excecao

Revisar:

```text
parte2/resultados/classificacao_automatica_supervisionada_log.csv
```

Filtro principal:

```text
Requer revisao humana = Sim
```

Total:

```text
558 linhas
```

### 9.2 Validacao Por Amostragem

Criar amostra estratificada por:

* municipio;
* area tematica;
* tipo de gasto;
* confianca;
* padroes de acao orcamentaria.

Objetivo:

* confirmar a consistencia das linhas de alta confianca;
* identificar possiveis vieses ou erros sistematicos;
* medir taxa de acerto por grupo.

### 9.3 Colunas De Revisao

Para revisar manualmente, recomenda-se criar colunas:

```text
Revisao
Area Tematica Revisada
Gasto E ou NE Revisado
Comentario Revisor
```

Valores sugeridos para `Revisao`:

```text
OK
Corrigir
Duvida
```

### 9.4 Aplicacao De Correcoes

Depois da revisao:

* aplicar correcoes pontuais na copia de trabalho;
* gerar relatorio de alteracoes;
* registrar padroes corrigidos;
* decidir se algum padrao deve virar regra operacional validada.

### 9.5 Relatorio Final

Produzir relatorio final com:

* total classificado;
* total revisado;
* taxa de manutencao;
* taxa de correcao;
* divergencias por area;
* divergencias por municipio;
* padroes metodologicos consolidados;
* limites da classificacao.

## 10. Proximo Passo Recomendado

Criar um arquivo de validacao com:

* todas as 558 linhas marcadas para revisao humana;
* uma amostra estratificada das linhas de alta confianca.

Nome sugerido:

```text
parte2/resultados/amostra_validacao_classificacao.csv
```

Depois disso, revisar manualmente usando as colunas:

```text
Revisao
Area Tematica Revisada
Gasto E ou NE Revisado
Comentario Revisor
```
