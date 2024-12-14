USE db_aula;

SELECT * FROM funcionarios;

SELECT nome, cpf FROM funcionarios ORDER BY nome DESC;

SELECT func.nome, func.cpf, func.endereco, dep.nome AS departamento, dep.sala
FROM funcionarios AS func, departamentos AS dep
WHERE dep.id = func.depto_id ORDER BY func.nome ASC;

# OU

SELECT a.nome, a.cpf, a.endereco, b.nome, b.sala
FROM funcionarios a INNER JOIN departamentos b
ON a.depto_id = b.id;