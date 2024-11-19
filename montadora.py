# montadora.py
#Atualizado
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'database': 'nome_do_banco'
}

# Conexão com o banco de dados
def conectar_db():
    return mysql.connector.connect(**db_config)

# Rota para listar todas as montadoras
@app.route('/montadoras', methods=['GET'])
def listar_montadoras():
    conn = conectar_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM montadoras")
    montadoras = cursor.fetchall()
    conn.close()
    return jsonify(montadoras)

# Rota para adicionar uma montadora
@app.route('/montadoras', methods=['POST'])
def adicionar_montadora():
    data = request.json
    conn = conectar_db()
    cursor = conn.cursor()
    query = """INSERT INTO montadoras (cnpj, razao_social, marca, contato, telefone_comercial, celular)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    valores = (data['cnpj'], data['razao_social'], data['marca'], data['contato'], data['telefone_comercial'], data['celular'])
    cursor.execute(query, valores)
    conn.commit()
    conn.close()
    return jsonify({"message": "Montadora adicionada com sucesso!"})

# Rota para editar uma montadora
@app.route('/montadoras/<int:id>', methods=['PUT'])
def editar_montadora(id):
    data = request.json
    conn = conectar_db()
    cursor = conn.cursor()
    query = """UPDATE montadoras
               SET cnpj = %s, razao_social = %s, marca = %s, contato = %s, telefone_comercial = %s, celular = %s
               WHERE id = %s"""
    valores = (data['cnpj'], data['razao_social'], data['marca'], data['contato'], data['telefone_comercial'], data['celular'], id)
    cursor.execute(query, valores)
    conn.commit()
    conn.close()
    return jsonify({"message": "Montadora atualizada com sucesso!"})

# Rota para excluir uma montadora
@app.route('/montadoras/<int:id>', methods=['DELETE'])
def excluir_montadora(id):
    conn = conectar_db()
    cursor = conn.cursor()
    query = "DELETE FROM montadoras WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Montadora excluída com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)

