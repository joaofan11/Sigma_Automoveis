# app.py
from flask import Flask, request, render_template, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Seu usuário do MySQL
        password="sua_senha",  # Sua senha do MySQL
        database="rede_sigma"  # Nome do banco de dados
    )

# Rota para listar clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes ORDER BY nome")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('07.Controle de Clientes.html', clientes=clientes)

# Rota para adicionar um cliente
@app.route('/clientes/adicionar', methods=['GET', 'POST'])
def adicionar_cliente():
    if request.method == 'POST':
        cpf = request.form['cpf']
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone_residencial = request.form['telefone_residencial']
        celular = request.form['celular']
        renda = request.form['renda']

        # Inserir o cliente no banco de dados
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clientes (cpf, nome, endereco_bairro, endereco_cidade, endereco_estado, telefone_residencial, celular, renda)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (cpf, nome, *endereco.split(','), telefone_residencial, celular, renda))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Cliente adicionado com sucesso!"}), 201
    return render_template('07.Controle de Clientes.html')

if __name__ == "__main__":
    app.run(debug=True)

