USE produto_db;

SELECT * FROM categoria;
SELECT * FROM produto;
SELECT * FROM produto_categoria;

CREATE TABLE venda(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
id_produto BIGINT NOT NULL,
data DATETIME NOT NULL,
quantidade INT NOT NULL,
dinheiro CHAR(1) NOT NULL,
cartao CHAR(1) NOT NULL,
parcelas INT NOT NULL,
FOREIGN KEY (id_produto) REFERENCES produto(id)
);

SELECT * FROM venda;

INSERT INTO venda(id_produto, data, quantidade, dinheiro, cartao, parcelas)
VALUES
(1, '2024-07-10 00:00:00', 10, 'S', 'N', 1),
(2, '2024-07-10 00:00:00', 25, 'N', 'S', 10),
(3, '2024-07-10 00:00:00', 50, 'S', 'N', 1),
(4, '2024-07-10 00:00:00', 35, 'N', 'S', 1),
(5, '2024-07-10 00:00:00', 27, 'N', 'S', 1),
(6, '2024-07-10 00:00:00', 5, 'N', 'S', 1),
(7, '2024-07-10 00:00:00', 9, 'N', 'S', 1);

WITH vendas_cartao AS (SELECT id_produto, quantidade FROM venda WHERE cartao = 'S')
	SELECT quantidade FROM vendas_cartao;

WITH vendas_cartao AS (SELECT id_produto, quantidade FROM venda WHERE cartao = 'S'),
    vendas_dinheiro AS (SELECT id_produto, quantidade FROM venda WHERE dinheiro = 'S')
    SELECT * FROM vendas_cartao JOIN vendas_dinheiro;

WITH vendas_cartao AS (SELECT id_produto, quantidade FROM venda WHERE cartao = 'S')
	SELECT vendas_cartao.id_produto, vendas_cartao.quantidade, produto.nome, produto.preco_venda,
    (vendas_cartao.quantidade * produto.preco_venda) AS valor_total
    FROM vendas_cartao INNER JOIN produto ON produto.id = vendas_cartao.id_produto;

SELECT id, cartao, dinheiro, parcelas,
CASE
	WHEN cartao = 'S' THEN 'Pago cartao'
    WHEN dinheiro = 'S' THEN 'Pago dinheiro'
END AS meio
FROM venda;

SELECT id, cartao, dinheiro, parcelas,
(CASE
	WHEN parcelas > 1 THEN 'Parcelado'
    ELSE 'À vista'
END) AS pagamento
FROM venda;
