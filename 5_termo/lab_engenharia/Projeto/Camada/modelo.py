import mysql.connector

class Produto:
    def __init__(self, codigo, descricao, preco, qtde):
        self._codigo = codigo
        self._descricao = descricao
        self._preco = preco
        self._qtde = qtde

    @property
    def codigo(self):
        return self._codigo
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco(self):
        return self._preco
    @property
    def qtde(self):
        return self._qtde

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    def repor(self, q):
        self._qtde += q

    def vender(self, q):
        if q > self._qtde:
            return False
        self._qtde -= q
        return True

class ProdutoDAO:
    def conectaDB(self):
        self.con = mysql.connector.connect(host="localhost", database="loja", user="root", password="")
        if self.con.is_connected():
            print("Conectado ao banco de dados!")
            self.cursor = self.con.cursor()
            return True
        return False

    def desconectaDB(self):
        self.con.close()

    def insert(self, obj):
        if not self.conectaDB():
            return False

        sql = "INSERT INTO produto VALUES(%s, %s, %s, %s)"
        values = (obj.codigo, obj.descricao, obj.preco, obj.qtde)
        self.cursor.execute(sql, values)

        inserido = False
        if self.cursor.rowcount > 0:
            inserido = True
            self.con.commit()

        self.desconectaDB()
        return inserido

    def update(self, obj):
        if not self.conectaDB():
            return False

        sql = "UPDATE produto set preco = %s, qtde = %s WHERE codigo = %s"
        values = (obj.preco, obj.qtde, obj.codigo)
        self.cursor.execute(sql, values)

        atualizado = False
        if self.cursor.rowcount > 0:
            atualizado = True
            self.con.commit()

        self.desconectaDB()
        return atualizado

    def delete(self, cod):
        if not self.conectaDB():
            return False

        self.cursor.execute(f"DELETE FROM produto WHERE codigo = {cod}")

        excluido = False
        if self.cursor.rowcount > 0:
            excluido = True
            self.con.commit()

        self.desconectaDB()
        return excluido

    def select(self, cod):
        if not self.conectaDB():
            return False

        self.cursor.execute(f"SELECT * FROM produto WHERE codigo = {cod}")
        dados = self.cursor.fetchone()

        prod = None
        if dados != None:
            prod = Produto(dados[0], dados[1], dados[2], dados[3])

        self.desconectaDB()
        return prod