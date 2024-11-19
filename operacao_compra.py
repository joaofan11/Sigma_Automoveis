#MUDEI
from flask import Flask, request, jsonify, render_template
import MySQLdb

app = Flask(__name__)

# Configuração do banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'seu_usuario'
app.config['MYSQL_PASSWORD'] = 'sua_senha'
app.config['MYSQL_DB'] = 'seu_banco'

mysql = MySQLdb.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    passwd=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

@app.route('/')
def index():
    return render_template('index.html')  # Seu HTML principal

@app.route('/compras', methods=['GET', 'POST'])
def compras():
    cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        dados = request.get_json()
        query = """
            INSERT INTO operacoes_compra (numero, data, cliente_id, vendedor_id, veiculo_id, valor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            dados['numero'],
            dados['data'],
            dados['cliente_id'],
            dados['vendedor_id'],
            dados['veiculo_id'],
            dados['valor']
        ))
        mysql.commit()
        return jsonify({'message': 'Compra registrada com sucesso!'})
    
    elif request.method == 'GET':
        cursor.execute("SELECT * FROM operacoes_compra")
        compras = cursor.fetchall()
        return jsonify(compras)

@app.route('/compras/<int:id>', methods=['PUT', 'DELETE'])
def atualizar_ou_excluir(id):
    cursor = mysql.cursor()
    if request.method == 'PUT':
        dados = request.get_json()
        query = """
            UPDATE operacoes_compra
            SET numero=%s, data=%s, cliente_id=%s, vendedor_id=%s, veiculo_id=%s, valor=%s
            WHERE id=%s
        """
        cursor.execute(query, (
            dados['numero'],
            dados['data'],
            dados['cliente_id'],
            dados['vendedor_id'],
            dados['veiculo_id'],
            dados['valor'],
            id
        ))
        mysql.commit()
        return jsonify({'message': 'Compra atualizada com sucesso!'})
    
    elif request.method == 'DELETE':
        cursor.execute("DELETE FROM operacoes_compra WHERE id=%s", (id,))
        mysql.commit()
        return jsonify({'message': 'Compra excluída com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)