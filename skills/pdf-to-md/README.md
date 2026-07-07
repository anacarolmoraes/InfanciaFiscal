# Skill: pdf-to-md

Esta skill permite a conversão de arquivos PDF para Markdown de forma local, rápida e segura.

## Instalação

A skill utiliza o projeto `pdfmd` que já foi clonado e instalado no seu `venv`.

**Dependências de Sistema (Opcional para OCR):**
Para converter PDFs que são imagens (scans), você deve instalar o Tesseract OCR no seu Windows:
1. Baixe o instalador: [Tesseract OCR for Windows](https://github.com/UB-Mannheim/tesseract/wiki).
2. Adicione ao PATH durante a instalação.

## Como Usar

Você pode me pedir para converter arquivos diretamente:

- "Converta o arquivo `docs/relatorio.pdf` para markdown."
- "Extraia o texto e as tabelas deste PDF: `artigo.pdf`."
- "Use OCR para ler este PDF digitalizado: `scaneado.pdf`."

## Vantagens
- **Tabelas**: Converte tabelas de PDF para tabelas de Markdown reais.
- **Matemática**: Mantém equações em formato LaTeX.
- **Privacidade**: Seus arquivos não saem do seu computador.
