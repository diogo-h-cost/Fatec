/* TAREFA -> ADD 5 departamentos e 15 funcionarios (3 func por depart) */

INSERT INTO departamentos(id, nome, sala) VALUES(3, "Marketing", "Sala 2");
INSERT INTO departamentos(id, nome, sala) VALUES(4, "Pesquisa", "Sala 7");
INSERT INTO departamentos(id, nome, sala) VALUES(5, "Desenvolvimento", "Sala 6");
INSERT INTO departamentos(id, nome, sala) VALUES(6, "Teste", "Sala 3");
INSERT INTO departamentos(id, nome, sala) VALUES(7, "Suporte", "Sala 4");

SELECT * FROM departamentos;

INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario) VALUES(5, 3, "3532523", "54515151", "Carlos Matos", "Rua tatu", 2000);
INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(6, 3, "41545", "54178879784",
"Fabio Tutes", "Rua mirus", 1500, 5);
INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(7, 3, "65618741", "78942350",
"Julio garcia", "Rua torta", 1700, 5);

INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario) VALUES(8, 4, "1511021", "45515151", "Jonas Melo", "Rua K", 3000);
INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(9, 4, "51521515", "5515151",
"Dener Visto", "Rua Ford", 2000, 8);
INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(10, 4, "415178", "96482165",
"Salu Krap", "Rua Apud", 1800, 8);

INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario) VALUES(11, 5, "651152", "111150146", "Edival Ald", "Rua Fabi", 4000);
INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(12, 5, "541555", "15151515",
"Lumir Chaves", "Rua Fig", 2500, 11);
INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(13, 5, "55215155", "155145515",
"Julia Gomes", "Rua Tupi", 2200, 11);

INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario) VALUES(14, 6, "262626", "8748474", "Fralu Lip", "Rua Jop", 6000);
INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(15, 6, "87115155", "415445515",
"Carla Nuna", "Rua Quad", 3500, 14);
INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(16, 6, "15155155", "41598788785",
"Ana Lopes", "Rua Octa", 4500, 14);

INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario) VALUES(17, 7, "251514", "551117897", "Maria Lua", "Rua Host", 3500);
INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(18, 7, "47654564", "45452100",
"Oliver Zeb", "Rua Oliva", 1500, 17);
INSERT INTO funcionarios(numf, depto_id, rg, cpf, nome, endereco, salario, id_supervisor) VALUES(19, 7, "7455564", "41151100",
"Tiago Varp", "Rua Gold", 1700, 17);

SELECT * FROM funcionarios;

UPDATE funcionarios SET endereco = "Rua Mirus" WHERE numf = 6;
UPDATE funcionarios SET endereco = "Rua Torta" WHERE numf = 7;

SELECT * FROM funcionarios WHERE numf > 5 and numf < 8;
