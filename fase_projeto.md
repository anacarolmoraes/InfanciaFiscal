# Fase Do Projeto - Parte 2

## Objetivo Da Parte 2

Construir um classificador especializado baseado em LLM para reproduzir a classificacao humana de acoes orcamentarias segundo o Guia UNICEF/GSPI-M.

O experimento testa inferencia em contexto, nao treinamento por ajuste de parametros.

A LLM deve usar:

* `parte2/knowledge_bundle/` como base normativa e metodologica estruturada;
* `fonte_parte_2.xlsx` como arquivo operacional com exemplos humanos e linhas a classificar;
* prompts padronizados como protocolo experimental;
* manuais e workflow para reproducibilidade.

## Restricoes E Decisoes Ativas

* Cada passo operacional deve ser executado com permissao explicita do usuario.
* O modo de trabalho deve seguir `operating-manual_fable.md`.
* A metodologia proprietaria pode ser mencionada em alto nivel, mas nao devem ser expostos prompts internos, heuristicas proprietarias, scripts de compilacao ou pipeline interno de construcao.
* O arquivo definitivo para execucao da metodologia e `fonte_parte_2.xlsx`.
* A estrutura atual do projeto nao deve ser renomeada sem nova decisao do usuario.
* Operacoes de leitura, analise ou edicao de Excel devem usar a skill local `skills/xlsx`.
* Nesta etapa, a IA deve preencher apenas:
  * `Area Tematica`;
  * `Gasto E ou NE`.
* A coluna `Indicador` nao deve ser classificada nesta etapa.

## Arquivos De Referencia

* `PARTE2.md`: documento-base da Parte 2.
* `PARTE2_COMPLEMENTO.md`: complemento metodologico alinhado ao projeto atual.
* `operating-manual_fable.md`: manual de modo de trabalho exigido pelo usuario.
* `skills/xlsx/SKILL.md`: skill local para leitura, analise e edicao de arquivos Excel.
* `fonte_parte_2.xlsx`: arquivo operacional definitivo.
* `Guia de Apuracao do Gasto Social com a Primeira Infancia (GSPI-M).pdf.pdf`: PDF fonte.

## O Que Foi Feito

### 1. Leitura Da Metodologia

Foram lidos:

* `operating-manual_fable.md`;
* `PARTE2.md`;
* `PARTE2_COMPLEMENTO.md`.

O entendimento consolidado e:

```text
Guia UNICEF
  -> Knowledge Bundle
  -> LLM entende metodologia macro

fonte_parte_2.xlsx
  -> municipios_classificados = exemplos humanos
  -> classificacao_automatizada = linhas a classificar pela IA
```

### 2. Atualizacao Da Skill `pdf-to-md`

A skill local `skills/pdf-to-md` foi atualizada.

Arquivos alterados:

* `skills/pdf-to-md/SKILL.md`;
* `skills/pdf-to-md/scripts/convert.py`.

Melhorias implementadas:

* deteccao de `.venv` ou `venv`;
* execucao local do `pdfmd`;
* validacao automatica do Markdown convertido;
* geracao de relatorio `*.conversion_report.json`;
* fallback local com `pdfplumber`, `pypdf/PyPDF2` e OCR quando dependencias existirem;
* economia de tokens: ler primeiro o relatorio, nao o Markdown inteiro.

Dependencias instaladas no `.venv`:

* `pymupdf`;
* `pdfplumber`;
* `pypdf`;
* `pytesseract`;
* `pdf2image`;
* `Pillow`.

### 3. Conversao Do Guia UNICEF

O PDF do Guia UNICEF foi convertido para:

* `parte2/guia_unicef.md`;
* `parte2/guia_unicef.conversion_report.json`.

Resultado da validacao:

* `passed: true`;
* `score: 100`;
* metodo: `pdfmd`;
* aproximadamente 15.033 palavras;
* 109 headings;
* 0 caracteres de substituicao.

### 4. Estrutura `parte2/`

Foi criada/validada a estrutura:

```text
parte2/
|-- README.md
|-- guia_unicef.md
|-- guia_unicef.conversion_report.json
|-- knowledge_bundle/
|-- manuals/
|-- prompts/
|-- workflow/
|-- municipios_base/
|-- resultados/
```

### 5. Knowledge Bundle Inicial

Foi criado o `Knowledge Bundle` em `parte2/knowledge_bundle/`.

Arquivos principais:

* `parte2/knowledge_bundle/index.md`;
* `parte2/knowledge_bundle/log.md`;
* `parte2/knowledge_bundle/metodologia/*.md`;
* `parte2/knowledge_bundle/areas/*.md`.

Conceitos metodologicos criados:

* unidade de inferencia;
* criterios de inclusao;
* criterios de exclusao;
* despesas-meio;
* gasto especifico ou ampliado;
* ponderadores;
* planilha de classificacao.

Areas tematicas criadas:

* Educacao Infantil;
* Saude Materno-infantil;
* Assistencia Social;
* Protecao dos Direitos da Crianca e da Familia;
* Direito a Cidade e Habitacao;
* Saneamento e Agua;
* Cultura e Direito de Brincar;
* Seguranca Alimentar;
* Enfrentamento da Pobreza.

Foi executada validacao OKF basica:

```text
checked=16 errors=0
```

### 6. Manuais, Prompts E Workflow

Foram criados:

* `parte2/manuals/operating_manual_humano.md`;
* `parte2/manuals/operating_manual_llm.md`;
* `parte2/prompts/classificador.md`;
* `parte2/prompts/avaliacao.md`;
* `parte2/prompts/revisao.md`;
* `parte2/workflow/workflow.md`;
* `parte2/README.md`.

Depois, `operating_manual_humano.md` e `parte2/README.md` foram atualizados para explicar a natureza cientifica do experimento e o papel dos prompts.

Papel dos artefatos:

* `knowledge_bundle/`: conhecimento normativo estruturado;
* `fonte_parte_2.xlsx`: exemplos humanos e linhas-alvo;
* `prompts/`: protocolo experimental de uso da LLM.

### 7. Complemento Metodologico

`PARTE2_COMPLEMENTO.md` foi reescrito para alinhar a metodologia ao projeto atual.

Pontos consolidados:

* `parte2/knowledge_bundle/` e a base normativa/metodologica macro;
* `fonte_parte_2.xlsx` e o arquivo operacional definitivo;
* aba `municipios_classificados` contem exemplos humanos;
* aba `classificacao_automatizada` contem linhas a classificar pela IA;
* `Indicador` fica fora do escopo desta etapa;
* a avaliacao deve comparar apenas `Area Tematica` e `Gasto E ou NE`;
* deve haver normalizacao de rotulos antes da avaliacao.

### 8. Inspecao Do Excel Definitivo

Foi inspecionado `fonte_parte_2.xlsx`.

Abas encontradas:

* `municipios_classificados`;
* `classificacao_automatizada`.

Dimensoes:

* `municipios_classificados`: 2.956 linhas de dados, 19 colunas;
* `classificacao_automatizada`: 7.010 linhas de dados, 18 colunas.

Municipios-base confirmados:

* Alianca do Tocantins;
* Crixas do Tocantins;
* Sao Valerio da Natividade;
* Peixe;
* Sandolandia.

Municipios de teste confirmados:

* Alvorada;
* Cariri do Tocantins;
* Formoso do Araguaia;
* Gurupi;
* Oliveira de Fatima;
* Sucupira;
* Parana;
* Figueiropolis;
* Araguacu;
* Santa Rita do Tocantins.

Colunas importantes:

* `nomePrograma`;
* `nomeFuncao`;
* `nomeSubFuncao`;
* `nomeAcaoOrcamentaria`;
* `Area Tematica` aparece no console como `�rea Tem�tica` por problema de exibicao;
* `Gasto E ou NE`;
* `Indicador`.

Problemas observados nos rotulos humanos:

* variacoes de caixa em `Nao especifico` / `Nao Especifico`;
* erros de digitacao como `Assitencia Social`;
* erros como `Sanemaneto e agua`;
* valores vazios, tracos e `nao se aplica`;
* possiveis problemas de acentuacao na exibicao do console.

Isso exige normalizacao antes da avaliacao de concordancia.

### 9. Trabalho Futuro Sobre Obsidian

Foi criado:

* `trabalho_futuro.md`.

Conteudo:

* recomendacao de nao colocar o vault do Obsidian dentro de `knowledge_bundle/`;
* proposta de `vault_gspi/` como segundo cerebro;
* separacao entre vault, bundle operacional e entrega ao cliente;
* possibilidade de conversar com o bundle via LLM/RAG.

### 10. Ajuste Dos Artefatos Operacionais Ao Fluxo Real

Com autorizacao do usuario, foram revisados os artefatos operacionais para refletir o complemento metodologico e o uso do arquivo `fonte_parte_2.xlsx`.

Arquivos atualizados:

* `parte2/manuals/operating_manual_llm.md`;
* `parte2/prompts/classificador.md`;
* `parte2/prompts/avaliacao.md`;
* `parte2/prompts/revisao.md`;
* `parte2/workflow/workflow.md`;
* `parte2/knowledge_bundle/metodologia/planilha-classificacao.md`.

Ajustes consolidados:

* `fonte_parte_2.xlsx` foi declarado como arquivo operacional definitivo;
* `municipios_classificados` foi declarado como aba de exemplos humanos;
* `classificacao_automatizada` foi declarada como aba-alvo;
* a execucao foi orientada para fluxo em lote;
* `Indicador` foi mantido fora do escopo da etapa atual;
* `Area Tematica` e `Gasto E ou NE` foram mantidas como unicas colunas de classificacao;
* subarea tematica, ponderadores e valores ponderados foram removidos como saidas desta etapa;
* foi reforcada a precedencia do Knowledge Bundle sobre exemplos humanos;
* foi prevista normalizacao de rotulos antes da avaliacao;
* confianca, justificativa, duvidas e divergencias devem ser registradas em log ou arquivo derivado, sem alterar desnecessariamente a planilha original.

### 11. Preparacao Da Execucao Em Lote E Lote Piloto

Com autorizacao do usuario, foi executada a proxima fase operacional usando `operating-manual_fable.md` como referencia de modo de trabalho.

Apos orientacao do usuario, ficou definido que as proximas leituras, analises e edicoes de Excel devem seguir a skill local:

* `skills/xlsx/SKILL.md`.

A skill recomenda:

* `pandas` para analise de dados e operacoes tabulares;
* `openpyxl` para preservar e editar workbooks existentes;
* recalculo por LibreOffice apenas quando houver formulas a recalcular.

Como a fase atual nao cria formulas, nao houve necessidade de recalculo.

Foi criada a copia de trabalho:

* `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

Foram criados artefatos derivados de preparacao:

* `parte2/workflow/preparar_execucao_lote.py`;
* `parte2/workflow/consultar_exemplos_humanos.py`;
* `parte2/workflow/aplicar_lote_piloto.py`;
* `parte2/resultados/preparacao_execucao_resumo.json`;
* `parte2/resultados/exemplos_humanos_representativos.csv`;
* `parte2/resultados/lote_piloto_001.csv`;
* `parte2/resultados/log_classificacao_template.csv`;
* `parte2/resultados/normalizacao_labels_inicial.json`.

O script de preparacao confirmou:

* `municipios_classificados`: 2.956 linhas de dados;
* `classificacao_automatizada`: 7.010 linhas de dados;
* campos essenciais presentes:
  * `nomePrograma`;
  * `nomeFuncao`;
  * `nomeSubFuncao`;
  * `nomeAcaoOrcamentaria`;
* campo de area tematica detectado no Excel como `Area Tematica` com problema de exibicao/encoding no console;
* lote piloto recomendado com 20 linhas.

Foi executado o lote piloto:

* arquivo de entrada: `parte2/resultados/lote_piloto_001.csv`;
* arquivo classificado: `parte2/resultados/lote_piloto_001_classificado.csv`;
* relatorio: `parte2/resultados/relatorio_lote_piloto_001.md`.

O lote piloto classificou as 20 primeiras linhas da aba `classificacao_automatizada`, todas do municipio de Alvorada.

As classificacoes foram aplicadas apenas na copia de trabalho `parte2/resultados/fonte_parte_2_trabalho.xlsx`.

A planilha original `fonte_parte_2.xlsx` nao foi alterada.

A coluna `Indicador` permaneceu sem preenchimento nas linhas do lote piloto.

Resultado quantitativo do lote piloto:

```text
linhas classificadas: 20
Alta confianca: 16
Media confianca: 3
Baixa confianca: 1
linhas para revisao humana: 4
```

Distribuicao por `Area Tematica`:

```text
nao se aplica: 7
Saude Materno-infantil: 6
Assistencia Social: 5
Educacao Infantil: 1
Protecao dos Direitos da Crianca e da Familia: 1
```

Distribuicao por `Gasto E ou NE`:

```text
-: 7
Nao Especifico: 12
Especifico: 1
```

Linhas marcadas para revisao antes de ampliar a classificacao:

* linha Excel 5: `MANUTENCAO DO FUNDO MUNICIPAL DE EDUCACAO - FME`;
* linha Excel 9: `GESTAO DA SECRETARIA MUNICIPAL DE POLITICAS PARA MULHERES`;
* linha Excel 14: `MANUTENCAO DO FUNDO MUNICIPAL DE SAUDE (FMS)`;
* linha Excel 16: `GESTAO DA SECRETARIA MUNICIPAL DE CULTURA`.

## Estado Atual

O projeto esta com:

* PDF convertido;
* bundle inicial criado e validado;
* manuais, prompts e workflow alinhados ao fluxo real de `fonte_parte_2.xlsx`;
* complemento metodologico alinhado;
* arquivo Excel definitivo identificado e inspecionado;
* escopo da classificacao definido para `Area Tematica` e `Gasto E ou NE`;
* `Indicador`, subarea tematica e ponderadores fora do escopo da etapa atual;
* copia de trabalho criada em `parte2/resultados/fonte_parte_2_trabalho.xlsx`;
* exemplos humanos representativos extraidos;
* lote piloto de 20 linhas executado e aplicado apenas na copia de trabalho;
* relatorio do lote piloto criado;
* necessidade de revisar 4 linhas do lote piloto antes de expandir a classificacao.

## Proximo Passo Recomendado

Revisar qualitativamente as 4 linhas marcadas no lote piloto antes de expandir a classificacao para os proximos lotes.

Etapa recomendada agora:

1. abrir `parte2/resultados/relatorio_lote_piloto_001.md`;
2. revisar as linhas Excel 5, 9, 14 e 16;
3. decidir se os criterios usados para despesas-meio de educacao, politicas para mulheres, gestao geral de saude e gestao geral de cultura devem ser mantidos;
4. se necessario, ajustar prompts/workflow ou registrar regra operacional complementar;
5. atualizar `fase_projeto.md`;
6. somente depois, executar o proximo lote.

## Passo Depois Disso

Depois da revisao do lote piloto, executar a classificacao em lotes sucessivos.

Sugestao de abordagem:

1. usar tamanho de lote inicial de 20 linhas;
2. classificar a aba `classificacao_automatizada` em lotes sucessivos;
3. preencher apenas `Area Tematica` e `Gasto E ou NE` na copia de trabalho;
4. manter `Indicador` sem classificacao nesta etapa;
5. gerar log de confianca/justificativa separado;
6. revisar linhas de baixa confianca ou marcadas para revisao humana;
7. avaliar concordancia quando houver referencia humana para os municipios de teste;
8. produzir relatorio de divergencias;
9. atualizar `fase_projeto.md` ao fim de cada etapa operacional.

## Observacao Para Nova Conversa

Ao retomar em nova conversa:

1. ler este arquivo primeiro;
2. respeitar a exigencia de permissao passo a passo;
3. nao assumir que `final_geral_trabalho_.xlsx` e o arquivo definitivo;
4. usar `fonte_parte_2.xlsx`;
5. nao classificar `Indicador` nesta etapa;
6. manter o `Knowledge Bundle` como regra macro e o Excel como campo empirico;
7. antes de editar ou executar novo passo operacional, propor o passo ao usuario e aguardar autorizacao;
8. atualizar este arquivo sempre que uma etapa for concluida ou uma decisao metodologica for tomada.
