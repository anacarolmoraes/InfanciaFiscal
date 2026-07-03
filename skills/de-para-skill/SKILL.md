---
name: de-para-skill
description: Use esta skill sempre que o usuário pedir para cruzar dados, fazer de-para de municípios, consolidar planilhas do Infância Fiscal, ou resgatar o trabalho humano de classificação. A skill serve para copiar a classificação valiosa (Área Temática, Gasto E ou NE e Indicador) feita por um humano nas abas dos municípios para a planilha consolidada geral_classificado.
---
# de-para-skill

Atue como um especialista em automação e processamento de dados em Excel. 
Sua tarefa é realizar o cruzamento de dados para resgatar a valiosa classificação feita por humanos nas abas de municípios e transferi-la com segurança para a planilha consolidada `geral_classificado`.

Para priorizar a **economia de tokens e a rapidez de execução**, você DEVE criar e executar um script em Python (utilizando a `venv` do projeto) para realizar este trabalho, em vez de tentar editar os dados linha por linha manualmente.

## 1. Regras do Script e Bibliotecas
- **Leitura de Cores e Preservação de Formatação:** Como a estrutura depende de cores e o arquivo original não pode ter seu layout ou outras colunas alterados, utilize a biblioteca `openpyxl` (ou equivalente que preserve o layout). O `pandas` **não lê formatação de cores** e destruiria a estrutura visual do Excel ao salvar o arquivo final.
- **Backup Prévio:** Antes de alterar o arquivo, o script deve criar automaticamente uma cópia de segurança (ex: `final_geral_trabalho_bkp.xlsx`).
- **Edição no Arquivo Original:** Após o backup, o script deve aplicar as alterações **diretamente no arquivo original**, modificando **apenas e especificamente as colunas solicitadas** na tarefa, deixando todo o restante (dados e formatação) intacto.

## 2. Estrutura da Planilha de Município
A estrutura é hierárquica e o script precisará analisar as propriedades de preenchimento (cor de fundo) das células:
- **Vermelho**: Nome do Programa.
- **Verde**: Função.
- **Laranja**: Subfunção.
- **Amarelo**: Ação Orçamentária (células mais externas).

## 3. Tarefa de Cruzamento
Para cada aba de município, identifique e copie a classificação humana presente nas colunas **(Área Temática)**, **(Gasto E ou NE)** e **(Indicador)** para as colunas correspondentes na aba `geral_classificado`.

**ATENÇÃO:** As letras (A, B, C, etc.) que abrigam essas colunas poderão mudar em algum momento do processamento. Portanto, o script deve identificar as colunas ativamente **pelo nome do cabeçalho** na primeira linha, a cada execução.

## 4. Critério de Match
- Utilize a hierarquia completa para garantir o encontro exato das linhas: **(Programa + Função + Subfunção + Ação Orçamentária)**, combinado com o **nome do município correspondente** (nome da aba).
- **Nota sobre Normalização:** A etapa de normalização textual (remoção de acentos, caracteres invisíveis, etc.) ocorre em uma skill anterior e separada. Foque em criar a lógica de match baseada nos dados disponíveis.

## 5. Validação e Relatório (Logs)
- Ao final da execução do script, o sistema deve gerar um arquivo de texto (ex: `relatorio_cruzamento.txt`) documentando o resultado da operação, contendo:
  - Resumo estatístico de sucessos e falhas.
  - Lista de quais ações/municípios falharam por não encontrarem correspondência (match), permitindo rápida revisão.

## 6. Arquivos e Diretórios de Trabalho
O arquivo alvo principal desta operação é o:
`C:\Users\anacrm\Documents\develop\github\InfanciaFiscal\final_geral_trabalho_.xlsx`
