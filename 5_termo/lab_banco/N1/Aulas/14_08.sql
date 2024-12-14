USE db_aula;

SELECT * FROM funcionarios LIMIT 0, 50; # Limitar a busca

SHOW DATABASES; # Ver os bancos

SHOW TABLES; # Ver as tabelas do banco selecionado

SELECT * FROM funcionarios ORDER BY numf DESC; # Ordenar a tabela de forma descendente

SELECT b.nome, b.rg, b.cpf, a.nome AS departamento, b.salario FROM departamentos a JOIN funcionarios b
ON a.id = b.depto_id; # Uniao de tabelas JOIN pela relacao ON | alias com AS para exibir outro nome

DESCRIBE departamentos; # Descricao da tabela

INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor)
VALUES(20, 7, "342242", "23100994", "Fabin Xales", "Rua Edge", 1200, 17),
(21, 6, "21321312", "9938232", "Juca Ted", "Rua Liba", 2000, 14); # INSERT com varios values

/* Testar
RENOMEAR
FUNCOES
SUBCONSULTAS
*/