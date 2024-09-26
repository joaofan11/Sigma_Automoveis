from clientes import Clientes
from vendedores import Vendedores
from veiculos import Veiculos
from operacoes import Operacoes
from pedidos import Pedidos
from montadoras import Montadoras

def menu():
    while True:
        print("\nREDE SIGMA DE AUTOMÓVEIS")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Vendedores")
        print("3. Gerenciar Veículos")
        print("4. Operações de Compra e Venda")
        print("5. Pedidos às Montadoras")
        print("6. Gerenciar Montadoras")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            Clientes.menu()
        elif opcao == '2':
            Vendedores.menu()
        elif opcao == '3':
            Veiculos.menu()
        elif opcao == '4':
            Operacoes.menu()
        elif opcao == '5':
            Pedidos.menu()
        elif opcao == '6':
            Montadoras.menu()
        elif opcao == '7':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def gerenciar_clientes():
    print("Funcionalidade de gerenciamento de clientes.")

def gerenciar_vendedores():
    print("Funcionalidade de gerenciamento de vendedores.")

def gerenciar_veiculos():
    print("Funcionalidade de gerenciamento de veículos.")

def operacoes_compra_venda():
    print("Funcionalidade de operações de compra e venda.")

def pedidos_montadoras():
    print("Funcionalidade de pedidos às montadoras.")

def gerenciar_montadoras():
    print("Funcionalidade de gerenciamento de montadoras.")

if __name__ == "__main__":
    menu()
