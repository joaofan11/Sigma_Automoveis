CREATE DATABASE rede_sigma;

USE rede_sigma;

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

CREATE TABLE vendedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo INT NOT NULL UNIQUE,
    usuario VARCHAR(50) NOT NULL
);

CREATE TABLE montadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cnpj VARCHAR(18) NOT NULL UNIQUE, 
    razao_social VARCHAR(255) NOT NULL,
    marca VARCHAR(100),
    contato VARCHAR(100),
    telefone_comercial VARCHAR(15),
    celular VARCHAR(15)
);

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
