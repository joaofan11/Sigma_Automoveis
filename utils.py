# utils.py
import re

def validar_cpf(cpf):
    # Implementar validação de CPF
    return re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf) is not None

def validar_data(data):
    # Implementar validação de data
    return re.match(r'^\d{2}/\d{2}/\d{4}$', data) is not None
