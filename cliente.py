from flask import Flask, request, render_template, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",  # Seu usuário do MySQL
            password="sua_senha",  # Sua senha do MySQL
            database="rede_sigma"  # Nome do banco de dados
        )
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Rota para listar clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes ORDER BY nome")
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('07.Controle de Clientes.html', clientes=clientes)
    return jsonify({"message": "Erro ao conectar ao banco de dados."}), 500

# Rota para adicionar um cliente
@app.route('/clientes/adicionar', methods=['GET', 'POST'])
def adicionar_cliente():
    if request.method == 'POST':
        # Pegando os dados do formulário
        dados_cliente = {
            'cpf': request.form['cpf'],
            'nome': request.form['nome'],
            'endereco_bairro': request.form['endereco_bairro'],
            'endereco_cidade': request.form['endereco_cidade'],
            'endereco_estado': request.form['endereco_estado'],
            'telefone_residencial': request.form['telefone_residencial'],
            'celular': request.form['celular'],
            'renda': request.form['renda']
        }

        # Inserir o cliente no banco de dados
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO clientes (cpf, nome, endereco_bairro, endereco_cidade, endereco_estado, telefone_residencial, celular, renda)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (dados_cliente['cpf'], dados_cliente['nome'], dados_cliente['endereco_bairro'], 
                                   dados_cliente['endereco_cidade'], dados_cliente['endereco_estado'], 
                                   dados_cliente['telefone_residencial'], dados_cliente['celular'], 
                                   dados_cliente['renda']))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"message": "Cliente adicionado com sucesso!"}), 201
        return jsonify({"message": "Erro ao conectar ao banco de dados."}), 500

    return render_template('07.Controle de Clientes.html')

if __name__ == "__main__":
    app.run(debug=True)
