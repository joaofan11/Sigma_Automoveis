# data_manager.py
import json

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
