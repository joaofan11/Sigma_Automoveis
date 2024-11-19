#mudei
from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'senha',
    'database': 'sistema_vendas'
}

# Conexão com o banco
def conectar_banco():
    return mysql.connector.connect(**db_config)

# Rota principal para exibir o HTML
@app.route('/')
def index():
    return render_template('operacao_venda.html')

# Rota para listar as vendas
@app.route('/vendas', methods=['GET'])
def listar_vendas():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM operacoes_venda")
    vendas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(vendas)

# Rota para adicionar uma nova venda
@app.route('/vendas', methods=['POST'])
def adicionar_venda():
    dados = request.json
    conexao = conectar_banco()
    cursor = conexao.cursor()
    query = """
        INSERT INTO operacoes_venda (numero, data, cliente_id, vendedor_id, veiculo_id, valor_entrada, valor_financiado, valor_total)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        dados['numero'],
        dados['data'],
        dados['cliente_id'],
        dados['vendedor_id'],
        dados['veiculo_id'],
        dados['valor_entrada'],
        dados['valor_financiado'],
        dados['valor_total']
    )
    cursor.execute(query, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({'status': 'Venda adicionada com sucesso'})

# Rota para editar uma venda existente
@app.route('/vendas/<int:id>', methods=['PUT'])
def editar_venda(id):
    dados = request.json
    conexao = conectar_banco()
    cursor = conexao.cursor()
    query = """
        UPDATE operacoes_venda
        SET numero = %s, data = %s, cliente_id = %s, vendedor_id = %s, veiculo_id = %s, 
            valor_entrada = %s, valor_financiado = %s, valor_total = %s
        WHERE id = %s
    """
    valores = (
        dados['numero'],
        dados['data'],
        dados['cliente_id'],
        dados['vendedor_id'],
        dados['veiculo_id'],
        dados['valor_entrada'],
        dados['valor_financiado'],
        dados['valor_total'],
        id
    )
    cursor.execute(query, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({'status': 'Venda editada com sucesso'})

# Rota para excluir uma venda
@app.route('/vendas/<int:id>', methods=['DELETE'])
def excluir_venda(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    query = "DELETE FROM operacoes_venda WHERE id = %s"
    cursor.execute(query, (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({'status': 'Venda excluída com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
