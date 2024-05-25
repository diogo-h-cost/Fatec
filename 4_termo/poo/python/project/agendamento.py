class Agendamento:
    def __init__(self, data, medico, cliente, funcionario, compareceu = "", concluido = "", valor = 0, pago = ""):
        self.__data = data
        self.__medico = medico
        self.__cliente = cliente
        self.__funcionario = funcionario
        self.__compar = compareceu
        self.__concluid = concluido
        self.__valor = valor
        self.__pago = pago

    def agendar(self):
        self.__compar = False
        self.__concluid = False
        self.__pago = False
        return "Agendamento realizado com sucesso"

    def finalizar(self):
        self.__compar = True
        self.__concluid = True
        self.__pago = True
        return "Consulta concluída com sucesso"

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self, value):
        self.__medico = value

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, value):
        self.__cliente = value

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, value):
        self.__funcionario = value

    @property
    def compar(self):
        return self.__compar

    @compar.setter
    def compar(self, value):
        self.__compar = value

    @property
    def concluid(self):
        return self.__concluid

    @concluid.setter
    def concluid(self, value):
        self.__concluid = value

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, value):
        self.__valor = value

    @property
    def pago(self):
        return self.__pago

    @pago.setter
    def pago(self, value):
        self.__pago = value