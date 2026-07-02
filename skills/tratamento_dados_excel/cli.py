import argparse
import sys
import os
import json
import xlwings as xw

# Ajusta path para importar o módulo limpador independente de onde o CLI for chamado
sys.path.append(os.path.dirname(__file__))
from limpador import limpar_texto_com_tracking, get_anomalias, DICT_PATH

sys.stdout.reconfigure(encoding='utf-8')

def update_dictionary(json_str):
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

def process_excel(file_path, col_name, sheet_name=None):
    print(f"Iniciando limpeza na coluna '{col_name}'...")
    try:
        app = xw.App(visible=False)
        wb = app.books.open(file_path)
        
        if sheet_name:
            sheets = [wb.sheets[sheet_name]]
        else:
            sheets = wb.sheets
            
        for sheet in sheets:
            print(f"Processando aba: {sheet.name}")
            
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
                continue
                
            # Range dos dados (excluindo header)
            orig_range = sheet.range((row_header + 1, col_idx), (last_row, col_idx))
            dest_range = sheet.range((row_header + 1, col_idx + 1), (last_row, col_idx + 1))
            
            # 4. Performance Extrema: Copia todos os ESTILOS da coluna original para a nova de uma só vez
            orig_range.copy()
            dest_range.paste('formats')
            
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
            
        print("Salvando planilha...")
        wb.save()
        wb.close()
        app.quit()
        print("Concluído com sucesso!")
        
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
        try:
            app.quit()
        except:
            pass

def main():
    parser = argparse.ArgumentParser(description="CLI de Limpeza de Excel (Alta Performance & Self-Healing)")
    parser.add_argument('--file', type=str, help="Caminho do arquivo Excel")
    parser.add_argument('--col', type=str, help="Nome da coluna alvo")
    parser.add_argument('--sheet', type=str, help="Aba específica (opcional)", default=None)
    parser.add_argument('--update-dict', type=str, help="JSON string para atualizar o dicionário")
    
    args = parser.parse_args()
    
    if args.update_dict:
        update_dictionary(args.update_dict)
    elif args.file and args.col:
        process_excel(args.file, args.col, args.sheet)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
