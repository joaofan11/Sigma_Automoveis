def validar_cpf(cpf):
    # Implementar a validação de CPF aqui
    return True

def carregar_dados(arquivo):
    dados = []
    try:
        with open(arquivo, 'r') as file:
            for linha in file:
                dados.append(linha.strip().split(';'))
    except FileNotFoundError:
        pass  # Se o arquivo não existir, retorna uma lista vazia
    return dados
