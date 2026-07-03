---
name: tratamento_dados_excel
description: Limpeza e normalização de alta performance usando CLI (para preservar cores) ou Pandas (para máxima velocidade) e dicionário self-healing.
---

# Tratamento de Dados Excel (Versão 10x)

Você está lidando com planilhas contábeis e municipais onde o rigor dos dados é máximo. O objetivo desta skill é fornecer uma ferramenta de limpeza e normalização (remoção de acentos, caracteres corrompidos, espaços), com capacidade de **auto-aprendizado** para caracteres anômalos.

## 1. Decisão Estratégica: Formatação vs Velocidade (PERGUNTE AO USUÁRIO)
Antes de executar a limpeza, você DEVE obrigatoriamente fazer a seguinte pergunta ao usuário:
> "Você precisa que a formatação visual (cores, bordas) original seja preservada (mais lento), ou prefere máxima velocidade (salvando a aba em um arquivo novo, sem as formatações originais)?"

### OPÇÃO A: Se o usuário quiser PRESERVAR formatação (xlwings)
Use o executável de linha de comando (CLI) já configurado na pasta da skill.
Execute no terminal (PowerShell):
```powershell
python skills/tratamento_dados_excel/cli.py --file "C:\caminho\da\planilha.xlsx" --col "NomeDaColuna"
```
**Flags opcionais:**
- `--sheet "Nome da Aba"` — processa apenas uma aba específica.
- `--skip-pivots` — pula automaticamente abas que contenham Tabelas Dinâmicas (Pivot Tables), evitando erros do Excel.

O CLI cuidará de duplicar as colunas e copiar a formatação exata usando `xlwings`. Atenção: isso abre o Excel em background e pode ser demorado ou falhar se o arquivo for excessivamente pesado (MemoryError) ou estiver bloqueado.

**⚠️ Encoding no Windows:** Se os nomes das abas ou colunas contiverem acentos (ex: `Rótulos de Linha`, `Fátima`), o PowerShell pode corromper os caracteres ao passá-los como argumentos. Nesse caso, invoque a CLI diretamente via Python para garantir encoding UTF-8:
```python
from skills.tratamento_dados_excel.cli import process_excel
process_excel("caminho/planilha.xlsx", "NomeDaColuna", sheet_name="Aba", skip_pivots=True)
```

### OPÇÃO B: Se o usuário preferir VELOCIDADE (pandas)
Use a flag `--fast` diretamente na CLI para rodar o processamento vetorizado via Pandas. Você pode passar múltiplas colunas separadas por vírgula em `--col`.
Execute no terminal (PowerShell):
```powershell
python skills/tratamento_dados_excel/cli.py --file "C:\caminho\da\planilha.xlsx" --col "Coluna1,Coluna2" --sheet "Nome da Aba" --fast
```
Isso lê os dados usando Pandas, renomeia as colunas originais para `_original` e cria as colunas limpas logo ao lado, salvando apenas a aba especificada de forma muito rápida e mantendo as outras abas do arquivo intocadas.

## 2. Auto-Aprendizado (Self-Healing)
Independentemente da opção escolhida, o script usa a função central que audita as palavras na memória.
- Se no console aparecer o aviso `[ACTION_REQUIRED]` com palavras corrompidas desconhecidas:
- Você (Agente) DEVE inferir a palavra correta.
- E ALIMENTARÁ O CLI rodando:
  ```powershell
  python skills/tratamento_dados_excel/cli.py --update-dict '{"PALAVRA_CORROMPIDÃ?": "PALAVRA_CORRETA"}'
  ```
- Após isso, rode o processo de limpeza novamente.

