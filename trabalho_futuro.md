# Trabalho Futuro - Obsidian Vault E Conversa Com O Bundle

## Contexto

Durante a implementacao da Parte 2, surgiu a discussao sobre onde criar um vault do Obsidian e como ele se relaciona com o `knowledge_bundle/`.

O objetivo e permitir que o cliente visualize melhor a estrutura do classificador e, ao mesmo tempo, preservar um artefato operacional limpo para uso pela LLM.

## Decisao Recomendada

Nao criar o vault do Obsidian dentro de `knowledge_bundle/`.

Motivo: `knowledge_bundle/` deve permanecer limpo, versionavel, compativel com OKF e consumivel pela LLM. Um vault do Obsidian tende a criar arquivos e convencoes proprias, como `.obsidian/`, plugins, templates, notas de curadoria, mapas e configuracoes visuais.

## Arquitetura Recomendada

```text
parte2/
├── vault_gspi/                  # segundo cerebro completo
│   ├── 00 - Comece Aqui.md
│   ├── 01 - Knowledge Bundle/
│   ├── 02 - Guia UNICEF/
│   ├── 03 - Exemplos Humanos/
│   ├── 04 - Casos Dificeis/
│   ├── 05 - Avaliacoes/
│   ├── 90 - Metodologia Proprietaria/
│   ├── 99 - Arquivo/
│   └── .obsidian/
│
├── knowledge_bundle/            # export limpo / fonte operacional OKF
├── manuals/
├── prompts/
├── workflow/
└── resultados/
```

## Criterio Brutalmente Sincero

O vault e bom como segundo cerebro porque permite expansao, associacao, curadoria, anotacoes, casos dificeis, mapas e evolucao metodologica.

Mas ele nao deve substituir diretamente o bundle operacional limpo.

O risco de colocar tudo em um unico lugar sem separacao e misturar:

1. conhecimento normativo: o que o Guia diz;
2. conhecimento operacional: como o classificador deve decidir;
3. conhecimento de construcao: como o sistema foi criado, testado e refinado.

Para o desenvolvedor, essa mistura pode ser fertil. Para o cliente e para a LLM, pode gerar ruido, ambiguidade e risco de tratar rascunhos como regra final.

## Recomendacao Final

Criar um vault mestre para pensamento, curadoria e apresentacao, mas manter uma area claramente marcada como export operacional.

Resumo:

* Para desenvolver o metodo: vault como segundo cerebro.
* Para a LLM classificar: `knowledge_bundle/` limpo como fonte canonica.
* Para o cliente entender: vault curado e didatico.
* Para publicacao cientifica: documentacao separada, com metodologia descrita em alto nivel.

O vault e organismo. O bundle e instrumento.

## Conversar Com O Bundle

E possivel conversar com o bundle, mas o bundle sozinho nao conversa. Quem conversa e uma LLM usando o bundle como base de conhecimento.

Niveis possiveis:

1. Conversa manual no Codex: pedir explicitamente para usar `parte2/knowledge_bundle/`.
2. Conversa em Obsidian: usar plugins de IA/RAG que indexem o vault.
3. Chat dedicado/RAG: criar uma interface que indexa o bundle, recupera trechos relevantes e aplica o prompt do classificador.

O melhor produto seria um chat com protocolo:

1. recebe pergunta ou linha orcamentaria;
2. busca trechos relevantes do bundle;
3. aplica o manual da LLM;
4. responde com decisao, justificativa e fonte interna;
5. marca incertezas.

Exemplo de pergunta:

```text
Use o Knowledge Bundle GSPI-M para avaliar:
Programa: Gestao e Manutencao
Funcao: Urbanismo
Subfuncao: Servicos Urbanos
Acao: Manutencao de pracas com areas infantis
```

Exemplo de resposta esperada:

```text
Decisao GSPI: GSPI
Area tematica: Direito a Cidade e Habitacao
Subarea tematica: 5.3 Promocao de Espacos Urbanos Inclusivos para Criancas
Classificacao E/NE: Ampliado
Ponderador sugerido: percentual de criancas de 0 a 6 anos na populacao total
Justificativa: ...
```
