from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuração da conexão com o MySQL
def get_db_connection():
    """Função para obter uma nova conexão com o banco de dados"""
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="rede_sigma"
    )

# Rota para exibir a página principal
@app.route("/")
def index():
    return render_template("index.html")

# Rota para buscar os veículos no banco de dados
@app.route("/veiculos", methods=["GET"])
def listar_veiculos():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM veiculos ORDER BY marca, modelo")
        veiculos = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify(veiculos)
    except mysql.connector.Error as err:
        return jsonify({"error": f"Erro ao buscar veículos: {err}"}), 500

# Rota para adicionar um veículo
@app.route("/veiculos", methods=["POST"])
def adicionar_veiculo():
    data = request.json
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO veiculos (numero_chassi, placa, marca, modelo, ano_fabricacao, ano_modelo, cor, valor)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (data["chassi"], data["placa"], data["marca"], data["modelo"], data["anoFabricacao"],
              data["anoModelo"], data["cor"], data["valor"]))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"message": "Veículo adicionado com sucesso!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": f"Erro ao adicionar veículo: {err}"}), 400

# Rota para excluir um veículo
@app.route("/veiculos/<int:id>", methods=["DELETE"])
def excluir_veiculo(id):
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM veiculos WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"message": "Veículo excluído com sucesso!"})
    except mysql.connector.Error as err:
        return jsonify({"error": f"Erro ao excluir veículo: {err}"}), 400

if __name__ == "__main__":
    app.run(debug=True)
