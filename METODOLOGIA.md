# Metodologia Do Projeto Infancia Fiscal - Documento Do Pesquisador

Este documento foi escrito para o pesquisador responsavel pelo projeto, que e contador e nao precisa entender de programacao.

Ele tem tres funcoes:

1. Explicar, em linguagem simples, o que foi feito no projeto e como foi feito.
2. Servir de roteiro quando o pesquisador precisar apresentar ou defender o trabalho.
3. Reservar espacos marcados com `[PREENCHER]` para o pesquisador registrar suas proprias decisoes, justificativas e observacoes.

Tudo o que esta escrito aqui pode ser conferido nos arquivos citados ao longo do texto. Nenhum numero foi inventado: todos vem dos relatorios gerados durante a execucao.

---

## 1. Resumo Em Um Paragrafo

> O projeto testou se uma inteligencia artificial (IA) consegue classificar despesas orcamentarias municipais segundo a metodologia GSPI-M (Gasto Social com a Primeira Infancia), do Guia UNICEF. A IA recebeu duas fontes de informacao: a regra (o Guia, organizado em arquivos de consulta) e exemplos praticos (2.956 despesas de 5 municipios ja classificadas por humanos). Com isso, ela classificou 7.010 despesas de 10 municipios de teste, indicando para cada uma a Area Tematica e o Tipo de Gasto. O trabalho comecou com lotes pequenos de 20 linhas, revisados por humano; apos a aprovacao dos padroes, o restante foi classificado automaticamente, com registro de auditoria linha a linha. A planilha original foi preservada e 558 linhas ficaram marcadas para revisao humana posterior.

Se o pesquisador so puder falar uma frase, pode ser esta:

> "Ensinamos a IA a aplicar o Guia UNICEF do jeito que um tecnico aplicaria: primeiro ela le a regra, depois observa exemplos reais classificados por humanos, e so entao classifica os casos novos - e tudo o que ela faz fica registrado para conferencia."

---

## 2. Contexto E Problema De Pesquisa

### 2.1 O Que E O GSPI-M

O GSPI-M e a metodologia do Guia UNICEF para apurar quanto um municipio gasta com a primeira infancia (criancas de 0 a 6 anos). Para isso, cada acao orcamentaria do municipio precisa ser classificada em:

* **Area Tematica**: qual politica publica a despesa atende (ex.: Educacao Infantil, Saude Materno-infantil, Assistencia Social) ou `nao se aplica`;
* **Tipo de Gasto** (coluna `Gasto E ou NE`): se o gasto e `Especifico` para a primeira infancia ou `Nao Especifico` (beneficia a primeira infancia junto com outros publicos). Quando a area e `nao se aplica`, usa-se `-`.

### 2.2 O Problema

Classificar despesa por despesa e um trabalho manual, demorado e que exige conhecimento tecnico do Guia. Um unico municipio pequeno pode ter centenas de acoes orcamentarias. Classificar dezenas de municipios a mao e inviavel em prazo razoavel.

### 2.3 A Pergunta De Pesquisa

> Uma IA, recebendo a metodologia do Guia UNICEF e exemplos de classificacao humana, consegue reproduzir a classificacao que um especialista humano faria?

`[PREENCHER: se o pesquisador tiver uma formulacao propria da pergunta de pesquisa, ou vinculo com dissertacao/artigo, registrar aqui.]`

---

## 3. Materiais Utilizados

### 3.1 A Regra: Guia UNICEF Transformado Em Base De Consulta

O Guia em PDF foi convertido para arquivos de texto organizados por tema, chamados no projeto de **Knowledge Bundle** (traduzindo: "pacote de conhecimento"). Ele fica na pasta `parte2/knowledge_bundle/` e contem:

* os criterios de inclusao e exclusao de despesas;
* a regra de gasto especifico ou ampliado;
* o tratamento de despesas-meio (despesas administrativas, de manutencao etc.);
* uma ficha para cada uma das nove areas tematicas.

**Analogia para explicar**: e como transformar o Guia em um manual de bolso organizado por assunto, para que a IA consulte sempre a mesma fonte normativa, em vez de "lembrar de cabeca".

Importante: o Knowledge Bundle contem apenas a regra do Guia. Ele nao se mistura com os exemplos praticos.

### 3.2 Os Exemplos: Municipios-Base

O arquivo `fonte_parte_2.xlsx` tem uma aba chamada `municipios_classificados`, com **2.956 despesas ja classificadas por humanos** em 5 municipios do Tocantins:

* Alianca do Tocantins;
* Crixas do Tocantins;
* Sao Valerio da Natividade;
* Peixe;
* Sandolandia.

**Analogia para explicar**: os municipios-base funcionam como a "jurisprudencia" do projeto. A regra esta no Guia; os exemplos mostram como um tecnico humano aplicou a regra em casos reais.

`[PREENCHER: quem fez a classificacao humana dos municipios-base, quando, e com base em que edicao do Guia.]`

### 3.3 O Alvo: Municipios De Teste

A aba `classificacao_automatizada` do mesmo arquivo tem **7.010 despesas ainda nao classificadas**, de 10 municipios de teste:

Alvorada, Cariri do Tocantins, Formoso do Araguaia, Gurupi, Oliveira de Fatima, Sucupira, Parana, Figueiropolis, Araguacu e Santa Rita do Tocantins.

Essas 7.010 linhas foram o objeto da classificacao pela IA.

---

## 4. Como A IA Classifica (Explicacao Sem Termos Tecnicos)

### 4.1 A IA Nao Foi "Treinada"

Este ponto e importante para nao dar explicacao errada em apresentacao.

A IA usada **nao passou por treinamento** no sentido tecnico (ninguem ajustou o "cerebro" do modelo). O que o projeto fez foi dar contexto para a IA no momento da classificacao: a regra (Knowledge Bundle) + os exemplos humanos. O nome tecnico disso e **aprendizado em contexto** (in-context learning).

**Analogia para explicar**: e como entregar a um estagiario inteligente o manual da empresa e uma pasta de casos ja resolvidos, e pedir que ele resolva os casos novos seguindo o manual. O estagiario nao "estudou por anos" - ele consulta o material que recebeu.

### 4.2 O Que A IA Olha Em Cada Linha

A IA nunca decide olhando so o nome da despesa. Para cada linha, ela analisa em conjunto quatro campos da planilha:

```text
nomePrograma          (o programa de governo)
nomeFuncao            (a funcao orcamentaria, ex.: Saude, Educacao)
nomeSubFuncao         (o detalhamento da funcao)
nomeAcaoOrcamentaria  (a acao especifica)
```

Com esses quatro campos ela infere: qual politica publica esta envolvida, qual a finalidade da despesa e quem e o publico beneficiado. So entao preenche `Area Tematica` e `Gasto E ou NE`.

### 4.3 Regra De Precedencia

Quando o exemplo humano e a regra do Guia apontam para direcoes diferentes, **a regra do Guia prevalece**. Os exemplos ilustram, mas nao substituem a norma.

### 4.4 O Que Ficou Fora Do Escopo

A coluna `Indicador` **nao foi preenchida** nesta etapa, porque depende de uma fase posterior da metodologia (ponderacao). Isso foi uma decisao deliberada, nao um esquecimento. O mesmo vale para subareas tematicas e ponderadores.

---

## 5. Etapas Do Trabalho (O Que Foi Feito, Na Ordem)

### Etapa 1 - Preparacao (regra + exemplos + planilha)

1. O Guia UNICEF em PDF foi convertido para texto e validado (conversao com nota maxima, sem perda de conteudo relevante).
2. O Knowledge Bundle foi montado a partir do Guia.
3. O arquivo `fonte_parte_2.xlsx` foi inspecionado e confirmado como fonte oficial.
4. Foi criada uma **copia de trabalho** (`parte2/resultados/fonte_parte_2_trabalho.xlsx`). Todo o preenchimento aconteceu na copia. **O arquivo original nunca foi alterado.**

### Etapa 2 - Lotes De Calibracao Com Revisao Humana

Antes de classificar tudo, o metodo foi testado em lotes pequenos de 20 linhas, todos do municipio de Alvorada:

| Lote | Linhas | Resultado da revisao humana |
| --- | --- | --- |
| Piloto 001 | 20 | 4 linhas conferidas; padrao aprovado |
| 002 | 20 | Aprovado integralmente |
| 003 | 20 | Aprovado integralmente |
| 004 | 20 | Aprovado integralmente |
| 005 | 20 | Aprovado integralmente |
| 006 | 20 | Aprovado integralmente |

Total: **120 linhas classificadas e validadas por humano**, com relatorio individual por lote na pasta `parte2/resultados/` (arquivos `relatorio_lote_*.md`).

Em cada lote, a IA marcava sozinha as linhas em que tinha menos certeza (ex.: "Manutencao do Fundo Municipal de Educacao", que nao diz se inclui educacao infantil). Essas linhas eram apresentadas ao revisor humano antes de continuar.

**Analogia para explicar**: e o mesmo principio de uma auditoria - primeiro se testa o procedimento em uma amostra pequena; so depois de aprovado o procedimento, ele e aplicado ao restante.

`[PREENCHER: quem foi o revisor humano dos lotes e qual criterio usou para aprovar. Registrar tambem exemplos de linhas que gerou duvida e como decidiu.]`

### Etapa 3 - Classificacao Automatica Supervisionada

Com o padrao aprovado nos 6 lotes, o revisor autorizou a classificacao do restante:

* **6.890 linhas** classificadas automaticamente com os mesmos criterios;
* total geral da aba: **7.010 linhas, todas classificadas**;
* `Indicador`: **0 preenchimentos** (confirmado por verificacao automatica);
* cada linha recebeu um **grau de confianca** (Alta, Media ou Baixa) e uma justificativa, gravados em um arquivo de auditoria separado.

### Etapa 4 - Trilha De Auditoria

Ficaram registrados, na pasta `parte2/resultados/`:

* `fonte_parte_2_trabalho.xlsx` - a planilha classificada (resultado principal);
* `classificacao_automatica_supervisionada_log.csv` (e versao em Excel) - o registro linha a linha: classificacao, confianca, justificativa e se requer revisao humana;
* `classificacao_automatica_supervisionada_resumo.json` - resumo tecnico da execucao;
* `relatorio_classificacao_automatica_supervisionada.md` - relatorio geral em texto.

**Analogia para explicar**: o log e o equivalente ao papel de trabalho do auditor - para cada lancamento, esta registrado o que foi decidido, com que grau de seguranca e por que.

---

## 6. Resultados Obtidos Ate Agora

### 6.1 Visao Geral

```text
Total de despesas classificadas:            7.010 (100% da aba alvo)
Classificadas em lotes com revisao humana:    120
Classificadas em modo automatico:           6.890
Coluna Indicador preenchida:                    0 (fora do escopo, como planejado)
Linhas marcadas para revisao humana:          558
```

### 6.2 Distribuicao Por Area Tematica (6.890 linhas automaticas)

```text
nao se aplica:                                  3.471
Saude Materno-infantil:                         1.724
Assistencia Social:                             1.010
Educacao Infantil:                                509
Saneamento e Agua:                                114
Protecao dos Direitos da Crianca e da Familia:     60
Seguranca Alimentar:                                2
```

Leitura simples: cerca de metade das despesas municipais nao tem relacao com primeira infancia (legislativo, administracao geral, iluminacao publica etc.). Entre as que tem relacao, predominam saude, assistencia social e educacao infantil - o que e coerente com o desenho das politicas municipais.

### 6.3 Distribuicao Por Tipo De Gasto

```text
-               : 3.471  (acompanha o "nao se aplica")
Nao Especifico  : 2.958  (beneficia a primeira infancia junto com outros publicos)
Especifico      :   461  (voltado diretamente a primeira infancia)
```

### 6.4 Grau De Confianca Da IA

```text
Alta:  6.332 linhas (92% do lote automatico)
Media:   558 linhas (8%) - marcadas para revisao humana
Baixa:     0 linhas
```

As 558 linhas de confianca media **foram classificadas**, mas ficaram sinalizadas no log para conferencia humana. Os casos tipicos sao:

* despesas-meio de educacao sem mencao a etapa infantil (ex.: fundo municipal de educacao);
* transporte e alimentacao escolar sem etapa explicitada;
* politicas para mulheres;
* conselho tutelar e protecao ampla de criancas e adolescentes;
* saneamento e residuos quando aparecem na funcao ambiental;
* acoes de renda e seguranca alimentar com publico amplo.

---

## 7. Controles De Qualidade E Salvaguardas

Estes pontos sao importantes em qualquer arguicao sobre confiabilidade:

1. **Original preservado**: `fonte_parte_2.xlsx` nunca foi alterado; todo o trabalho ocorreu em copia.
2. **Escopo travado**: a IA so podia preencher duas colunas; `Indicador` ficou intocado e isso e verificavel.
3. **Calibracao antes da escala**: nada foi classificado em massa antes de 6 lotes aprovados por humano.
4. **Incerteza declarada**: a IA foi instruida a marcar as proprias duvidas, em vez de esconde-las.
5. **Auditoria linha a linha**: toda classificacao tem justificativa registrada em log.
6. **Separacao regra x exemplo**: a base normativa (Guia) nao se mistura com os exemplos humanos nem com padroes aprendidos na pratica; novas regras so entram apos validacao humana.

---

## 8. O Que Ainda Nao Foi Feito (Limitacoes Atuais)

E fundamental o pesquisador ser transparente sobre isto:

1. **A taxa de acerto ainda nao foi medida formalmente.** A metodologia preve comparar a classificacao da IA com classificacao humana e calcular a concordancia (meta: acima de 90%). Ate agora a validacao foi qualitativa (revisao dos lotes iniciais e aprovacao dos padroes). A medicao numerica e o proximo passo.
2. **As 558 linhas marcadas para revisao ainda nao foram revisadas.**
3. **Nao houve ainda amostragem das linhas de alta confianca** para confirmar que a confianca alta corresponde de fato a acerto.
4. **Todos os municipios sao do Tocantins.** A generalizacao para municipios de outros estados (outras nomenclaturas orcamentarias) ainda nao foi testada.

`[PREENCHER: conforme as validacoes forem feitas, registrar aqui os numeros de concordancia e as correcoes aplicadas.]`

---

## 9. Proximos Passos Planejados

1. Revisar as 558 linhas marcadas (validacao por excecao).
2. Revisar uma amostra estratificada das linhas de alta confianca (validacao por amostragem), sorteada por municipio, area tematica, tipo de gasto e confianca.
3. Aplicar as correcoes na copia de trabalho e registrar a taxa de manutencao e de correcao.
4. Produzir o relatorio final de validacao, com concordancia por coluna e analise das divergencias.
5. So depois disso, decidir se algum padrao aprendido vira regra operacional validada.

---

## 10. Espaco Do Pesquisador

Use esta secao para registrar, com suas palavras, as decisoes que so voce pode explicar. Sugestoes de topicos:

### 10.1 Justificativa Do Projeto

`[PREENCHER: por que este trabalho e relevante para o municipio/estado/academia? Qual lacuna ele preenche?]`

### 10.2 Papel Do Pesquisador No Metodo

`[PREENCHER: descrever seu papel como revisor humano: o que voce conferiu nos lotes, que criterios contabeis/orcamentarios usou, exemplos de decisoes que tomou.]`

### 10.3 Decisoes Metodologicas Tomadas

Ja registradas no projeto (confirme e complemente):

* classificar apenas `Area Tematica` e `Gasto E ou NE` nesta etapa;
* deixar `Indicador` para a fase de ponderacao;
* comecar por lotes pequenos revisados antes de escalar;
* prevalencia do Guia sobre os exemplos humanos em caso de conflito.

`[PREENCHER: outras decisoes e suas razoes.]`

### 10.4 Observacoes Da Revisao Humana

`[PREENCHER: padroes de erro ou acerto que voce percebeu; casos dificeis; sugestoes de ajuste na regra.]`

### 10.5 Conclusoes Parciais

`[PREENCHER: sua avaliacao, como especialista, sobre a viabilidade do metodo ate aqui.]`

---

## 11. Perguntas Frequentes (Para Apresentacoes)

**"A IA foi treinada com os dados dos municipios?"**
Nao. O modelo nao foi treinado nem alterado. Ele recebeu a regra (Guia estruturado) e exemplos humanos como material de consulta no momento da classificacao. O termo correto e aprendizado em contexto.

**"Como sei que a IA nao inventou classificacoes?"**
Tres protecoes: (1) ela so pode usar os rotulos validos da metodologia; (2) cada linha tem justificativa registrada em log, conferivel contra a planilha; (3) as linhas em que ela teve menos certeza estao marcadas para revisao humana.

**"A IA substitui o especialista?"**
Nao. O desenho e de supervisao humana: o especialista calibra (lotes iniciais), a IA escala (linhas restantes) e o especialista valida (revisao por excecao e por amostragem). A palavra final e sempre humana.

**"E se a IA errar?"**
O erro e corrigivel: existe um fluxo de revisao em que o humano marca `OK`, `Corrigir` ou `Duvida` em uma amostra, e as correcoes sao aplicadas na planilha com registro. Erros recorrentes viram aprendizado documentado.

**"Os resultados valem para qualquer municipio?"**
Por enquanto o metodo foi aplicado a municipios do Tocantins. A estrutura orcamentaria brasileira e padronizada (funcao/subfuncao), o que favorece a generalizacao, mas isso ainda precisa ser testado formalmente.

**"O arquivo original esta seguro?"**
Sim. O original nunca foi alterado; todos os preenchimentos ocorreram em uma copia de trabalho, e ha verificacao automatica disso.

---

## 12. Glossario

| Termo | Significado simples |
| --- | --- |
| IA / LLM | Programa de inteligencia artificial que entende e produz texto (como o ChatGPT ou o Claude). LLM = "grande modelo de linguagem". |
| Aprendizado em contexto | A IA consulta materiais fornecidos na hora (regra + exemplos) em vez de ser treinada/modificada. |
| Knowledge Bundle | O Guia UNICEF reorganizado em arquivos de consulta por assunto; a "fonte normativa" do projeto. |
| Municipios-base | Os 5 municipios com classificacao feita por humanos, usados como exemplos praticos. |
| Municipios de teste | Os 10 municipios cujas despesas a IA classificou. |
| Lote | Grupo de 20 linhas classificado e revisado antes de continuar. |
| Confianca (Alta/Media/Baixa) | O grau de certeza que a IA declarou em cada classificacao. |
| Log | Arquivo de registro linha a linha (o "papel de trabalho" da classificacao). |
| Copia de trabalho | Copia da planilha original onde o preenchimento e feito, preservando o original. |
| Script / skill | Pequenos programas que executam tarefas repetitivas (rodar a classificacao, gerar amostra de revisao etc.). O pesquisador nao precisa le-los. |
| Despesa-meio | Despesa administrativa ou de apoio (manutencao de secretaria, fundo etc.), que exige criterio especial no Guia. |

---

## 13. Onde Conferir Cada Informacao

| Informacao | Arquivo |
| --- | --- |
| Planilha original (intocada) | `fonte_parte_2.xlsx` |
| Planilha classificada | `parte2/resultados/fonte_parte_2_trabalho.xlsx` |
| Registro linha a linha | `parte2/resultados/classificacao_automatica_supervisionada_log.xlsx` |
| Relatorio geral | `parte2/resultados/relatorio_classificacao_automatica_supervisionada.md` |
| Relatorios dos lotes iniciais | `parte2/resultados/relatorio_lote_piloto_001.md` ate `relatorio_lote_006.md` |
| Regra estruturada (Guia) | `parte2/knowledge_bundle/` |
| Guia UNICEF em texto | `parte2/guia_unicef.md` |
| Historico tecnico completo | `fase_projeto.md` e `parte2/ESTADO_PROJETO.md` |
| Complemento metodologico | `PARTE2_COMPLEMENTO.md` |
