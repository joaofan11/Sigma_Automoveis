import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco"
)

cursor = db.cursor()

# Função para conectar ao banco de dados
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="seu_banco"
    )

# Rota para adicionar um pedido
@app.route('/adicionar_pedido', methods=['POST'])
def adicionar_pedido():
    data = request.json
    try:
        db = conectar_db()
        cursor = db.cursor()
        query = """
            INSERT INTO pedidos (numero, data, cliente_id, vendedor_id, montadora_id, modelo, ano, cor, acessorios, valor)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            data['numero'], data['data'], data['cliente_id'], data['vendedor_id'],
            data['montadora_id'], data['modelo'], data['ano'], data['cor'],
            data['acessorios'], data['valor']
        )
        cursor.execute(query, valores)
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"message": "Pedido adicionado com sucesso!"})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})

# Rota para listar pedidos
@app.route('/listar_pedidos', methods=['GET'])
def listar_pedidos():
    try:
        db = conectar_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pedidos")
        resultados = cursor.fetchall()
        pedidos = [
            {
                "id": linha[0],
                "numero": linha[1],
                "data": linha[2],
                "cliente_id": linha[3],
                "vendedor_id": linha[4],
                "montadora_id": linha[5],
                "modelo": linha[6],
                "ano": linha[7],
                "cor": linha[8],
                "acessorios": linha[9],
                "valor": linha[10]
            } for linha in resultados
        ]
        cursor.close()
        db.close()
        return jsonify(pedidos)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})

# Rota para excluir um pedido
@app.route('/excluir_pedido/<int:id>', methods=['DELETE'])
def excluir_pedido(id):
    try:
        db = conectar_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM pedidos WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"message": "Pedido excluído com sucesso!"})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})

if __name__ == '__main__':
    app.run(debug=True)
