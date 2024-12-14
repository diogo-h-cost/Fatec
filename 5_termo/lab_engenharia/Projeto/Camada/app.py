from flask import Flask, render_template, request
from controle import ProdutoControle

app = Flask(__name__)

@app.route("/")
def menu():
    """Exibe o menu principal com opções para cadastrar e consultar produtos."""
    return render_template("menu.html")

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar_produto():
    """Cadastra um novo produto."""
    if request.method == "GET":
        return render_template("cadastrar_produto.html")
    else:
        codigo = request.form["codigo"]
        descricao = request.form["descricao"]
        preco = float(request.form["preco"])
        quantidade = int(request.form["quantidade"])

        if produtos.cadastrar(codigo, descricao, preco, quantidade):
            return render_template("mensagem.html", mensagem="Produto cadastrado com sucesso!")
        else:
            return render_template("mensagem.html", mensagem="Falha no cadastro!")

@app.route("/consultar", methods=["GET", "POST"])
def consultar_produto():
    """Consulta um produto por código."""
    if request.method == "GET":
        return render_template("consultar_produto.html")
    else:
        codigo = request.form["codigo"]
        produto = produtos.consultar(codigo)

        if produto:
            return render_template("exibe_produto.html", produto=produto)
        else:
            return render_template("mensagem.html", mensagem="Produto não encontrado.")

@app.route("/atualizar", methods=["GET", "POST"])
def atualizar_preco():
    """Atualiza o preco de um produto após a sua consulta"""
    atual = produtos.produto_atual()
    print(atual)
    if request.method =="GET":
        return render_template("atualizar_preco.html", produto=produtos.produto_atual())
    else:
        codigo = atual[0]
        novo_preco=request.form["preco"]
        print('Novo preço: ', novo_preco, '\nCodigo: ', atual[0])
        if produtos.atualizar(codigo, novo_preco):
            return render_template("mensagem.html", mensagem="Preço atualizado!")
        else:
            return render_template("mensagem.html", mensagem="Falha na atualização do preço !")

@app.route("/repor", methods=["GET", "POST"])
def repor_produto():
    """Repõe um produto após a sua consulta"""
    atual = produtos.produto_atual()
    print(atual)
    if request.method =="GET":
        return render_template("repor_produto.html", produto=produtos.produto_atual())
    else:
        codigo = atual[0]
        qtde=request.form["qtde"]
        #print('Novo preço: ', novo_preco, '\nCodigo: ', atual[0])
        if produtos.repor(codigo, qtde):
            return render_template("mensagem.html", mensagem="Produto reposto!")
        else:
            return render_template("mensagem.html", mensagem="Falha na reposição!")

@app.route("/vender", methods=["GET", "POST"])
def vender_produto():
    """Vende um produto após a sua consulta"""
    atual = produtos.produto_atual()
    print(atual)
    if request.method =="GET":
        return render_template("vender_produto.html", produto=produtos.produto_atual())
    else:
        codigo = atual[0]
        qtde=request.form["qtde"]
        #print('Novo preço: ', novo_preco, '\nCodigo: ', atual[0])
        if produtos.vender(codigo, qtde):
            return render_template("mensagem.html", mensagem="Produto vendido!")
        else:
            return render_template("mensagem.html", mensagem="Quantidade insuficiente!")

@app.route("/excluir", methods=["GET", "POST"])
def excluir_produto():
    """Exclui um produto após a sua consulta"""
    atual = produtos.produto_atual()
    print(atual)
    if request.method =="GET":
        return render_template("excluir_produto.html", produto=produtos.produto_atual())
    else:
        codigo = atual[0]
        if produtos.excluir(codigo):
            return render_template("mensagem.html", mensagem="Produto excluído!")
        else:
            return render_template("mensagem.html", mensagem="Falha na exclusão!")

produtos = ProdutoControle()
if __name__ == "__main__":
    app.run(debug=True)