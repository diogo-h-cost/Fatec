/* TAREFA -> Crie uma tabela telefones, que conterá os campos telefone, varchar de 15 caracteres, não nulo, e um campo numf, que receberá a chave identificadora do registro do funcionário da tabela funcionário, também não pode ser nulo. Cadastre 2 telefones para cada funcionário. */

CREATE TABLE telefones(
id INT AUTO_INCREMENT PRIMARY KEY,
numf INT NOT NULL,
telefone VARCHAR(15) NOT NULL,
FOREIGN KEY (numf) REFERENCES funcionarios(numf) ON DELETE CASCADE,
UNIQUE(numf, telefone)
);

/* UNIQUE(numf, telefone): Garante que a combinação de numf e telefone seja única
prevenindo que o mesmo número de telefone seja associado mais de uma vez
ao mesmo funcionário. */

SELECT * FROM funcionarios;

INSERT INTO telefones(numf, telefone) VALUES(3, "102030");
INSERT INTO telefones(numf, telefone) VALUES(4, "541505");
INSERT INTO telefones(numf, telefone) VALUES(5, "306402");
INSERT INTO telefones(numf, telefone) VALUES(6, "807050");
INSERT INTO telefones(numf, telefone) VALUES(7, "106064");
INSERT INTO telefones(numf, telefone) VALUES(8, "151055");
INSERT INTO telefones(numf, telefone) VALUES(9, "154410");
INSERT INTO telefones(numf, telefone) VALUES(10, "151097");
INSERT INTO telefones(numf, telefone) VALUES(11, "154151");
INSERT INTO telefones(numf, telefone) VALUES(12, "410858");
INSERT INTO telefones(numf, telefone) VALUES(13, "151451");
INSERT INTO telefones(numf, telefone) VALUES(14, "564511");
INSERT INTO telefones(numf, telefone) VALUES(15, "210454");
INSERT INTO telefones(numf, telefone) VALUES(16, "346087");
INSERT INTO telefones(numf, telefone) VALUES(17, "465020");
INSERT INTO telefones(numf, telefone) VALUES(18, "708050");
INSERT INTO telefones(numf, telefone) VALUES(19, "304090");
INSERT INTO telefones(numf, telefone) VALUES(20, "208070");
INSERT INTO telefones(numf, telefone) VALUES(21, "906040");

SELECT * FROM telefones;
SELECT DISTINCT telefone FROM telefones;
