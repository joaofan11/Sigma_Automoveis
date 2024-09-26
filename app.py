from flask import Flask, render_template, request, redirect, url_for
import utils  # Arquivo de validações e utilitários

app = Flask(__name__)

# Caminhos para os arquivos de dados
CLIENTES_FILE = 'database/clientes.txt'
VENDEDORES_FILE = 'database/vendedores.txt'
VEICULOS_FILE = 'database/veiculos.txt'
OPERACOES_FILE = 'database/operacoes.txt'
PEDIDOS_FILE = 'database/pedidos.txt'
MONTADORAS_FILE = 'database/montadoras.txt'


# Rota inicial
@app.route('/')
def index():
    return render_template('index.html')


# ------------------------------ Clientes ---------------------------------

@app.route('/clientes')
def clientes():
    clientes = utils.carregar_dados(CLIENTES_FILE)
    return render_template('clientes.html', clientes=clientes)


@app.route('/clientes/cadastrar', methods=['POST'])
def cadastrar_cliente():
    cpf = request.form['cpf']
    nome = request.form['nome']
    endereco = request.form['endereco']
    telefone = request.form['telefone']
    celular = request.form['celular']
    renda = request.form['renda']

    # Validação do CPF
    if not utils.validar_cpf(cpf):
        return "CPF inválido!", 400

    # Gravar o cliente no arquivo
    with open(CLIENTES_FILE, 'a') as file:
        file.write(f"{cpf};{nome};{endereco};{telefone};{celular};{renda}\n")

    return redirect(url_for('clientes'))


# ------------------------------ Vendedores -------------------------------

@app.route('/vendedores')
def vendedores():
    vendedores = utils.carregar_dados(VENDEDORES_FILE)
    return render_template('vendedores.html', vendedores=vendedores)


@app.route('/vendedores/cadastrar', methods=['POST'])
def cadastrar_vendedor():
    codigo = request.form['codigo']
    usuario = request.form['usuario']

    # Gravar o vendedor no arquivo
    with open(VENDEDORES_FILE, 'a') as file:
        file.write(f"{codigo};{usuario}\n")

    return redirect(url_for('vendedores'))


# ------------------------------ Veículos ---------------------------------

@app.route('/veiculos')
def veiculos():
    veiculos = utils.carregar_dados(VEICULOS_FILE)
    return render_template('veiculos.html', veiculos=veiculos)


@app.route('/veiculos/cadastrar', methods=['POST'])
def cadastrar_veiculo():
    chassi = request.form['chassi']
    placa = request.form['placa']
    marca = request.form['marca']
    modelo = request.form['modelo']
    ano_fabricacao = request.form['ano_fabricacao']
    ano_modelo = request.form['ano_modelo']
    cor = request.form['cor']
    valor = request.form['valor']

    # Gravar o veículo no arquivo
    with open(VEICULOS_FILE, 'a') as file:
        file.write(f"{chassi};{placa};{marca};{modelo};{ano_fabricacao};{ano_modelo};{cor};{valor}\n")

    return redirect(url_for('veiculos'))


# ------------------------------ Operações --------------------------------

@app.route('/operacoes')
def operacoes():
    operacoes = utils.carregar_dados(OPERACOES_FILE)
    return render_template('operacoes.html', operacoes=operacoes)


@app.route('/operacoes/cadastrar', methods=['POST'])
def cadastrar_operacao():
    operacao_tipo = request.form['tipo']  # Compra ou Venda
    cliente = request.form['cliente']
    vendedor = request.form['vendedor']
    veiculo = request.form['veiculo']
    valor = request.form['valor']

    # Gravar a operação no arquivo
    with open(OPERACOES_FILE, 'a') as file:
        file.write(f"{operacao_tipo};{cliente};{vendedor};{veiculo};{valor}\n")

    return redirect(url_for('operacoes'))


# ------------------------------ Pedidos ----------------------------------

@app.route('/pedidos')
def pedidos():
    pedidos = utils.carregar_dados(PEDIDOS_FILE)
    return render_template('pedidos.html', pedidos=pedidos)


@app.route('/pedidos/cadastrar', methods=['POST'])
def cadastrar_pedido():
    numero = request.form['numero']
    cliente = request.form['cliente']
    vendedor = request.form['vendedor']
    montadora = request.form['montadora']
    modelo = request.form['modelo']
    ano = request.form['ano']
    cor = request.form['cor']
    acessorios = request.form['acessorios']
    valor = request.form['valor']

    # Gravar o pedido no arquivo
    with open(PEDIDOS_FILE, 'a') as file:
        file.write(f"{numero};{cliente};{vendedor};{montadora};{modelo};{ano};{cor};{acessorios};{valor}\n")

    return redirect(url_for('pedidos'))


# ------------------------------ Montadoras -------------------------------

@app.route('/montadoras')
def montadoras():
    montadoras = utils.carregar_dados(MONTADORAS_FILE)
    return render_template('montadoras.html', montadoras=montadoras)


@app.route('/montadoras/cadastrar', methods=['POST'])
def cadastrar_montadora():
    cnpj = request.form['cnpj']
    razao_social = request.form['razao_social']
    marca = request.form['marca']
    contato = request.form['contato']
    telefone = request.form['telefone']
    celular = request.form['celular']

    # Gravar a montadora no arquivo
    with open(MONTADORAS_FILE, 'a') as file:
        file.write(f"{cnpj};{razao_social};{marca};{contato};{telefone};{celular}\n")

    return redirect(url_for('montadoras'))


if __name__ == '__main__':
    app.run(debug=True)
