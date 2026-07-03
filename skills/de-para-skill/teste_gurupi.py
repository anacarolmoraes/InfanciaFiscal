import sys
import os
import shutil
import xlwings as xw

sys.path.append(os.path.abspath('skills/tratamento_dados_excel'))
from limpador import limpar_texto

def normalize(text):
    if text is None: return ""
    return limpar_texto(str(text)).strip()

def main():
    print("Iniciando rotina de De-Para (Teste: Gurupi)...")
    
    # 1. Faz o backup
    print("Criando backup...")
    shutil.copy('final_geral_trabalho_.xlsx', 'final_geral_trabalho_bkp.xlsx')
    
    app = xw.App(visible=False)
    app.display_alerts = False
    
    try:
        wb = app.books.open('final_geral_trabalho_.xlsx', update_links=False)
        
        # Mapeamento de cores
        COLOR_PROGRAMA = (255, 0, 0)
        COLOR_FUNCAO = (146, 208, 80)
        COLOR_SUBFUNCAO = (255, 192, 0)
        COLOR_ACAO = (255, 255, 0)
        
        # Ler aba Gurupi
        sheet_mun = wb.sheets['Gurupi']
        
        # Descobrir colunas de Área Temática etc na aba do municipio
        header_row = 3
        col_area = None
        col_gasto = None
        col_indicador = None
        
        for c in range(1, 20):
            val = sheet_mun.range((header_row, c)).value
            if val:
                val_str = str(val).lower()
                if 'rea' in val_str and 'tem' in val_str:
                    col_area = c
                elif 'gasto' in val_str:
                    col_gasto = c
                elif 'indicad' in val_str:
                    col_indicador = c
                    
        print(f"Colunas encontradas: Area={col_area}, Gasto={col_gasto}, Indicador={col_indicador}")
        
        last_row_mun = sheet_mun.range(f'A{sheet_mun.cells.last_cell.row}').end('up').row
        
        # Construir dicionario
        de_para_dict = {}
        curr_programa = ""
        curr_funcao = ""
        curr_subfuncao = ""
        
        for r in range(header_row + 1, last_row_mun + 1):
            cell_a = sheet_mun.range((r, 1))
            val = cell_a.value
            if not val:
                continue
                
            color = cell_a.color
            val_norm = normalize(val)
            
            if color == COLOR_PROGRAMA:
                curr_programa = val_norm
            elif color == COLOR_FUNCAO:
                curr_funcao = val_norm
            elif color == COLOR_SUBFUNCAO:
                curr_subfuncao = val_norm
            elif color == COLOR_ACAO:
                curr_acao = val_norm
                
                # Pega classificacao
                area = sheet_mun.range((r, col_area)).value if col_area else None
                gasto = sheet_mun.range((r, col_gasto)).value if col_gasto else None
                indicador = sheet_mun.range((r, col_indicador)).value if col_indicador else None
                
                key = ("GURUPI", curr_programa, curr_funcao, curr_subfuncao, curr_acao)
                de_para_dict[key] = (area, gasto, indicador)
                
        print(f"Dicionario construído com {len(de_para_dict)} mapeamentos classificados!")
        
        # 2. Injetar na aba geral_classificado
        sheet_geral = wb.sheets['geral_classificado']
        
        # Descobrir colunas na geral_classificado
        header_range = sheet_geral.range('A1:AZ1').value
        
        idx_mun = next(i for i, v in enumerate(header_range) if v and 'nomeMunicipio' in str(v))
        idx_prog = next(i for i, v in enumerate(header_range) if v and v == 'nomePrograma')
        idx_func = next(i for i, v in enumerate(header_range) if v and v == 'nomeFuncao')
        idx_sub = next(i for i, v in enumerate(header_range) if v and v == 'nomeSubFuncao')
        idx_acao = next(i for i, v in enumerate(header_range) if v and v == 'nomeAcaoOrcamentaria')
        
        col_out_area = next(i+1 for i, v in enumerate(header_range) if v and 'rea Tem' in str(v))
        col_out_gasto = next(i+1 for i, v in enumerate(header_range) if v and 'Gasto E ou NE' in str(v))
        col_out_ind = next(i+1 for i, v in enumerate(header_range) if v and 'Indicador' in str(v))
        
        last_row_geral = sheet_geral.range(f'A{sheet_geral.cells.last_cell.row}').end('up').row
        
        mun_vals = sheet_geral.range((2, idx_mun+1), (last_row_geral, idx_mun+1)).value
        prog_vals = sheet_geral.range((2, idx_prog+1), (last_row_geral, idx_prog+1)).value
        func_vals = sheet_geral.range((2, idx_func+1), (last_row_geral, idx_func+1)).value
        sub_vals = sheet_geral.range((2, idx_sub+1), (last_row_geral, idx_sub+1)).value
        acao_vals = sheet_geral.range((2, idx_acao+1), (last_row_geral, idx_acao+1)).value
        
        orig_area = sheet_geral.range((2, col_out_area), (last_row_geral, col_out_area)).value
        orig_gasto = sheet_geral.range((2, col_out_gasto), (last_row_geral, col_out_gasto)).value
        orig_ind = sheet_geral.range((2, col_out_ind), (last_row_geral, col_out_ind)).value
        
        if not isinstance(orig_area, list): orig_area = [orig_area]
        if not isinstance(orig_gasto, list): orig_gasto = [orig_gasto]
        if not isinstance(orig_ind, list): orig_ind = [orig_ind]
        
        out_area = []
        out_gasto = []
        out_ind = []
        
        matches = 0
        misses = 0
        missing_keys = set()
        
        print("Realizando match...")
        for i in range(len(mun_vals)):
            mun = normalize(mun_vals[i])
            prog = normalize(prog_vals[i])
            func = normalize(func_vals[i])
            sub = normalize(sub_vals[i])
            acao = normalize(acao_vals[i])
            
            key = (mun, prog, func, sub, acao)
            
            if mun == "GURUPI":
                if key in de_para_dict:
                    area, gasto, ind = de_para_dict[key]
                    out_area.append([area if area else orig_area[i]])
                    out_gasto.append([gasto if gasto else orig_gasto[i]])
                    out_ind.append([ind if ind else orig_ind[i]])
                    matches += 1
                else:
                    out_area.append([orig_area[i]])
                    out_gasto.append([orig_gasto[i]])
                    out_ind.append([orig_ind[i]])
                    misses += 1
                    missing_keys.add(key)
            else:
                out_area.append([orig_area[i]])
                out_gasto.append([orig_gasto[i]])
                out_ind.append([orig_ind[i]])
                
        print(f"Matches em Gurupi: {matches} | Falhas (Misses): {misses}")
        
        # Escrever na planilha
        print("Gravando valores...")
        sheet_geral.range((2, col_out_area), (last_row_geral, col_out_area)).value = out_area
        sheet_geral.range((2, col_out_gasto), (last_row_geral, col_out_gasto)).value = out_gasto
        sheet_geral.range((2, col_out_ind), (last_row_geral, col_out_ind)).value = out_ind
        
        wb.save()
        
        with open('relatorio_cruzamento.txt', 'w', encoding='utf-8') as f:
            f.write(f"Relatório de Cruzamento (Gurupi)\n")
            f.write(f"Matches obtidos: {matches}\n")
            f.write(f"Linhas de Gurupi que não encontraram hierarquia na aba geral: {misses}\n\n")
            f.write(f"Hierarquias sem match:\n")
            for k in missing_keys:
                f.write(str(k) + "\n")
                
        print("Script finalizado com sucesso!")
        
    finally:
        wb.close()
        app.quit()

if __name__ == '__main__':
    main()
