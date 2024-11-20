#pagina montadora.py
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'database': 'nome_do_banco'
}

# Função para criar uma conexão com o banco de dados
def conectar_db():
    try:
        return mysql.connector.connect(**db_config)
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para fechar a conexão com o banco de dados
def fechar_conexao(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

# Rota para listar todas as montadoras
@app.route('/montadoras', methods=['GET'])
def listar_montadoras():
    conn = conectar_db()
    if not conn:
        return jsonify({"message": "Erro ao conectar com o banco de dados"}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM montadoras")
    montadoras = cursor.fetchall()
    fechar_conexao(conn, cursor)
    
    return jsonify(montadoras)

# Rota para adicionar uma montadora
@app.route('/montadoras', methods=['POST'])
def adicionar_montadora():
    data = request.json
    conn = conectar_db()
    if not conn:
        return jsonify({"message": "Erro ao conectar com o banco de dados"}), 500

    cursor = conn.cursor()
    query = """INSERT INTO montadoras (cnpj, razao_social, marca, contato, telefone_comercial, celular)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    valores = (data['cnpj'], data['razao_social'], data['marca'], data['contato'], data['telefone_comercial'], data['celular'])
    
    try:
        cursor.execute(query, valores)
        conn.commit()
        return jsonify({"message": "Montadora adicionada com sucesso!"}), 201
    except Error as e:
        return jsonify({"message": f"Erro ao adicionar montadora: {e}"}), 500
    finally:
        fechar_conexao(conn, cursor)

# Rota para editar uma montadora
@app.route('/montadoras/<int:id>', methods=['PUT'])
def editar_montadora(id):
    data = request.json
    conn = conectar_db()
    if not conn:
        return jsonify({"message": "Erro ao conectar com o banco de dados"}), 500

    cursor = conn.cursor()
    query = """UPDATE montadoras
               SET cnpj = %s, razao_social = %s, marca = %s, contato = %s, telefone_comercial = %s, celular = %s
               WHERE id = %s"""
    valores = (data['cnpj'], data['razao_social'], data['marca'], data['contato'], data['telefone_comercial'], data['celular'], id)
    
    try:
        cursor.execute(query, valores)
        conn.commit()
        return jsonify({"message": "Montadora atualizada com sucesso!"})
    except Error as e:
        return jsonify({"message": f"Erro ao atualizar montadora: {e}"}), 500
    finally:
        fechar_conexao(conn, cursor)

# Rota para excluir uma montadora
@app.route('/montadoras/<int:id>', methods=['DELETE'])
def excluir_montadora(id):
    conn = conectar_db()
    if not conn:
        return jsonify({"message": "Erro ao conectar com o banco de dados"}), 500

    cursor = conn.cursor()
    query = "DELETE FROM montadoras WHERE id = %s"
    
    try:
        cursor.execute(query, (id,))
        conn.commit()
        return jsonify({"message": "Montadora excluída com sucesso!"})
    except Error as e:
        return jsonify({"message": f"Erro ao excluir montadora: {e}"}), 500
    finally:
        fechar_conexao(conn, cursor)

if __name__ == '__main__':
    app.run(debug=True)

