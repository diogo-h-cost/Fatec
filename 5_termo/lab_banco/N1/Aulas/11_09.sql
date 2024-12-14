USE mercearia;

SELECT * FROM categoria;
SELECT * FROM produto;
SELECT * FROM produto_categoria;

# INNER JOIN c/ 3 tabelas
SELECT  prod_cat.id_produto AS tabela, cat.nome AS categoria, prod.nome, prod.descricao FROM
((produto prod INNER JOIN produto_categoria prod_cat ON prod.id = prod_cat.id_produto)
INNER JOIN categoria cat ON prod_cat.id_categoria = cat.id);

# Funcoes
SELECT SUM(preco_compra) AS soma, AVG(preco_compra) AS media FROM produto;
