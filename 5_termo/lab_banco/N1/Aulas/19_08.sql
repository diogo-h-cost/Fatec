USE db_aula;

SELECT * FROM funcionarios;

# Caractere coringa [LIKE] - seleciona tudo que comeca% ou %termina
SELECT nome, rg, cpf FROM funcionarios WHERE nome LIKE 'a%';

# Sem repeticao [DISTINCT] 
SELECT DISTINCT salario FROM funcionarios;
