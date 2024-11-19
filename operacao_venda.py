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

# Função para conectar ao banco e garantir o fechamento automático
def conectar_banco():
    return mysql.connector.connect(**db_config)

# Função para executar uma consulta no banco de dados
def executar_query(query, valores=None, fetch=False):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(query, valores)
    if fetch:
        resultado = cursor.fetchall()
    else:
        conexao.commit()
        resultado = None
    cursor.close()
    conexao.close()
    return resultado

# Rota principal para exibir o HTML
@app.route('/')
def index():
    return render_template('operacao_venda.html')

# Rota para listar as vendas
@app.route('/vendas', methods=['GET'])
def listar_vendas():
    query = "SELECT * FROM operacoes_venda"
    vendas = executar_query(query, fetch=True)
    return jsonify(vendas)

# Rota para adicionar uma nova venda
@app.route('/vendas', methods=['POST'])
def adicionar_venda():
    dados = request.json
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
    executar_query(query, valores)
    return jsonify({'status': 'Venda adicionada com sucesso'})

# Rota para editar uma venda existente
@app.route('/vendas/<int:id>', methods=['PUT'])
def editar_venda(id):
    dados = request.json
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
    executar_query(query, valores)
    return jsonify({'status': 'Venda editada com sucesso'})

# Rota para excluir uma venda
@app.route('/vendas/<int:id>', methods=['DELETE'])
def excluir_venda(id):
    query = "DELETE FROM operacoes_venda WHERE id = %s"
    executar_query(query, (id,))
    return jsonify({'status': 'Venda excluída com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
