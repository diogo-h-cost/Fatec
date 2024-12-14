from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

class Ui_MainWindow(object):

    def conexao(self):
        self.con=mysql.connector.connect(host='localhost', database='loja', user='root', password='')
        if self.con.is_connected():
            print('Conectado ao banco de dados!')
            self.cursor=self.con.cursor()

    def setupUi(self, MainWindow):
        self.conexao()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 47, 14))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 47, 14))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 47, 14))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 47, 14))
        self.label_4.setObjectName("label_4")

        self.leCodigo = QtWidgets.QLineEdit(self.centralwidget)
        self.leCodigo.setGeometry(QtCore.QRect(80, 30, 81, 20))
        self.leCodigo.setObjectName("leCodigo")

        self.leDescricao = QtWidgets.QLineEdit(self.centralwidget)
        self.leDescricao.setGeometry(QtCore.QRect(80, 60, 361, 20))
        self.leDescricao.setObjectName("leDescricao")

        self.lePreco = QtWidgets.QLineEdit(self.centralwidget)
        self.lePreco.setGeometry(QtCore.QRect(80, 90, 113, 20))
        self.lePreco.setObjectName("lePreco")

        self.leQtde = QtWidgets.QLineEdit(self.centralwidget)
        self.leQtde.setGeometry(QtCore.QRect(80, 120, 113, 20))
        self.leQtde.setObjectName("leQtde")

        self.pbCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.pbCadastrar.setGeometry(QtCore.QRect(80, 160, 75, 23))
        self.pbCadastrar.setObjectName("pbCadastrar")
        self.pbCadastrar.clicked.connect(self.cadastrar)

        self.pbConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.pbConsultar.setGeometry(QtCore.QRect(170, 160, 75, 23))
        self.pbConsultar.setObjectName("pbConsultar")
        self.pbConsultar.clicked.connect(self.consultar)

        self.pbAlterar = QtWidgets.QPushButton(self.centralwidget)
        self.pbAlterar.setGeometry(QtCore.QRect(260, 160, 75, 23))
        self.pbAlterar.setObjectName("pbAlterar")
        self.pbAlterar.setEnabled(False) # Desabilita o botao
        self.pbAlterar.clicked.connect(self.alterar)

        self.pbExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.pbExcluir.setGeometry(QtCore.QRect(350, 160, 75, 23))
        self.pbExcluir.setObjectName("pbExcluir")
        self.pbExcluir.setEnabled(False) # Desabilita o botao
        self.pbExcluir.clicked.connect(self.excluir)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Loja de Informática")) # Titulo

        self.label.setText(_translate("MainWindow", "Código")) # Campo
        self.label_2.setText(_translate("MainWindow", "Descrição")) # Campo
        self.label_3.setText(_translate("MainWindow", "Preço")) # Campo
        self.label_4.setText(_translate("MainWindow", "Qtde")) # Campo

        self.pbCadastrar.setText(_translate("MainWindow", "Cadastrar")) # Botao
        self.pbConsultar.setText(_translate("MainWindow", "Consultar")) # Botao
        self.pbAlterar.setText(_translate("MainWindow", "Alterar")) # Botao
        self.pbExcluir.setText(_translate("MainWindow", "Excluir")) # Botao

    def cadastrar(self):
        codigo = int(self.leCodigo.text())
        descricao = self.leDescricao.text()
        preco = float(self.lePreco.text())
        qtde = int(self.leQtde.text())
        sql = 'INSERT INTO produto VALUES(%s,%s,%s,%s)'
        dados = (codigo, descricao, preco, qtde)
        self.cursor.execute(sql,dados)
        if self.cursor.rowcount>0:
            self.exibe_msg('Produto cadastrado!')
            self.con.commit()
            self.limpar()

    def limpar(self):
        self.leCodigo.setText('')
        self.leDescricao.setText('')
        self.lePreco.setText('')
        self.leQtde.setText('')
        self.leCodigo.setFocus()
        self.pbAlterar.setEnabled(False)
        self.pbExcluir.setEnabled(False)

    def consultar(self):
        self.cursor.execute('SELECT * FROM produto WHERE codigo = '+self.leCodigo.text())
        dados=self.cursor.fetchone()
        if dados!=None:
            self.leDescricao.setText(dados[1])
            self.lePreco.setText(str(dados[2]))
            self.leQtde.setText(str(dados[3]))
            self.pbAlterar.setEnabled(True)
            self.pbExcluir.setEnabled(True)
        else:
            self.limpar()

    def alterar(self):
        codigo=int(self.leCodigo.text())
        descricao=self.leDescricao.text()
        preco=float(self.lePreco.text())
        qtde=int(self.leQtde.text())
        sql=('update produto set descricao=%s,'+
            'preco=%s, qtde=%s where codigo=%s')
        dados=(descricao, preco, qtde, codigo)
        self.cursor.execute(sql,dados)
        if self.cursor.rowcount>0:
            self.exibe_msg('Produto alterado com sucesso!')
            self.con.commit()
            self.limpar()

    def excluir(self):
        self.cursor.execute('DELETE FROM produto WHERE codigo = ' + self.leCodigo.text())
        if self.cursor.rowcount > 0:
            self.exibe_msg('Produto excluido com sucesso!')
            self.con.commit()
            self.limpar()

    def exibe_msg(self, mensagem):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensagem)
        msg.setWindowTitle("Atençao!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())