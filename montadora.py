# montadora.py
import json
from data_manager import salvar_dados, carregar_dados
from db_json import add_item, list_items

# Função para adicionar uma montadora
def adicionar_montadora(entries):
    montadora = {
        "cnpj": entries["CNPJ"].get(),
        "marca": entries["Marca"].get(),
        "contato": entries["Contato"].get()
    }
    add_item("montadoras.json", montadora)

# Função para listar as montadoras
def listar_montadoras():
    return list_items("montadoras.json")


montadoras = carregar_dados('montadoras.json')

class Montadora:
    def __init__(self, cnpj, razao_social, marca, contato, telefone_comercial, celular):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.marca = marca
        self.contato = contato
        self.telefone_comercial = telefone_comercial
        self.celular = celular

def adicionar_montadora():
    cnpj = input("Digite o CNPJ: ")
    razao_social = input("Digite a razão social: ")
    marca = input("Digite a marca: ")
    contato = input("Digite o nome do contato: ")
    telefone_comercial = input("Digite o telefone comercial: ")
    celular = input("Digite o celular: ")

    montadora = Montadora(cnpj, razao_social, marca, contato, telefone_comercial, celular)
    montadoras.append(montadora.__dict__)
    salvar_dados('montadoras.json', montadoras)

def listar_montadoras():
    for montadora in montadoras:
        print(f"CNPJ: {montadora['cnpj']}, Marca: {montadora['marca']}, Contato: {montadora['contato']}")
