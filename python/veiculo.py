# veiculo.py
import json
from data_manager import salvar_dados, carregar_dados

veiculos = carregar_dados('veiculos.json')

class Veiculo:
    def __init__(self, chassi, placa, marca, modelo, ano_fabricacao, ano_modelo, cor, valor):
        self.chassi = chassi
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.ano_modelo = ano_modelo
        self.cor = cor
        self.valor = valor

def adicionar_veiculo():
    chassi = input("Digite o número do chassi: ")
    placa = input("Digite a placa: ")
    marca = input("Digite a marca: ")
    modelo = input("Digite o modelo: ")
    ano_fabricacao = input("Digite o ano de fabricação: ")
    ano_modelo = input("Digite o ano do modelo: ")
    cor = input("Digite a cor: ")
    valor = input("Digite o valor: ")

    veiculo = Veiculo(chassi, placa, marca, modelo, ano_fabricacao, ano_modelo, cor, valor)
    veiculos.append(veiculo.__dict__)
    salvar_dados('veiculos.json', veiculos)

def listar_veiculos():
    veiculos_ordenados = sorted(veiculos, key=lambda x: (x['marca'], x['modelo']))
    for veiculo in veiculos_ordenados:
        print(f"Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Placa: {veiculo['placa']}")
