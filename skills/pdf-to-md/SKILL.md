---
name: pdf-to-md
description: "Transforma PDFs em Markdown limpo usando processamento local/offline, com validacao automatica de qualidade e fallbacks economicos em tokens via bibliotecas Python locais ou OCR quando disponiveis. Use quando Codex precisar converter PDF para Markdown, preparar PDFs para consumo por LLM, validar se a conversao ficou boa, ou recuperar conversoes ruins sem enviar documentos a servicos externos."
---

# pdf-to-md

## Objetivo

Converter PDFs para Markdown de forma local, privada e economica em tokens.

Use o script `scripts/convert.py` como interface padrao. Ele:

1. executa `pdfmd` local;
2. valida automaticamente o Markdown gerado;
3. tenta fallbacks locais se a validacao falhar;
4. grava um relatorio pequeno `*.conversion_report.json`;
5. imprime um resumo JSON para o agente ler antes de abrir qualquer Markdown grande.

## Regra De Economia De Tokens

Nao leia o Markdown inteiro logo apos a conversao.

Leia primeiro o `*.conversion_report.json`. Abra trechos do Markdown somente se o relatorio indicar sucesso ou se for necessario diagnosticar uma falha especifica.

## Comando Padrao

Execute a partir da raiz do repositorio:

```powershell
.\.venv\Scripts\python.exe .\skills\pdf-to-md\scripts\convert.py "arquivo.pdf" -o "saida.md" -- --ocr auto --lang por --stats
```

Notas:

- Tudo depois de `--` e repassado ao `pdfmd`.
- Se `-o` apontar para uma pasta, o script cria `nome-do-pdf.md` dentro dela.
- O script detecta `.venv`, `venv` ou o Python atual.
- O script injeta `pdfmd/` no `PYTHONPATH`, entao nao depende de gastar tokens explicando instalacao editavel.

## Validacao

O relatorio avalia, sem LLM:

- existencia do arquivo `.md`;
- tamanho minimo;
- contagem de palavras;
- headings;
- tabelas Markdown;
- caracteres de substituicao Unicode;
- taxa de caracteres suspeitos;
- presenca de termos do nome do arquivo.

Considere a conversao boa quando `passed` for `true` e `score >= 70`.

## Fallbacks Locais

Se a validacao falhar, o script tenta, nesta ordem:

1. `pdfplumber`, se instalado;
2. `pypdf` ou `PyPDF2`, se instalado;
3. OCR via `pdf2image` + `pytesseract` + binario `tesseract`, se todos estiverem disponiveis.

Se uma dependencia nao existir, o relatorio marca o fallback como `skipped`. Nao instale pacotes sem permissao explicita do usuario.

## Privacidade

Nunca envie PDFs a servicos externos. Conversao, validacao e OCR devem ocorrer somente em ferramentas locais.

## Quando A Conversao Falhar

Reporte ao usuario:

- caminho do `.md`;
- caminho do relatorio;
- `score`;
- motivos em `reasons`;
- fallbacks tentados ou pulados.

Depois proponha o menor proximo passo: instalar dependencias locais, tentar outro modo de OCR, ou revisar trechos problematicos.
