# Complemento da Documentacao - Municipios, Metodologia e Validacao

Este documento complementa a metodologia descrita em `PARTE2.md`.

Ele esclarece como o `Knowledge Bundle` e o arquivo Excel definitivo devem ser usados na execucao da classificacao assistida por LLM.

## 1. Papel Do Knowledge Bundle

O diretorio `parte2/knowledge_bundle/` contem a base normativa e operacional estruturada a partir do Guia UNICEF/GSPI-M.

Ele deve ser usado pela LLM para entender a metodologia macro de classificacao, incluindo:

* criterios de inclusao e exclusao;
* areas tematicas;
* subareas;
* regra de gasto especifico ou ampliado;
* restricoes sobre despesas-meio;
* precedencia do Guia sobre exemplos humanos.

O `Knowledge Bundle` nao e a planilha de entrada da classificacao. Ele e a fonte de conhecimento estruturado que orienta a interpretacao das linhas orcamentarias.

## 2. Arquivo Operacional Definitivo

O arquivo operacional definitivo da Parte 2 e:

```text
fonte_parte_2.xlsx
```

Esse arquivo contem tanto os exemplos humanos quanto as linhas que deverao ser classificadas pela IA.

Ele possui duas abas principais:

```text
municipios_classificados
classificacao_automatizada
```

## 3. Municipios-Base

Os municipios-base sao aqueles que ja possuem classificacao humana previamente realizada.

Eles estao reunidos na aba:

```text
municipios_classificados
```

Os municipios-base sao:

* Alianca do Tocantins;
* Crixas do Tocantins;
* Sao Valerio da Natividade;
* Peixe;
* Sandolandia.

Esses municipios devem ser usados como exemplos reais de aplicacao humana do Guia UNICEF/GSPI-M, ja consumido e organizado no `Knowledge Bundle`.

A LLM deve observar como foram classificadas principalmente as colunas:

* Area Tematica;
* Gasto E ou NE.

A coluna `Indicador` nao deve ser usada como alvo de classificacao nesta etapa, pois sua definicao depende de etapa posterior de ponderacao.

## 4. Municipios De Teste

Os municipios de teste estao reunidos na aba:

```text
classificacao_automatizada
```

Esses municipios deverao ser classificados pela LLM a partir da combinacao entre:

* metodologia macro do `Knowledge Bundle`;
* exemplos humanos da aba `municipios_classificados`;
* hierarquia orcamentaria da propria linha.

Os municipios de teste sao:

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

## 5. Relacao Entre Bundle E Excel

A arquitetura correta da classificacao e:

```text
Guia UNICEF
        |
        v
parte2/knowledge_bundle/
        |
        v
LLM entende a metodologia macro de classificacao

fonte_parte_2.xlsx
        |
        |-- municipios_classificados = exemplos humanos
        |
        |-- classificacao_automatizada = linhas a classificar pela IA
```

O `Knowledge Bundle` fornece a regra.

A aba `municipios_classificados` fornece exemplos praticos de aplicacao humana.

A aba `classificacao_automatizada` fornece as linhas que serao classificadas pela IA.

Em caso de conflito entre o `Knowledge Bundle` e os exemplos humanos, deve prevalecer o `Knowledge Bundle`, pois ele deriva do Guia UNICEF/GSPI-M.

## 6. Unidade De Inferencia

A classificacao nao deve ser realizada com base apenas na descricao da acao orcamentaria.

Cada linha deve ser interpretada como uma unidade composta pela hierarquia:

```text
Programa
Funcao
Subfuncao
Acao Orcamentaria
```

No arquivo `fonte_parte_2.xlsx`, esses elementos aparecem principalmente nas colunas:

* `nomePrograma`;
* `nomeFuncao`;
* `nomeSubFuncao`;
* `nomeAcaoOrcamentaria`.

A LLM deve analisar a combinacao desses quatro elementos para inferir:

1. a politica publica envolvida;
2. a finalidade da despesa;
3. o publico beneficiario;
4. a classificacao correspondente.

## 7. Saidas Esperadas Nesta Etapa

Para cada linha da aba `classificacao_automatizada`, a LLM devera preencher apenas:

* `Area Tematica`;
* `Gasto E ou NE`.

A coluna `Indicador` nao devera ser preenchida nesta etapa.

Caso seja necessario registrar algo nessa coluna por exigencia operacional, usar:

```text
Nao classificado nesta etapa
```

## 8. Principios De Classificacao

### 8.1. Prioridade Do Knowledge Bundle

O `Knowledge Bundle`, derivado do Guia UNICEF/GSPI-M, e a fonte normativa principal.

Os exemplos humanos nao substituem o Guia.

### 8.2. Uso Dos Municipios-Base

Os municipios-base devem ser usados como exemplos de aplicacao pratica do Guia.

A LLM deve aprender padroes de interpretacao, nao simplesmente copiar classificacoes por similaridade textual.

### 8.3. Analise Hierarquica Obrigatoria

Nenhuma linha deve ser classificada com base em uma unica palavra ou apenas no nome da acao orcamentaria.

A classificacao deve considerar conjuntamente:

* Programa;
* Funcao;
* Subfuncao;
* Acao Orcamentaria.

### 8.4. Interpretacao Semantica

A LLM deve identificar a finalidade da despesa, a politica publica envolvida e o publico beneficiario sempre que essas informacoes puderem ser inferidas da hierarquia orcamentaria.

### 8.5. Generalizacao

A LLM deve reconhecer casos semanticamente equivalentes, ainda que escritos com palavras diferentes.

Exemplo:

```text
Construcao de UBS
Ampliacao de Unidade Basica de Saude
Reforma de posto de saude
```

Essas expressoes nao devem ser tratadas apenas como textos diferentes. A LLM deve avaliar se possuem finalidade orcamentaria equivalente.

### 8.6. Registro De Incerteza

Quando houver ambiguidade relevante, a LLM devera sinalizar a linha como caso de baixa confianca para revisao humana.

## 9. Procedimento Metodologico Revisado

A metodologia deve ser executada nesta ordem:

1. Extrair o Guia UNICEF em PDF para Markdown usando a skill `pdf-to-md`.
2. Converter o conteudo relevante do Guia em `Knowledge Bundle` estruturado em OKF.
3. Validar se o bundle contem conceitos, regras, excecoes e categorias necessarias.
4. Abrir o arquivo `fonte_parte_2.xlsx`.
5. Carregar a aba `municipios_classificados` como exemplos humanos.
6. Carregar a aba `classificacao_automatizada` como conjunto-alvo.
7. Apresentar a LLM o `Knowledge Bundle` e exemplos humanos suficientes.
8. Solicitar que a LLM classifique as linhas da aba `classificacao_automatizada`.
9. Preencher apenas as colunas `Area Tematica` e `Gasto E ou NE`.
10. Manter `Indicador` em branco ou como `Nao classificado nesta etapa`.
11. Comparar a classificacao da LLM com classificacao humana de referencia, quando disponivel.
12. Calcular taxa de concordancia.
13. Analisar erros e ambiguidades.
14. Se necessario, executar segunda rodada apos revisao do protocolo.

## 10. Metrica De Validacao

A validacao deve medir a concordancia entre a classificacao da LLM e a classificacao humana.

A comparacao deve ser feita por linha e por coluna.

As colunas avaliadas nesta etapa sao:

* `Area Tematica`;
* `Gasto E ou NE`.

A coluna `Indicador` nao entra na metrica desta etapa.

Acuracia:

```text
Acuracia = numero de classificacoes coincidentes / numero total de classificacoes avaliadas
```

A comparacao deve ocorrer em tres niveis:

1. acuracia da `Area Tematica`;
2. acuracia do `Gasto E ou NE`;
3. acuracia conjunta da linha, quando as duas colunas coincidem simultaneamente.

O objetivo metodologico e alcancar concordancia superior a 90% em relacao a classificacao humana.

## 11. Normalizacao Antes Da Avaliacao

Antes de calcular concordancia, os rotulos devem ser normalizados.

Isso e necessario porque os exemplos humanos podem conter variacoes de escrita, acentuacao, caixa, espacos, erros de digitacao ou marcadores como branco e `-`.

Exemplos de normalizacao necessaria:

* `Nao especifico`, `Nao Especifico` e variacoes devem ser tratados como o mesmo rotulo;
* grafias com erro de digitacao devem ser mapeadas para o rotulo canonico;
* valores vazios, tracos e `nao se aplica` devem ser tratados de forma consistente.

A normalizacao nao deve alterar a planilha original sem registro. Ela deve ser aplicada na etapa de avaliacao ou em arquivo derivado.

## 12. Analise De Divergencias

As divergencias entre a LLM e o humano devem ser analisadas qualitativamente.

Cada divergencia pode ser classificada em uma das seguintes categorias:

* erro de interpretacao do Guia;
* erro de generalizacao;
* ambiguidade da descricao orcamentaria;
* insuficiencia de contexto na linha;
* inconsistencia nos exemplos humanos;
* possivel erro humano na classificacao de referencia;
* conflito entre regra geral e caso concreto.

Nem toda divergencia representa necessariamente erro da LLM. Algumas divergencias podem revelar ambiguidade da classificacao humana ou insuficiencia de informacao na linha orcamentaria.

## 13. Riscos Metodologicos

### 13.1. Confundir Treinamento Com Aprendizado Em Contexto

A LLM nao sera treinada no sentido tecnico de ajuste de pesos.

Ela utilizara o `Knowledge Bundle` e os exemplos humanos como contexto para inferencia.

Os termos mais adequados sao:

```text
aprendizado em contexto
```

ou

```text
inferencia orientada por conhecimento estruturado
```

### 13.2. Supervalorizar Os Exemplos

Os cinco municipios-base nao substituem o Guia.

Eles demonstram aplicacao pratica, mas a classificacao deve sempre ser fundamentada prioritariamente no `Knowledge Bundle`.

### 13.3. Classificar Por Similaridade Textual

O classificador nao deve apenas buscar palavras iguais ou parecidas.

Ele deve interpretar a finalidade da despesa dentro da hierarquia orcamentaria.

Esse ponto deve ser reforcado nos prompts e nos manuais.

## 14. Estrutura Do Projeto

Este complemento nao altera a estrutura de pastas nem os nomes ja definidos no projeto.

A estrutura operacional permanece:

```text
parte2/
|
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

O arquivo `fonte_parte_2.xlsx` fica na raiz do projeto e e o arquivo operacional definitivo para exemplos e classificacao.

## 15. Entregaveis Finais Desta Etapa

Ao final da Parte 2, deverao existir:

1. Guia UNICEF extraido em Markdown;
2. `Knowledge Bundle` estruturado em OKF;
3. arquivo `fonte_parte_2.xlsx` com municipios-base e linhas-alvo;
4. manual de uso do classificador;
5. manual operacional da LLM;
6. prompts de classificacao, avaliacao e revisao;
7. classificacao produzida pela LLM para a aba `classificacao_automatizada`;
8. comparacao com classificacao humana, quando disponivel;
9. relatorio de divergencias;
10. conclusao sobre a viabilidade do metodo.

## 16. Formulacao Metodologica Recomendada

O projeto adota um protocolo de classificacao baseado em LLM, no qual o modelo recebe um `Knowledge Bundle` estruturado a partir do Guia UNICEF/GSPI-M e um conjunto de exemplos humanos previamente classificados na aba `municipios_classificados` do arquivo `fonte_parte_2.xlsx`.

A partir desses insumos, a LLM classifica novas acoes orcamentarias da aba `classificacao_automatizada`, considerando a hierarquia formada por Programa, Funcao, Subfuncao e Acao Orcamentaria.

Os municipios-base sao usados como exemplos de aplicacao pratica do Guia, permitindo que a LLM observe padroes humanos de interpretacao. Os municipios de teste funcionam como campo de validacao do metodo.

Nesta etapa, a LLM preenche apenas `Area Tematica` e `Gasto E ou NE`. A coluna `Indicador` permanece fora do escopo, pois depende de etapa posterior de ponderacao.

A validacao do metodo e realizada por meio da comparacao entre a classificacao produzida pela LLM e a classificacao humana de referencia, buscando concordancia superior a 90%. As divergencias sao analisadas qualitativamente para identificar erros de interpretacao, ambiguidades, inconsistencias dos dados ou limitacoes do protocolo.

## 17. Conclusao Metodologica

A metodologia revisada separa claramente:

* conhecimento normativo estruturado no `Knowledge Bundle`;
* exemplos humanos no arquivo `fonte_parte_2.xlsx`;
* inferencia da LLM;
* classificacao automatizada;
* validacao humana;
* analise de divergencias.

Essa separacao torna o classificador mais replicavel, auditavel e adequado para uso cientifico.

O ponto central e que a LLM nao deve repetir classificacoes ja vistas. Ela deve aplicar um protocolo de interpretacao baseado no Guia, usando os municipios-base como exemplos de raciocinio humano e os municipios de teste como validacao.
