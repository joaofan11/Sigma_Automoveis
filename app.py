from dotenv import load_dotenv
import os
import mysql.connector
from flask import Flask, request, jsonify, render_template
from datetime import datetime
import logging

# Carregar as variáveis do arquivo .env
load_dotenv()

# Configuração de logging para captura de erros
logging.basicConfig(level=logging.INFO)

# Função para obter a conexão com o banco de dados
def get_db_connection():
    """Função para obter uma nova conexão com o banco de dados"""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "sua_senha"),
        database=os.getenv("DB_NAME", "rede_sigma")
    )

# Funções de validação
def validar_data(data):
    """Valida uma data no formato DD-MM-YYYY"""
    try:
        datetime.strptime(data, "%d-%m-%Y")
        return True
    except ValueError:
        return False

# Função genérica para executar uma consulta no banco de dados
def execute_query(query, values=None, fetch=False):
    """Executa uma consulta no banco de dados e retorna o resultado"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, values)
        if fetch:
            return cursor.fetchall()
        conn.commit()
    except mysql.connector.Error as e:
        logging.error(f"Erro de banco de dados: {str(e)}")
        return f"Erro de banco de dados: {str(e)}"
    finally:
        cursor.close()
        conn.close()

# Função genérica para adicionar um recurso no banco de dados
def add_resource(resource_type, query, values):
    """Função genérica para adicionar recursos (clientes, montadoras, etc.)"""
    result = execute_query(query, values)
    if isinstance(result, str):  # Erro ao executar consulta
        return jsonify({"error": result}), 500
    return jsonify({"message": f"{resource_type} criado com sucesso!"}), 201

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Rota para listar e adicionar clientes
@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':  # Adicionar cliente
        data = request.json
        query = """INSERT INTO clientes (cpf, nome, endereco_bairro, endereco_cidade, endereco_estado, 
                  telefone_residencial, celular, renda) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (data['cpf'], data['nome'], data.get('endereco_bairro'), data.get('endereco_cidade'),
                   data.get('endereco_estado'), data.get('telefone_residencial'), data.get('celular'), data.get('renda'))
        return add_resource('Cliente', query, valores)

    # Requisição GET para listar todos os clientes
    clientes = execute_query("SELECT * FROM clientes", fetch=True)
    return jsonify(clientes), 200

# Rota para editar ou excluir cliente
@app.route('/clientes/<int:id>', methods=['PUT', 'DELETE'])
def editar_excluir_cliente(id):
    data = request.json
    if request.method == 'PUT':  # Editar cliente
        query = """UPDATE clientes SET cpf = %s, nome = %s, endereco_bairro = %s, endereco_cidade = %s, 
                   endereco_estado = %s, telefone_residencial = %s, celular = %s, renda = %s WHERE id = %s"""
        valores = (data['cpf'], data['nome'], data.get('endereco_bairro'), data.get('endereco_cidade'),
                   data.get('endereco_estado'), data.get('telefone_residencial'), data.get('celular'), data.get('renda'), id)
        result = execute_query(query, valores)
        return jsonify({"message": "Cliente atualizado com sucesso!"}) if not isinstance(result, str) else jsonify({"error": result}), 500

    elif request.method == 'DELETE':  # Excluir cliente
        query = "DELETE FROM clientes WHERE id = %s"
        result = execute_query(query, (id,))
        return jsonify({"message": "Cliente excluído com sucesso!"}) if not isinstance(result, str) else jsonify({"error": result}), 500

# Rota para listar e adicionar montadoras
@app.route('/montadoras', methods=['GET', 'POST'])
def montadoras():
    if request.method == 'POST':  # Adicionar montadora
        data = request.json
        query = """INSERT INTO montadoras (cnpj, razao_social, marca, contato, telefone_comercial, celular)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (data['cnpj'], data['razao_social'], data['marca'], data['contato'],
                   data['telefone_comercial'], data['celular'])
        return add_resource('Montadora', query, valores)

    # Requisição GET para listar todas as montadoras
    montadoras = execute_query("SELECT * FROM montadoras", fetch=True)
    return jsonify(montadoras), 200

# Rota para editar ou excluir montadora
@app.route('/montadoras/<int:id>', methods=['PUT', 'DELETE'])
def editar_excluir_montadora(id):
    data = request.json
    if request.method == 'PUT':  # Editar montadora
        query = """UPDATE montadoras SET cnpj = %s, razao_social = %s, marca = %s, contato = %s, 
                   telefone_comercial = %s, celular = %s WHERE id = %s"""
        valores = (data['cnpj'], data['razao_social'], data['marca'], data['contato'],
                   data['telefone_comercial'], data['celular'], id)
        result = execute_query(query, valores)
        return jsonify({"message": "Montadora atualizada com sucesso!"}) if not isinstance(result, str) else jsonify({"error": result}), 500

    elif request.method == 'DELETE':  # Excluir montadora
        query = "DELETE FROM montadoras WHERE id = %s"
        result = execute_query(query, (id,))
        return jsonify({"message": "Montadora excluída com sucesso!"}) if not isinstance(result, str) else jsonify({"error": result}), 500

# Rota para adicionar um pedido
@app.route('/adicionar_pedido', methods=['POST'])
def adicionar_pedido():
    data = request.json

    # Validação de Data
    if not validar_data(data.get('data', '')):  
        return jsonify({"error": "Data inválida!"}), 400

    query = """
        INSERT INTO pedidos (numero, data, cliente_id, vendedor_id, montadora_id, modelo, ano, cor, acessorios, valor)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        data['numero'], data['data'], data['cliente_id'], data['vendedor_id'],
        data['montadora_id'], data['modelo'], data['ano'], data['cor'],
        data['acessorios'], data['valor']
    )
    return add_resource('Pedido', query, valores)

# Rota para listar e adicionar veículos
@app.route("/veiculos", methods=["GET", "POST"])
def veiculos():
    if request.method == 'POST':  # Adicionar veículo
        data = request.json
        query = """INSERT INTO veiculos (numero_chassi, placa, marca, modelo, ano_fabricacao, ano_modelo, cor, valor)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (data["chassi"], data["placa"], data["marca"], data["modelo"], data["anoFabricacao"],
                   data["anoModelo"], data["cor"], data["valor"])
        execute_query(query, valores)
        return jsonify({"message": "Veículo adicionado com sucesso!"}), 201

    # Requisição GET para listar todos os veículos
    veiculos = execute_query("SELECT * FROM veiculos ORDER BY marca, modelo", fetch=True)
    return jsonify(veiculos)

# Rota para excluir um veículo
@app.route("/veiculos/<int:id>", methods=["DELETE"])
def excluir_veiculo(id):
    query = "DELETE FROM veiculos WHERE id = %s"
    execute_query(query, (id,))
    return jsonify({"message": "Veículo excluído com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
