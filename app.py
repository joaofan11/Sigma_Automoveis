#mudei
import mysql.connector
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Função para conectar ao banco de dados MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Seu usuário do MySQL
        password="sua_senha",  # Sua senha do MySQL
        database="rede_sigma"  # Nome do banco de dados
    )


@app.route('/')
def index():
    return render_template('index.html')

# Rotas para clientes
@app.route('/clientes')
def clientes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT nome, cpf FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(clientes)


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
