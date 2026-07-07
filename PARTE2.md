# Parte 2 – Construção de um Classificador Especializado Baseado em LLM

## Objetivo

Esta etapa do projeto tem como objetivo desenvolver um **classificador especializado** capaz de reproduzir a classificação humana de ações orçamentárias utilizando uma Large Language Model (LLM).

O diferencial do projeto não está na LLM, mas na utilização de um **Knowledge Bundle** estruturado, derivado do Guia da UNICEF, combinado com exemplos reais previamente classificados por especialistas humanos.

O resultado esperado é um classificador reproduzível, capaz de ser utilizado por terceiros sem necessidade de conhecer a metodologia interna utilizada para sua construção.

---

# Objetivo científico

O objetivo científico do projeto é investigar se uma LLM consegue reproduzir, com elevado grau de concordância, o processo humano de classificação de ações orçamentárias quando recebe:

* um conjunto estruturado de conhecimento normativo;
* exemplos previamente classificados por especialistas;
* um protocolo padronizado de utilização.

O foco da pesquisa não é treinar a LLM, mas avaliar sua capacidade de realizar **inferência em contexto (In-Context Learning)** utilizando conhecimento previamente estruturado.

---

# Arquitetura Conceitual

O projeto é dividido em duas camadas completamente distintas.

## Camada 1 — Metodologia Proprietária

Esta camada corresponde ao método desenvolvido para transformar documentos normativos em conhecimento operacional.

Ela constitui propriedade intelectual do desenvolvedor e não faz parte da entrega ao cliente.

Exemplos:

* engenharia de conhecimento;
* pipeline de compilação;
* prompts internos;
* heurísticas;
* skills utilizadas;
* validações internas;
* refinamentos iterativos;
* organização dos bundles.

Essa camada poderá ser descrita de forma resumida em trabalhos científicos, mas sua implementação operacional permanece proprietária.

---

## Camada 2 — Produto Entregável

O cliente recebe apenas os artefatos necessários para utilizar o classificador.

Esses artefatos incluem:

* Knowledge Bundle;
* Operating Manual do Usuário;
* Operating Manual da LLM;
* municípios-base;
* prompts de utilização;
* workflow operacional;
* template de classificação.

O usuário consegue executar o classificador sem conhecer a metodologia utilizada para construir o bundle.

---

# Fluxo Geral

```text
Guia UNICEF (PDF)
        ↓
Extração para Markdown (pdfmd)
        ↓
Knowledge Bundle
        ↓
Municípios-base
        ↓
Operating Manual da LLM
        ↓
LLM
        ↓
Classificação
        ↓
Comparação com classificação humana
```

---

# Papel do Knowledge Bundle

O Knowledge Bundle representa o conhecimento operacional do domínio.

Ele não é um resumo do Guia.

Ele contém apenas o conhecimento necessário para permitir que a LLM realize a tarefa de classificação.

Seu conteúdo é organizado para consumo por modelos de linguagem.

---

# Papel dos Municípios-base

Os municípios-base não representam conhecimento normativo.

Eles representam experiência humana.

Sua finalidade é demonstrar como as regras presentes no Knowledge Bundle foram aplicadas na prática.

Eles funcionam como exemplos de referência durante a inferência.

---

# Papel da LLM

A LLM não aprende novos parâmetros.

Ela realiza inferência utilizando:

* Knowledge Bundle;
* municípios-base;
* protocolo operacional.

O processo corresponde ao uso de aprendizado em contexto (*In-Context Learning*).

---

# Papel do Guia da UNICEF

O Guia constitui a fonte normativa primária.

Sempre que houver conflito entre:

* Guide;
* municípios-base;

prevalece o Guia.

Os municípios-base existem apenas para ilustrar a aplicação prática das regras.

---

# Processo de Classificação

Para cada linha da planilha, a LLM deverá interpretar conjuntamente:

* Programa;
* Função;
* Subfunção;
* Ação Orçamentária.

Esses quatro elementos formam a unidade de inferência.

A classificação jamais deverá considerar apenas a descrição da ação orçamentária.

---

Após interpretar a hierarquia, a LLM deverá:

1. identificar a política pública correspondente;
2. identificar a finalidade da ação;
3. consultar o Knowledge Bundle;
4. comparar com os municípios-base;
5. inferir a Área Temática;
6. inferir Gasto E/NE;
7. verificar consistência antes de registrar o resultado.

---

# Produto Final

O produto entregue ao cliente consiste em um Sistema Especialista baseado em LLM composto por:

* Knowledge Bundle;
* exemplos humanos;
* protocolo operacional;
* prompts de utilização;
* documentação;
* workflow de classificação.

---

# Propriedade Intelectual

## Pertence ao cliente

* documentos fornecidos;
* Knowledge Bundle produzido especificamente para seu domínio;
* municípios classificados;
* resultados produzidos pelo classificador.

## Permanece de propriedade do desenvolvedor

* metodologia de engenharia de conhecimento;
* pipeline de compilação;
* prompts internos;
* skills;
* processos de validação;
* arquitetura do sistema;
* heurísticas;
* templates de construção;
* melhorias futuras da metodologia.

---

# Posicionamento do Serviço

O serviço não consiste em desenvolver um classificador específico.

O serviço consiste em desenvolver **Sistemas Especialistas Baseados em LLM**, capazes de transformar conhecimento normativo em conhecimento operacional reutilizável.

O classificador da UNICEF constitui apenas um caso de aplicação desse método.

A mesma metodologia poderá ser utilizada para construir sistemas especialistas em outros domínios, preservando a mesma arquitetura e alterando apenas a base de conhecimento utilizada.

---

# Organização da Pasta `parte2`

```text
parte2/
│
├── README.md
├── knowledge_bundle/
│   └── knowledge_bundle.okf
│
├── manuals/
│   ├── operating_manual_humano.md
│   └── operating_manual_llm.md
│
├── prompts/
│   ├── classificador.md
│   ├── avaliacao.md
│   └── revisao.md
│
├── workflow/
│   └── workflow.md
│
├── municipios_base/
│
└── resultados/
```

---

# Próximos Passos

1. Converter o Guia da UNICEF (PDF) localizado em C:\Users\anacrm\Documents\develop\github\InfanciaFiscal\Guia de Apuração do Gasto Social com a Primeira Infância (GSPI-M).pdf.pdf para Markdown utilizando necessariamente a skill skills\pdf-to-md.
2. Construir o Knowledge Bundle em formato compatível com o OKF, após aprender a fazer em <https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md>
3. Validar o bundle quanto à completude e consistência.
4. Preparar os cinco municípios-base como exemplos de referência.
5. Elaborar o Operating Manual da LLM.
6. Executar a classificação dos dez municípios de teste.
7. Comparar os resultados com a classificação humana.
8. Avaliar a concordância e documentar os resultados do experimento.
