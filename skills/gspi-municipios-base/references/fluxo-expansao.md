# Fluxo De Expansao Dos Municipios-Base

## Quando Expandir

Expanda municipios-base quando houver exemplos humanos novos e revisados, especialmente:

* municipios ainda ausentes da base;
* padroes de acao orcamentaria recorrentes;
* divergencias corrigidas durante revisao humana;
* decisoes metodologicas consolidadas.

Nao expanda a base com linhas ainda duvidosas.

## Fluxo Recomendado Para Usuario Leigo

1. Abrir `parte2/modelos/modelo_municipios_base.xlsx`.
2. Preencher a aba `novos_exemplos`.
3. Salvar uma copia com nome claro, por exemplo:

```text
novos_municipios_base_2026_07.xlsx
```

4. Pedir ao assistente:

```text
Use a skill gspi-municipios-base e valide este arquivo de novos municipios-base.
```

5. Corrigir problemas apontados na validacao, se houver.
6. Pedir:

```text
Expanda a base de municipios com este arquivo validado.
```

7. Quando for classificar novos arquivos, pedir:

```text
Sincronize a base expandida para o arquivo de classificacao.
```

## Regra De Ouro

Municipios-base sao exemplos humanos. Eles ajudam a interpretar casos parecidos, mas nao substituem o `knowledge_bundle/`.

Se um exemplo humano contradiz a metodologia GSPI-M, registre a divergencia para decisao metodologica em vez de transformar automaticamente em regra.

