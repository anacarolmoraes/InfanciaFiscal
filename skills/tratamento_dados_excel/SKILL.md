---
name: tratamento_dados_excel
description: Limpeza e normalização de alta performance usando CLI e dicionário self-healing.
---

# Tratamento de Dados Excel (Versão 10x)

Você está lidando com planilhas contábeis e municipais onde o rigor dos dados é máximo. O objetivo desta skill é fornecer uma ferramenta de **alta performance** (vetorizada), com preservação nativa do estilo visual do Excel, e capacidade de **auto-aprendizado** para caracteres corrompidos.

## 1. Regra de Ouro (Custo Zero de Código)
Você **NUNCA** deve escrever scripts Python descartáveis para limpar a planilha. Ao invés disso, você DEVE simplesmente rodar o nosso executável de linha de comando (CLI) já configurado na pasta da skill.

## 2. Como usar a Ferramenta CLI
Quando o usuário pedir para tratar uma coluna (ex: `Rótulos de Linha`), execute no terminal (PowerShell):

```powershell
python skills/tratamento_dados_excel/cli.py --file "C:\caminho\da\planilha.xlsx" --col "NomeDaColuna"
```
*(Opcional: você pode adicionar `--sheet "Nome da Aba"` se não quiser rodar em todas as abas).*

A ferramenta CLI cuidará 100% de:
- Copiar a coluna original renomeando-a para `_original`.
- Duplicar a formatação exata, cores e bordas em massa sem perder performance.
- Limpar `ftfy`, remover acentos e corrigir os erros complexos do caractere `Ã?`.

## 3. Auto-Aprendizado (Self-Healing)
Como o CLI é inteligente, ele audita as palavras na memória.
- Se o CLI detectar que existe alguma palavra desconhecida que não conseguiu ser recuperada (imprimindo no console a tag `[ACTION_REQUIRED]`), você (Agente) DEVE agir!
- Você analisará o JSON impresso no console com as palavras não mapeadas.
- Inferirá qual seria a palavra correta baseada no contexto fiscal/municipal.
- **ALIMENTARÁ O CLI** rodando o comando:
  ```powershell
  python skills/tratamento_dados_excel/cli.py --update-dict '{"PALAVRA_CORROMPIDÃ?": "PALAVRA_CORRETA"}'
  ```
- E então rodará o comando `--file` novamente para que a limpeza seja perfeita.

## 4. Resultado Esperado
O uso da CLI reduz drasticamente seu consumo de tokens e reduz a chance de erros sintáticos em scripts gerados sob demanda, garantindo uma resposta ultrarrápida para o usuário.
