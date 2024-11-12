from flask import Flask, render_template, request, jsonify
from data_manager import carregar_dados, salvar_dados

app = Flask(__name__)

# Rotas para clientes
@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    clientes = carregar_dados('clientes.json')
    if request.method == 'POST':
        novo_cliente = request.json
        clientes.append(novo_cliente)
        salvar_dados('clientes.json', clientes)
        return jsonify({"message": "Cliente adicionado com sucesso!"}), 201
    return jsonify(clientes), 200

# Rotas para montadoras
@app.route('/montadoras', methods=['GET', 'POST'])
def montadoras():
    montadoras = carregar_dados('montadoras.json')
    if request.method == 'POST':
        nova_montadora = request.json
        montadoras.append(nova_montadora)
        salvar_dados('montadoras.json', montadoras)
        return jsonify({"message": "Montadora adicionada com sucesso!"}), 201
    return jsonify(montadoras), 200

# Outras rotas para veiculos, compras, vendas, etc.

if __name__ == "__main__":
    app.run(debug=True)
