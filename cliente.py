# cliente.py
import json
from data_manager import salvar_dados, carregar_dados

clientes = carregar_dados('clientes.json')

class Cliente:
    def __init__(self, cpf, nome, endereco, telefone_residencial, celular, renda):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.telefone_residencial = telefone_residencial
        self.celular = celular
        self.renda = renda

def adicionar_cliente():
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    endereco = input("Digite o endereço (bairro, cidade, estado): ")
    telefone_residencial = input("Digite o telefone residencial: ")
    celular = input("Digite o celular: ")
    renda = input("Digite a renda: ")

    cliente = Cliente(cpf, nome, endereco, telefone_residencial, celular, renda)
    clientes.append(cliente.__dict__)
    salvar_dados('clientes.json', clientes)

def listar_clientes():
    clientes_ordenados = sorted(clientes, key=lambda x: x['nome'])
    for cliente in clientes_ordenados:
        print(f"CPF: {cliente['cpf']}, Nome: {cliente['nome']}, Renda: {cliente['renda']}")
