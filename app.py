from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Função para carregar dados de um arquivo JSON
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

# Função para salvar dados no arquivo JSON
def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Rota para listar os itens (exemplo: clientes)
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = load_data('clientes.json')
    return jsonify(clientes)

# Rota para adicionar um cliente
@app.route('/clientes', methods=['POST'])
def adicionar_cliente():
    new_cliente = request.get_json()
    clientes = load_data('clientes.json')
    clientes.append(new_cliente)
    save_data('clientes.json', clientes)
    return jsonify({"message": "Cliente adicionado com sucesso!"}), 201

# Rota para listar vendedores
@app.route('/vendedores', methods=['GET'])
def listar_vendedores():
    vendedores = load_data('vendedores.json')
    return jsonify(vendedores)

# Rota para adicionar um vendedor
@app.route('/vendedores', methods=['POST'])
def adicionar_vendedor():
    new_vendedor = request.get_json()
    vendedores = load_data('vendedores.json')
    vendedores.append(new_vendedor)
    save_data('vendedores.json', vendedores)
    return jsonify({"message": "Vendedor adicionado com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
