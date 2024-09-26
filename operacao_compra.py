# operacao_compra.py
import json
from data_manager import salvar_dados, carregar_dados

compras = carregar_dados('compras.json')

class OperacaoCompra:
    def __init__(self, numero, data, cliente, vendedor, veiculo, valor):
        self.numero = numero
        self.data = data
        self.cliente = cliente
        self.vendedor = vendedor
        self.veiculo = veiculo
        self.valor = valor

def adicionar_compra():
    numero = input("Digite o número da operação: ")
    data = input("Digite a data: ")
    cliente = input("Digite o nome do cliente: ")
    vendedor = input("Digite o nome do vendedor: ")
    veiculo = input("Digite a placa do veículo: ")
    valor = input("Digite o valor da compra: ")

    compra = OperacaoCompra(numero, data, cliente, vendedor, veiculo, valor)
    compras.append(compra.__dict__)
    salvar_dados('compras.json', compras)

def listar_compras():
    for compra in compras:
        print(f"Número: {compra['numero']}, Cliente: {compra['cliente']}, Veículo: {compra['veiculo']}")
