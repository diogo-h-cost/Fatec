CREATE DATABASE produto_db;

USE produto_db;

CREATE TABLE produto (
id BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nome VARCHAR(100) NOT NULL,
descricao VARCHAR(255) NULL,
preco_compra DECIMAL(9, 2) NOT NULL,
preco_venda DECIMAL(9, 2) NOT NULL,
quantidade INT DEFAULT 0 NOT NULL,
disponivel BOOL DEFAULT TRUE NOT NULL,
dt_cadastro TIMESTAMP NOT NULL
);

CREATE TABLE categoria (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nome VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE prod_categ (
id_prod BIGINT NOT NULL,
id_categ INT NOT NULL,
PRIMARY KEY (id_prod, id_categ), # Chave primaria composta
FOREIGN KEY (id_prod) REFERENCES produto(id),
FOREIGN KEY (id_categ) REFERENCES categoria(id)
);

INSERT INTO produto(nome, descricao, preco_compra, preco_venda, quantidade, disponivel, dt_cadastro)
VALUES('Caneta', 'Marca: Bic, Cor: Preta', 1.50, 3.0, 100, True, '2024-08-28 14:00:00');

INSERT INTO categoria(nome) VALUE('Material Escolar');

INSERT INTO prod_categ(id_prod, id_categ) VALUES(1, 1);

SELECT * FROM produto;
SELECT * FROM categoria;
SELECT * FROM prod_categ;