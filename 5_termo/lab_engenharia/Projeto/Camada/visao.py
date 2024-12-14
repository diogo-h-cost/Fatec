from controle import ProdutoControle
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

class Loja:
    def __init__(self):
        self.prodControl = ProdutoControle()
        app = QtWidgets.QApplication([])
        self.tela = uic.loadUi('C:/Users/Fatec/Desktop/Projeto/Camada/Loja.ui')
        self.tela.leCodigo.focusOutEvent = self.consultarFocusOut # Quando ler o Cod exibe dados
        self.tela.pbCadastrar.clicked.connect(self.cadastrar) # Botao Cadastrar
        self.tela.pbAlterar.clicked.connect(self.alterar) # Botao Alterar
        self.tela.pbExcluir.clicked.connect(self.excluir) # Botao Excluir
        self.tela.pbVender.clicked.connect(self.vender) # Botao Vender (Movimento)
        self.tela.pbRepor.clicked.connect(self.repor) # Botao Repor (Movimento)
        self.tela.show()
        app.exec_()

    def consultarFocusOut(self, event):
        QtWidgets.QLineEdit.focusOutEvent(self.tela.leCodigo, event)
        cod = self.tela.leCodigo.text() # Captura o codigo do campo
        dados = self.prodControl.consultar(cod) # [se existir] traz os dados do banco | [se nao] None
        if dados != None: # Se estiver cadastrado exibe os campos
            self.tela.leDescricao.setText(dados[1])
            self.tela.lePreco.setText(dados[2])
            self.tela.leQtde.setText(dados[3])
            self.tela.pbCadastrar.setEnabled(False)
            self.tela.pbAlterar.setEnabled(True)
            self.tela.pbExcluir.setEnabled(True)
            self.tela.gbMovimento.setEnabled(True)
        else: # Se nao estiver cadastrado limpa os campos
            self.tela.leDescricao.setText('')
            self.tela.lePreco.setText('')
            self.tela.leQtde.setText('')
            self.tela.pbCadastrar.setEnabled(True)
            self.tela.pbAlterar.setEnabled(False)
            self.tela.pbExcluir.setEnabled(False)
            self.tela.gbMovimento.setEnabled(False)

    def cadastrar(self):
        if self.prodControl.cadastrar(
            self.tela.leCodigo.text(),
            self.tela.leDescricao.text(),
            self.tela.lePreco.text(),
            self.tela.leQtde.text()):
            self.exibe_msg('Produto Cadastrado!')
            self.limpar() # Limpar Tela e Bloquear Botoes
        else:
            self.exibe_msg('Falha no Cadastro!')

    def exibe_msg(self, mensagem):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information) # Icone da janela
        msg.setText(mensagem) # Msg da janela
        msg.setWindowTitle('Atenção!') # Titulo da janela
        msg.setStandardButtons(QMessageBox.Ok) # Botao
        msg.exec_()

    def limpar(self):
        self.tela.leCodigo.setText('') # Set um texto vazio
        self.tela.leDescricao.setText('')
        self.tela.lePreco.setText('')
        self.tela.leQtde.setText('')
        self.tela.leMovimento.setText('')

        self.tela.pbCadastrar.setEnabled(False) # Desativa os botoes
        self.tela.pbAlterar.setEnabled(False)
        self.tela.pbExcluir.setEnabled(False)
        self.tela.gbMovimento.setEnabled(False) # Desativa o bloco Movimento

        self.tela.leCodigo.setFocus() # Cursor no codigo

    def alterar(self):
        if self.prodControl.atualizar(self.tela.leCodigo.text(), self.tela.lePreco.text()):
            self.exibe_msg('Preço Atualizado!')
            self.limpar() # Limpar Tela e Bloquear Botoes
        else:
            self.exibe_msg('Falha na Atualização!')

    def excluir(self):
        if self.prodControl.excluir(self.tela.leCodigo.text()):
            self.exibe_msg('Produto Excluído')
            self.limpar() # Limpar Tela e Bloquear Botoes
        else:
            self.exibe_msg('Falha na exclusão')

    def repor(self):
        if self.prodControl.repor(
            self.tela.leCodigo.text(),
            self.tela.leMovimento.text()):
            self.exibe_msg('Produto Adicionado!')
            self.limpar() # Limpar Tela e Bloquear Botoes
        else:
            self.exibe_msg('Falha na Reposição!')

    def vender(self):
        if self.prodControl.vender(
            self.tela.leCodigo.text(),
            self.tela.leMovimento.text()):
            self.exibe_msg('Produto Vendido!')
            self.limpar() # Limpar Tela e Bloquear Botoes
        else:
            self.exibe_msg('Qtde Insuficiente!')

store = Loja()