CREATE DATABASE erp_estoque;
USE erp_estoque;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    categoria VARCHAR(30),
    preco FLOAT,
    quantidade INT,
    ultima_mov DATETIME
);

SELECT * FROM produtos;

