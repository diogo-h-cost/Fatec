SHOW TABLES;

SELECT * FROM categoria;
SELECT * FROM produto;
SELECT * FROM produto_categoria;

INSERT INTO produto_categoria VALUES(1, 7);

# JOIN entre 3 tabelas
SELECT prod.id, prod.nome, categ.id, categ.nome, prod_categ.id_produto, prod_categ.id_categoria
FROM produto_categoria prod_categ
JOIN produto prod ON prod_categ.id_produto = prod.id
JOIN categoria categ ON prod_categ.id_categoria = categ.id;