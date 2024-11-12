# menu_gui.py
import tkinter as tk
from tkinter import ttk

# Funções de manipulação de dados
from cliente import adicionar_cliente, listar_clientes
from montadora import adicionar_montadora, listar_montadoras
from operacao_compra import adicionar_compra, listar_compras
from operacao_venda import adicionar_venda, listar_vendas
from pedido import adicionar_pedido, listar_pedidos
from veiculo import adicionar_veiculo, listar_veiculos
from vendendor import adicionar_vendedor, listar_vendedores


class RedeSigmaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Rede Sigma")
        self.geometry("600x500")
        self.configure(bg="#f5f5f5")  # Cor de fundo clara
        self.create_widgets()

    def create_widgets(self):
        # Estilo personalizado
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TLabel", font=("Helvetica", 16), padding=10, background="#f5f5f5")

        # Título do Menu
        ttk.Label(self, text="Menu Principal", font=("Helvetica", 20, "bold"), foreground="#2e86de").pack(pady=20)

        # Botões do Menu
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)

        buttons = [
            ("Gerenciar Clientes", self.menu_clientes),
            ("Gerenciar Vendedores", self.menu_vendedores),
            ("Gerenciar Veículos", self.menu_veiculos),
            ("Operações de Compra", self.menu_compras),
            ("Operações de Venda", self.menu_vendas),
            ("Gerenciar Pedidos", self.menu_pedidos),
            ("Gerenciar Montadoras", self.menu_montadoras)
        ]

        for text, command in buttons:
            ttk.Button(button_frame, text=text, command=command, width=30).pack(pady=5)

        # Botão de Sair
        ttk.Button(self, text="Sair", command=self.quit, width=15, style="TButton").pack(pady=20)

    def open_submenu(self, title, fields, add_function, list_function):
        submenu = tk.Toplevel(self)
        submenu.title(title)
        submenu.geometry("450x400")
        submenu.configure(bg="#f5f5f5")

        ttk.Label(submenu, text=f"{title}", font=("Helvetica", 18, "bold"), foreground="#2e86de").pack(pady=20)

        form_frame = ttk.Frame(submenu)
        form_frame.pack(pady=10)

        entries = {}
        for field in fields:
            label = ttk.Label(form_frame, text=field + ":")
            label.grid(row=len(entries), column=0, padx=10, pady=5, sticky="e")
            entry = ttk.Entry(form_frame)
            entry.grid(row=len(entries), column=1, padx=10, pady=5)
            entries[field] = entry

        # Botões de Adicionar e Listar
        button_frame = ttk.Frame(submenu)
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text=f"Adicionar {title}", command=lambda: add_function(entries)).grid(row=0, column=0, padx=20)
        ttk.Button(button_frame, text=f"Listar {title}", command=lambda: self.list_data(submenu, list_function)).grid(row=0, column=1, padx=20)

    def list_data(self, parent, list_function):
        data = list_function()
        list_window = tk.Toplevel(parent)
        list_window.title("Listagem")
        list_window.geometry("400x300")

        text_area = tk.Text(list_window)
        text_area.pack(fill='both', padx=10, pady=10)

        for item in data:
            text_area.insert(tk.END, str(item) + "\n")

    def menu_clientes(self):
        fields = ["CPF", "Nome", "Renda"]
        self.open_submenu("Clientes", fields, adicionar_cliente, listar_clientes)

    def menu_vendedores(self):
        fields = ["Código", "Usuário"]
        self.open_submenu("Vendedores", fields, adicionar_vendedor, listar_vendedores)

    def menu_veiculos(self):
        fields = ["Marca", "Modelo", "Placa"]
        self.open_submenu("Veículos", fields, adicionar_veiculo, listar_veiculos)

    def menu_compras(self):
        fields = ["Número", "Cliente", "Veículo"]
        self.open_submenu("Compras", fields, adicionar_compra, listar_compras)

    def menu_vendas(self):
        fields = ["Número", "Cliente", "Veículo"]
        self.open_submenu("Vendas", fields, adicionar_venda, listar_vendas)

    def menu_pedidos(self):
        fields = ["Número", "Cliente", "Montadora"]
        self.open_submenu("Pedidos", fields, adicionar_pedido, listar_pedidos)

    def menu_montadoras(self):
        fields = ["CNPJ", "Marca", "Contato"]
        self.open_submenu("Montadoras", fields, adicionar_montadora, listar_montadoras)

if __name__ == "__main__":
    app = RedeSigmaApp()
    app.mainloop()
