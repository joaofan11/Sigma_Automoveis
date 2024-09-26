# pedido.py
import json
from data_manager import salvar_dados, carregar_dados

pedidos = carregar_dados('pedidos.json')

class Pedido:
    def __init__(self, numero, data, cliente, vendedor, montadora, modelo, ano, cor, acessorios, valor):
        self.numero = numero
        self.data = data
        self.cliente = cliente
        self.vendedor = vendedor
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.acessorios = acessorios
        self.valor = valor

def adicionar_pedido():
    numero = input("Digite o número do pedido: ")
    data = input("Digite a data: ")
    cliente = input("Digite o nome do cliente: ")
    vendedor = input("Digite o nome do vendedor: ")
    montadora = input("Digite o nome da montadora: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano do veículo: ")
    cor = input("Digite a cor: ")
    acessorios = input("Digite os acessórios: ")
    valor = input("Digite o valor: ")

    pedido = Pedido(numero, data, cliente, vendedor, montadora, modelo, ano, cor, acessorios, valor)
    pedidos.append(pedido.__dict__)
    salvar_dados('pedidos.json', pedidos)

def listar_pedidos():
    for pedido in pedidos:
        print(f"Número: {pedido['numero']}, Cliente: {pedido['cliente']}, Montadora: {pedido['montadora']}")
