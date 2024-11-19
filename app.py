from flask import Flask, request, jsonify, render_template
import mysql.connector

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

# Rota para clientes (GET, POST, PUT, DELETE)
@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':  # Adicionar cliente
        data = request.json
        query = """INSERT INTO clientes (cpf, nome, endereco_bairro, endereco_cidade, endereco_estado, 
                  telefone_residencial, celular, renda) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (data['cpf'], data['nome'], data.get('endereco_bairro'), data.get('endereco_cidade'),
                   data.get('endereco_estado'), data.get('telefone_residencial'), data.get('celular'), data.get('renda'))
        cursor.execute(query, valores)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Cliente adicionado com sucesso!"}), 201

    # Requisição GET para listar todos os clientes
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(clientes), 200

# Rota para editar ou excluir cliente (usando PUT ou DELETE)
@app.route('/clientes/<int:id>', methods=['PUT', 'DELETE'])
def editar_excluir_cliente(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'PUT':  # Editar cliente
        data = request.json
        query = """UPDATE clientes SET cpf = %s, nome = %s, endereco_bairro = %s, endereco_cidade = %s, 
                   endereco_estado = %s, telefone_residencial = %s, celular = %s, renda = %s WHERE id = %s"""
        valores = (data['cpf'], data['nome'], data.get('endereco_bairro'), data.get('endereco_cidade'),
                   data.get('endereco_estado'), data.get('telefone_residencial'), data.get('celular'), data.get('renda'), id)
        cursor.execute(query, valores)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Cliente atualizado com sucesso!"})

    elif request.method == 'DELETE':  # Excluir cliente
        query = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Cliente excluído com sucesso!"})

# Rota para listar e adicionar montadoras (GET, POST)
@app.route('/montadoras', methods=['GET', 'POST'])
def montadoras():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':  # Adicionar montadora
        data = request.json
        query = """INSERT INTO montadoras (cnpj, razao_social, marca, contato, telefone_comercial, celular)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (data['cnpj'], data['razao_social'], data['marca'], data['contato'],
                   data['telefone_comercial'], data['celular'])
        cursor.execute(query, valores)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Montadora adicionada com sucesso!"}), 201

    # Requisição GET para listar todas as montadoras
    cursor.execute("SELECT * FROM montadoras")
    montadoras = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(montadoras), 200

# Rota para editar ou excluir montadora (usando PUT ou DELETE)
@app.route('/montadoras/<int:id>', methods=['PUT', 'DELETE'])
def editar_excluir_montadora(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'PUT':  # Editar montadora
        data = request.json
        query = """UPDATE montadoras SET cnpj = %s, razao_social = %s, marca = %s, contato = %s, 
                   telefone_comercial = %s, celular = %s WHERE id = %s"""
        valores = (data['cnpj'], data['razao_social'], data['marca'], data['contato'],
                   data['telefone_comercial'], data['celular'], id)
        cursor.execute(query, valores)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Montadora atualizada com sucesso!"})

    elif request.method == 'DELETE':  # Excluir montadora
        query = "DELETE FROM montadoras WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Montadora excluída com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
