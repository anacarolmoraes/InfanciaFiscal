import argparse
import sys
import os
import json
import xlwings as xw

# Ajusta path para importar o módulo limpador independente de onde o CLI for chamado
sys.path.append(os.path.dirname(__file__))
from limpador import limpar_texto_com_tracking, get_anomalias, DICT_PATH

sys.stdout.reconfigure(encoding='utf-8')


def _tem_tabela_dinamica(sheet):
    """Verifica se a aba possui Tabelas Dinâmicas (Pivot Tables)."""
    try:
        return sheet.api.PivotTables().Count > 0
    except Exception:
        return False


def update_dictionary(json_str):
    """Atualiza o dicionário de correções com novas palavras."""
    try:
        new_items = json.loads(json_str)
        if os.path.exists(DICT_PATH):
            with open(DICT_PATH, 'r', encoding='utf-8') as f:
                d = json.load(f)
        else:
            d = {}
        
        d.update(new_items)
        
        with open(DICT_PATH, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=4)
        print(f"Dicionário atualizado com sucesso! {len(new_items)} novas palavras inseridas.")
    except Exception as e:
        print(f"Erro ao atualizar dicionário: {e}")


def _processar_aba(sheet, col_names):
    """Processa uma única aba: localiza as colunas, duplica com formatação e aplica limpeza.
    
    Retorna True se processou pelo menos uma coluna, False caso contrário.
    """
    colunas_processadas = 0
    for col_name in col_names:
        # Procura o cabeçalho alvo nas primeiras linhas
        header_range = sheet.range('A1:Z10')
        col_header = None
        for cell in header_range:
            if cell.value == col_name:
                col_header = cell
                break
        
        if not col_header:
            print(f"  -> Cabeçalho '{col_name}' não encontrado nesta aba. Pulando.")
            continue
            
        col_idx = col_header.column
        row_header = col_header.row
        
        # 1. Renomeia header original
        col_header.value = f"{col_name}_original"
        
        # 2. Insere coluna nova à direita
        sheet.api.Columns(col_idx + 1).Insert()
        
        # 3. Configura novo header
        novo_header = sheet.range((row_header, col_idx + 1))
        novo_header.value = col_name
        novo_header.color = col_header.color
        
        last_row = sheet.range((sheet.cells.last_cell.row, col_idx)).end('up').row
        if last_row <= row_header:
            colunas_processadas += 1
            continue
            
        # Range dos dados (excluindo header)
        orig_range = sheet.range((row_header + 1, col_idx), (last_row, col_idx))
        dest_range = sheet.range((row_header + 1, col_idx + 1), (last_row, col_idx + 1))
        
        # 4. Performance: Copia ESTILOS da coluna original para a nova apenas se não for a aba pesada
        if sheet.name != 'geral_classificado':
            orig_range.copy()
            dest_range.paste('formats')
        else:
            print("  -> (PULANDO CÓPIA DE ESTILOS NA ABA GERAL PARA GARANTIR PERFORMANCE)")
        # 5. Processamento na memória
        valores_originais = orig_range.value
        if not isinstance(valores_originais, list):
            valores_originais = [valores_originais]
            
        novos_valores = []
        for val in valores_originais:
            if val is not None and str(val).strip() != "" and str(val).strip() != "Total Geral":
                novo_val = limpar_texto_com_tracking(str(val))
                novos_valores.append([novo_val])
            else:
                novos_valores.append([val])
                
        # 6. Gravação na planilha
        dest_range.value = novos_valores
        colunas_processadas += 1
        
    return colunas_processadas > 0


def process_excel(file_path, col_names, sheet_name=None, skip_pivots=False):
    """Processa a(s) aba(s) do arquivo Excel aplicando limpeza nas colunas alvo.
    
    Args:
        file_path: Caminho do arquivo Excel.
        col_names: Lista de nomes de colunas a serem limpas.
        sheet_name: Nome de uma aba específica (opcional). Se omitido, processa todas.
        skip_pivots: Se True, pula automaticamente abas com Tabela Dinâmica.
    """
    print(f"Iniciando limpeza nas colunas {col_names}...")
    app = None
    try:
        app = xw.App(visible=False)
        app.display_alerts = False
        app.screen_updating = False
        app.calculation = 'manual'
        wb = app.books.open(file_path, update_links=False)
        
        if sheet_name:
            sheets = [wb.sheets[sheet_name]]
        else:
            sheets = list(wb.sheets)

        abas_ok = 0
        abas_puladas = 0
        abas_erro = 0
            
        for sheet in sheets:
            print(f"Processando aba: {sheet.name}")

            # Pula abas com Tabela Dinâmica se solicitado
            if skip_pivots and _tem_tabela_dinamica(sheet):
                print(f"  -> Aba '{sheet.name}' contém Tabela Dinâmica. Pulando (--skip-pivots).")
                abas_puladas += 1
                continue

            try:
                if _processar_aba(sheet, col_names):
                    abas_ok += 1
                else:
                    abas_puladas += 1
            except Exception as e:
                # Captura erros por aba sem interromper o restante
                print(f"  -> Erro na aba '{sheet.name}': {e}")
                abas_erro += 1
            
        print("Salvando planilha...")
        app.calculation = 'automatic'
        wb.save()
        wb.close()
        app.quit()
        app = None
        print(f"Concluído! Processadas: {abas_ok} | Puladas: {abas_puladas} | Erros: {abas_erro}")
        
        # Self-Healing: Verifica anomalias
        anomalias = get_anomalias()
        if anomalias:
            print("\n" + "="*60)
            print("[ACTION_REQUIRED] Foram encontradas palavras corrompidas DESCONHECIDAS:")
            print(json.dumps(anomalias, ensure_ascii=False, indent=2))
            print("Agente: Inferir as correções e rodar CLI novamente usando:")
            print('python cli.py --update-dict \'{"CORROMPIDA": "CORRETA"}\'')
            print("="*60 + "\n")
            
    except Exception as e:
        print(f"Erro no processamento: {e}")
    finally:
        if app is not None:
            try:
                app.quit()
            except Exception:
                pass


def process_excel_fast(file_path, col_names, sheet_name=None):
    """Processa a(s) aba(s) do arquivo Excel rapidamente usando pandas, mantendo outras abas intactas.
    
    Args:
        file_path: Caminho do arquivo Excel.
        col_names: Lista de nomes de colunas a serem limpas.
        sheet_name: Nome de uma aba específica (opcional). Se omitido, processa todas.
    """
    import pandas as pd
    print(f"Iniciando limpeza rápida (Pandas) nas colunas {col_names}...")
    try:
        # Carrega o arquivo Excel para obter todas as abas
        xl = pd.ExcelFile(file_path)
        sheet_names = xl.sheet_names
        
        if sheet_name:
            if sheet_name not in sheet_names:
                print(f"Erro: Aba '{sheet_name}' não encontrada no arquivo.")
                return
            target_sheets = [sheet_name]
        else:
            target_sheets = sheet_names

        for s_name in target_sheets:
            print(f"Processando aba: {s_name}")
            
            # Lê apenas a primeira linha da aba para verificar as colunas existentes
            df_header = pd.read_excel(file_path, sheet_name=s_name, nrows=0)
            cols_to_process = [c for c in col_names if c in df_header.columns]
            
            if not cols_to_process:
                print(f"  -> Nenhuma das colunas {col_names} encontrada nesta aba. Pulando.")
                continue
            
            # Carrega os dados inteiros da aba
            df = pd.read_excel(file_path, sheet_name=s_name)
            
            for col in cols_to_process:
                print(f"  -> Limpando coluna: {col}...")
                col_idx = df.columns.get_loc(col)
                
                # Renomeia a coluna original
                cols_list = list(df.columns)
                cols_list[col_idx] = f"{col}_original"
                df.columns = cols_list
                
                # Aplica a limpeza
                cleaned = df[f"{col}_original"].apply(
                    lambda x: limpar_texto_com_tracking(str(x)) if pd.notnull(x) and str(x).strip() != "" else x
                )
                
                # Insere a nova coluna imediatamente após a original
                df.insert(col_idx + 1, col, cleaned)
                
            print(f"  -> Salvando aba '{s_name}' no arquivo Excel...")
            # Grava a aba substituindo-a e mantendo todas as outras intactas
            with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                df.to_excel(writer, sheet_name=s_name, index=False)
                
        print("Limpeza rápida concluída!")
        
        # Self-Healing: Verifica anomalias
        anomalias = get_anomalias()
        if anomalias:
            print("\n" + "="*60)
            print("[ACTION_REQUIRED] Foram encontradas palavras corrompidas DESCONHECIDAS:")
            print(json.dumps(anomalias, ensure_ascii=False, indent=2))
            print("Agente: Inferir as correções e rodar CLI novamente usando:")
            print('python cli.py --update-dict \'{"CORROMPIDA": "CORRETA"}\'')
            print("="*60 + "\n")
            
    except Exception as e:
        print(f"Erro no processamento rápido: {e}")


def main():
    """Ponto de entrada da CLI."""
    parser = argparse.ArgumentParser(description="CLI de Limpeza de Excel (Alta Performance & Self-Healing)")
    parser.add_argument('--file', type=str, help="Caminho do arquivo Excel")
    parser.add_argument('--col', type=str, help="Nome da coluna alvo ou lista separada por vírgulas")
    parser.add_argument('--sheet', type=str, help="Aba específica (opcional)", default=None)
    parser.add_argument('--skip-pivots', action='store_true',
                        help="Pula automaticamente abas que contenham Tabelas Dinâmicas")
    parser.add_argument('--fast', action='store_true',
                        help="Usa Pandas para máxima velocidade (ignora formatação visual)")
    parser.add_argument('--update-dict', type=str, help="JSON string para atualizar o dicionário")
    
    args = parser.parse_args()
    
    if args.update_dict:
        update_dictionary(args.update_dict)
    elif args.file and args.col:
        cols = [c.strip() for c in args.col.split(',')]
        if args.fast:
            process_excel_fast(args.file, cols, args.sheet)
        else:
            process_excel(args.file, cols, args.sheet, args.skip_pivots)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

