from modelo import Produto, ProdutoDAO

class ProdutoControle:
    def __init__(self):
        self.pDAO = ProdutoDAO()
        self.prod = None

    def cadastrar(self, codigo, descricao, preco, qtde):
        p = Produto(int(codigo), descricao, float(preco), int(qtde))
        return self.pDAO.insert(p)

    def consultar(self, codigo):
        self.prod = self.pDAO.select(int(codigo))
    
        if self.prod != None:
            dados = (str(self.prod.codigo), self.prod.descricao, str(self.prod.preco), str(self.prod.qtde))
            return dados

        self.prod = None
        return None

    def atualizar(self, codigo, preco):
        if self.prod.codigo != int(codigo):
            return False

        self.prod.preco = float(preco)
        atualizou = self.pDAO.update(self.prod)
        self.prod = None
        return atualizou

    def excluir(self, codigo):
        if self.prod.codigo != int(codigo):
            return False

        excluiu = self.pDAO.delete(int(codigo))
        self.prod = None
        return excluiu

    def repor(self, codigo, qtde):
        if self.prod.codigo != int(codigo):
            return False

        self.prod.repor(int(qtde)) # Dados em memoria
        repos = self.pDAO.update(self.prod) # Dados no banco
        self.prod = None
        return repos

    def vender(self, codigo, qtde):
        if self.prod.codigo != int(codigo):
            return False

        if not self.prod.vender(int(qtde)):
            return False

        vendeu = self.pDAO.update(self.prod)
        self.prod = None
        return vendeu

    def produto_atual(self):
        dados = (
            str(self.prod.codigo),
            self.prod.descricao,
            str(self.prod.preco),
            str(self.prod.qtde)
        )
        return dados