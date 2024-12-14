ALTER TABLE funcionarios ADD COLUMN id_supervisor INT NULL;

ALTER TABLE funcionarios ADD FOREIGN KEY(id_supervisor) REFERENCES funcionarios(numf);

INSERT INTO departamentos(id, nome, sala) VALUES(2, "Contabilidade", "Sala 5");

INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario) VALUES(3, 2, "12345", "098765", "João Santos",
"Rua Y", 1500);

INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(4, 2, "8709821", "878721314",
"Pedro da Silva", "Rua A", 1000, 3);