# db_json.py
import json
import os

# Função para carregar os dados do banco de dados JSON
def load_data(filename):
    """Carrega os dados do arquivo JSON. Se não existir, retorna uma lista vazia."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

# Função para salvar dados no arquivo JSON
def save_data(filename, data):
    """Salva os dados no arquivo JSON."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Função para adicionar um item ao banco de dados JSON
def add_item(filename, item):
    data = load_data(filename)
    data.append(item)
    save_data(filename, data)

# Função para listar os itens do banco de dados JSON
def list_items(filename):
    return load_data(filename)

