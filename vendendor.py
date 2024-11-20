#pagina vendendor.py
from flask import Flask, request, render_template, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Função para obter a conexão com o banco de dados
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # Substitua pelo seu usuário
            password="sua_senha",  # Substitua pela sua senha
            database="rede_sigma"  # Substitua pelo nome do banco
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para executar consultas e retornar resultados
def executar_consulta(query, params=None, fetchall=True):
    conn = get_db_connection()
    if conn is None:
        return None
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(query, params or ())
            if fetchall:
                return cursor.fetchall()
            else:
                conn.commit()
    except Error as e:
        print(f"Erro na consulta: {e}")
        return None
    finally:
        conn.close()

# Rota para listar vendedores
@app.route('/vendedores', methods=['GET'])
def listar_vendedores():
    vendedores = executar_consulta("SELECT * FROM vendedores ORDER BY usuario")
    if vendedores is None:
        return jsonify({"error": "Não foi possível recuperar os vendedores."}), 500
    return render_template('vendedor.html', vendedores=vendedores)

# Rota para adicionar um vendedor
@app.route('/vendedores/adicionar', methods=['POST'])
def adicionar_vendedor():
    data = request.get_json()
    codigo = data['codigo']
    usuario = data['usuario']

    query = "INSERT INTO vendedores (codigo, usuario) VALUES (%s, %s)"
    params = (codigo, usuario)
    
    if executar_consulta(query, params, fetchall=False) is not None:
        return jsonify({"message": "Vendedor adicionado com sucesso!"}), 201
    else:
        return jsonify({"error": "Erro ao adicionar vendedor."}), 400

if __name__ == '__main__':
    app.run(debug=True)
