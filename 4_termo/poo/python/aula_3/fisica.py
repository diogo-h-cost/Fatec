from cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, id = "", cpf = "", nome = "", endereco = "", telefone = "", email = ""):
        super().__init__(id, email, telefone, endereco)
        self._nome = nome
        self._cpf = cpf

    def validaFaturamento(self, valor = 0):
        print('Análise de faturamento não se aplica')

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value