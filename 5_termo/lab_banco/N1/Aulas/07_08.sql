CREATE SCHEMA `db_aula` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

USE db_aula;

CREATE TABLE departamentos(
id INT NOT NULL,
nome VARCHAR(255) NOT NULL,
sala VARCHAR(255) NOT NULL,
PRIMARY KEY(id));

CREATE TABLE funcionarios(
numf INT NOT NULL,
depto_id INT NOT NULL,
rg VARCHAR(12) NOT NULL,
cpf VARCHAR(14),
nome VARCHAR(255) NOT NULL,
endereco VARCHAR(255) NOT NULL,
salario FLOAT,
PRIMARY KEY(numf),
FOREIGN KEY(depto_id) REFERENCES departamentos(id));