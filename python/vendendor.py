# vendedor.py
import json
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
