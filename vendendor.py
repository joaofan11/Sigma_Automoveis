#Atualizado
from flask import Flask, request, render_template, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Conexão com o banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # Substitua pelo seu usuário
        password="sua_senha",  # Substitua pela sua senha
        database="rede_sigma"  # Substitua pelo nome do banco
    )

# Rota para listar vendedores
@app.route('/vendedores', methods=['GET'])
def listar_vendedores():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vendedores ORDER BY usuario")
    vendedores = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('vendedor.html', vendedores=vendedores)

# Rota para adicionar um vendedor
@app.route('/vendedores/adicionar', methods=['POST'])
def adicionar_vendedor():
    data = request.get_json()
    codigo = data['codigo']
    usuario = data['usuario']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO vendedores (codigo, usuario) VALUES (%s, %s)",
            (codigo, usuario)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Vendedor adicionado com sucesso!"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
