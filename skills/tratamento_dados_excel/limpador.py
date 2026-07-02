import ftfy
import unidecode as ud
import json
import os

DICT_PATH = os.path.join(os.path.dirname(__file__), 'dicionario.json')

def load_dict():
    if os.path.exists(DICT_PATH):
        with open(DICT_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

DICIONARIO_CORRUPCAO = load_dict()
# Variável global para armazenar anomalias detectadas
anomalias_detectadas = set()

def limpar_texto(texto):
    """
    Limpa e normaliza o texto. Se encontrar 'Ã?' que não foi resolvido pelo dicionário,
    adiciona à lista de anomalias detectadas.
    """
    if not isinstance(texto, str):
        return texto
    
    if "Ã?" in texto:
        texto = texto.replace("Ã?Ã?ES", "COES")
        texto = texto.replace("Ã?Ã?O", "CAO")
        texto = texto.replace("Ã?Ã?", "CA")
        
        for corrompida, limpa in DICIONARIO_CORRUPCAO.items():
            texto = texto.replace(corrompida, limpa)
            
        texto = ud.unidecode(texto)
        
        # Se após o tratamento básico ainda sobrou o caracter corrompido '?' ou 'Ã' (isolado)
        # E se isso originou da falha do unidecode, o caracter '?' fica evidente
        # Na verdade, após unidecode, 'Ã?' vira 'A?'. 
        # Vamos verificar na string original:
    else:
        texto = ud.unidecode(ftfy.fix_text(texto))
        
    texto = " ".join(texto.split())
    return texto.upper()

def limpar_texto_com_tracking(texto_original):
    texto_limpo = limpar_texto(texto_original)
    
    # Detecção de anomalias
    if isinstance(texto_original, str) and "Ã?" in texto_original:
        # Verifica se alguma palavra corrompida original ainda tem vestígios 
        # Não podemos checar o texto_limpo diretamente porque o dicionário pode não ter coberto
        # Vamos extrair palavras originais com Ã? que não estão no dicionário
        for word in texto_original.split():
            if "Ã?" in word:
                # Trata sufixos genéricos
                w_temp = word.replace("Ã?Ã?ES", "COES").replace("Ã?Ã?O", "CAO").replace("Ã?Ã?", "CA")
                if "Ã?" in w_temp and word not in DICIONARIO_CORRUPCAO:
                    anomalias_detectadas.add(word)
                    
    return texto_limpo

def get_anomalias():
    return list(anomalias_detectadas)
