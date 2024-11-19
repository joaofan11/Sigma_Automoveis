#mudei
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

# Rota para adicionar um pedido
@app.route('/adicionar_pedido', methods=['POST'])
def adicionar_pedido():
    data = request.json
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
    return jsonify({"message": "Pedido adicionado com sucesso!"})

# Rota para listar pedidos
@app.route('/listar_pedidos', methods=['GET'])
def listar_pedidos():
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
    return jsonify(pedidos)

# Rota para excluir um pedido
@app.route('/excluir_pedido/<int:id>', methods=['DELETE'])
def excluir_pedido(id):
    cursor.execute("DELETE FROM pedidos WHERE id = %s", (id,))
    db.commit()
    return jsonify({"message": "Pedido excluído com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
