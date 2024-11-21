# vendedor.py
import json
from db_json import add_item, list_items
from data_manager import salvar_dados, carregar_dados

vendedores = carregar_dados('vendedores.json')

class Vendedor:
    def __init__(self, codigo, usuario):
        self.codigo = codigo
        self.usuario = usuario

def adicionar_vendedor():
    codigo = input("Digite o código do vendedor: ")
    usuario = input("Digite o nome de usuário do vendedor: ")

    vendedor = Vendedor(codigo, usuario)
    vendedores.append(vendedor.__dict__)
    salvar_dados('vendedores.json', vendedores)

def listar_vendedores():
    for vendedor in vendedores:
        print(f"Código: {vendedor['codigo']}, Usuário: {vendedor['usuario']}")


# Função para adicionar um vendedor
def adicionar_vendedor(entries):
    vendedor = {
        "codigo": entries["Código"].get(),
        "usuario": entries["Usuário"].get()
    }
    add_item("vendedores.json", vendedor)

# Função para listar os vendedores
def listar_vendedores():
    return list_items("vendedores.json")
