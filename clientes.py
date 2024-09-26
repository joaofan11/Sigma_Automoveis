import utils

class Clientes:
    arquivo = 'database/clientes.txt'

    @staticmethod
    def menu():
        while True:
            print("\n[Clientes] Escolha uma opção:")
            print("1. Cadastrar Cliente")
            print("2. Listar Clientes")
            print("3. Buscar Cliente")
            print("4. Excluir Cliente")
            print("5. Voltar ao Menu Principal")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                Clientes.cadastrar()
            elif opcao == '2':
                Clientes.listar()
            elif opcao == '3':
                Clientes.buscar()
            elif opcao == '4':
                Clientes.excluir()
            elif opcao == '5':
                break
            else:
                print("Opção inválida!")

    @staticmethod
    def cadastrar():
        cpf = input("Digite o CPF do cliente: ")
        if not utils.validar_cpf(cpf):
            print("CPF inválido!")
            return
        nome = input("Digite o nome: ")
        endereco = input("Digite o endereço (Bairro, Cidade, Estado): ")
        telefone = input("Digite o telefone: ")
        celular = input("Digite o celular: ")
        renda = input("Digite a renda: ")

        with open(Clientes.arquivo, "a") as file:
            file.write(f"{cpf};{nome};{endereco};{telefone};{celular};{renda}\n")
        print("Cliente cadastrado com sucesso!")

    @staticmethod
    def listar():
        print("\nLista de Clientes:")
        with open(Clientes.arquivo, "r") as file:
            for line in file:
                print(line.strip())

    @staticmethod
    def buscar():
        cpf = input("Digite o CPF do cliente: ")
        with open(Clientes.arquivo, "r") as file:
            for line in file:
                if cpf in line:
                    print(f"Cliente encontrado: {line.strip()}")
                    return
        print("Cliente não encontrado.")

    @staticmethod
    def excluir():
        cpf = input("Digite o CPF do cliente a ser excluído: ")
        linhas = []
        with open(Clientes.arquivo, "r") as file:
            linhas = file.readlines()

        with open(Clientes.arquivo, "w") as file:
            for linha in linhas:
                if cpf not in linha:
                    file.write(linha)
        print("Cliente excluído com sucesso!")
