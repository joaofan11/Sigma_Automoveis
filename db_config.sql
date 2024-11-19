-- Criação do Banco de Dados
CREATE DATABASE rede_sigma;

USE rede_sigma;

-- Tabela de Clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(14) NOT NULL UNIQUE, 
    nome VARCHAR(255) NOT NULL,
    endereco_bairro VARCHAR(100),
    endereco_cidade VARCHAR(100),
    endereco_estado VARCHAR(2),
    telefone_residencial VARCHAR(15),
    celular VARCHAR(15),
    renda DECIMAL(10, 2),
    INDEX(nome) 
);

-- Tabela de Vendedores
CREATE TABLE vendedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo INT NOT NULL UNIQUE,
    usuario VARCHAR(50) NOT NULL
);

-- Tabela de Montadoras
CREATE TABLE montadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cnpj VARCHAR(18) NOT NULL UNIQUE, 
    razao_social VARCHAR(255) NOT NULL,
    marca VARCHAR(100),
    contato VARCHAR(100),
    telefone_comercial VARCHAR(15),
    celular VARCHAR(15)
);

-- Tabela de Veículos
CREATE TABLE veiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_chassi VARCHAR(17) NOT NULL UNIQUE, 
    placa VARCHAR(7) NOT NULL UNIQUE, 
    marca VARCHAR(100),
    modelo VARCHAR(100),
    ano_fabricacao INT,
    ano_modelo INT,
    cor VARCHAR(50),
    valor DECIMAL(10, 2),
    INDEX(marca, modelo) 
);

-- Tabela de Operações de Compra
CREATE TABLE operacoes_compra (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL,
    data DATE NOT NULL,
    cliente_id INT,
    vendedor_id INT,
    veiculo_id INT,
    valor DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id),
    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
);

-- Tabela de Operações de Venda
CREATE TABLE operacoes_venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL,
    data DATE NOT NULL,
    cliente_id INT,
    vendedor_id INT,
    veiculo_id INT,
    valor_entrada DECIMAL(10, 2),
    valor_financiado DECIMAL(10, 2),
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id),
    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
);

-- Tabela de Pedidos
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL,
    data DATE NOT NULL,
    cliente_id INT,
    vendedor_id INT,
    montadora_id INT,
    modelo VARCHAR(100),
    ano INT,
    cor VARCHAR(50),
    acessorios TEXT,
    valor DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id),
    FOREIGN KEY (montadora_id) REFERENCES montadoras(id)
);

-- Consulta de Operações de Venda
SELECT * FROM operacoes_venda
;

-- Consulta com JOIN: Dados de Venda com Detalhes do Cliente e Veículo
SELECT 
    ov.numero AS venda_numero,
    ov.data AS venda_data,
    c.nome AS cliente_nome,
    v.modelo AS veiculo_modelo,
    ov.valor_total AS valor_total
FROM operacoes_venda ov
JOIN clientes c ON ov.cliente_id = c.id
JOIN veiculos v ON ov.veiculo_id = v.id
;

-- Inserção de Pedido
INSERT INTO pedidos (numero, data, cliente_id, vendedor_id, montadora_id, modelo, ano, cor, acessorios, valor)
VALUES
(1, '2024-11-18', 1, 1, 1, 'SUV', 2024, 'Branco', 'Ar condicionado, Teto solar', 150000.00)
;

-- Consulta de Pedidos
SELECT * FROM pedidos;

CREATE DATABASE IF NOT EXISTS data_manager;
USE data_manager;

-- Tabela para Armazenamento de Dados JSON
CREATE TABLE data_store (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_arquivo VARCHAR(255) NOT NULL,
    dados JSON NOT NULL,
    ultima_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Índice para Pesquisar por Nome do Arquivo
CREATE INDEX idx_nome_arquivo ON data_store(nome_arquivo);


CREATE PROCEDURE salvar_dados(IN nomeArquivo VARCHAR(255), IN dadosJson JSON)
BEGIN
    DECLARE arquivoExistente INT;

    -- Verifica se o arquivo já existe
    SELECT COUNT(*) INTO arquivoExistente
    FROM data_store
    WHERE nome_arquivo = nomeArquivo;

    IF arquivoExistente > 0 THEN
        -- Atualiza o registro existente
        UPDATE data_store
        SET dados = dadosJson
        WHERE nome_arquivo = nomeArquivo;
    ELSE
        -- Insere um novo registro
        INSERT INTO data_store (nome_arquivo, dados)
        VALUES (nomeArquivo, dadosJson);
    END IF;
END;


CREATE PROCEDURE carregar_dados(IN nomeArquivo VARCHAR(255))
BEGIN
    -- Retorna os dados JSON associados ao nome do arquivo
    SELECT dados
    FROM data_store
    WHERE nome_arquivo = nomeArquivo;
END;

