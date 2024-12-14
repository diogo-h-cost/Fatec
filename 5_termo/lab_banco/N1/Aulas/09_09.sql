# JOINS (Inner, Left, Right, Full)

USE empresa;

SHOW TABLES;

SELECT * FROM funcionarios;
SELECT * FROM departamentos;
SELECT * FROM telefones;

INSERT INTO departamentos(id, nome, sala) VALUES(9, "Recursos Humanos", "Sala 9");

/*
Retorna apenas as linhas que têm correspondência em ambas as tabelas envolvidas na junção
*/
SELECT * FROM funcionarios a
INNER JOIN departamentos b ON a.depto_id = b.id;

/*
Retorna todas as linhas da tabela à DIREITA e as linhas correspondentes
da tabela à ESQUERDA. Se não houver correspondência, os resultados da tabela à esquerda serão NULOS
*/
SELECT * FROM funcionarios a
RIGHT JOIN departamentos b ON a.depto_id = b.id;

/*
Retorna todas as linhas da tabela à ESQUERDA e as linhas correspondentes da tabela à DIREITA.
Se não houver correspondência, os resultados da tabela à direita serão NULOS
*/
SELECT * FROM funcionarios a
LEFT JOIN departamentos b ON a.depto_id = b.id;

/*
Retorna todas as linhas possíveis de ambas as tabelas,
combinando registros com base na condição de junção e preenchendo com NULL quando não há correspondência
*/
SELECT * FROM funcionarios CROSS JOIN departamentos;

/*
O resultado será todas as combinações possíveis dos registros da tabela departamentos
com o(s) registro(s) da tabela funcionarios que atendem à condição.
*/
SELECT * FROM funcionarios CROSS JOIN departamentos WHERE funcionarios.numf = 3;

------------------------------------------------------------------------------------------------------------

USE aula;

SHOW TABLES;

SELECT * FROM categoria;
SELECT * FROM produto_categoria;
SELECT * FROM produto;

INSERT INTO produto_categoria(id_produto, id_categoria) VALUES(1, 7);
INSERT INTO produto_categoria(id_produto, id_categoria) VALUES(5, 8);

DELETE FROM produto_categoria WHERE id_produto = 1 AND id_categoria = 7;

# JOIN com 3 tabelas