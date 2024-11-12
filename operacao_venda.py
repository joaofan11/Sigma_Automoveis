# operacao_venda.py
import json
from data_manager import salvar_dados, carregar_dados

vendas = carregar_dados('vendas.json')

class OperacaoVenda:
    def __init__(self, numero, data, cliente, vendedor, veiculo, valor_entrada, valor_financiado, valor_total):
        self.numero = numero
        self.data = data
        self.cliente = cliente
        self.vendedor = vendedor
        self.veiculo = veiculo
        self.valor_entrada = valor_entrada
        self.valor_financiado = valor_financiado
        self.valor_total = valor_total

def adicionar_venda():
    numero = input("Digite o número da operação: ")
    data = input("Digite a data: ")
    cliente = input("Digite o nome do cliente: ")
    vendedor = input("Digite o nome do vendedor: ")
    veiculo = input("Digite a placa do veículo: ")
    valor_entrada = input("Digite o valor de entrada: ")
    valor_financiado = input("Digite o valor financiado: ")
    valor_total = input(f"Digite o valor total: ")

    venda = OperacaoVenda(numero, data, cliente, vendedor, veiculo, valor_entrada, valor_financiado, valor_total)
    vendas.append(venda.__dict__)
    salvar_dados('vendas.json', vendas)

def listar_vendas():
    for venda in vendas:
        print(f"Número: {venda['numero']}, Cliente: {venda['cliente']}, Veículo: {venda['veiculo']}")
