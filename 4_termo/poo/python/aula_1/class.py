class Funcionario:
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    def cal_salario(self, horas_trab, val_hora):
        salario = round((float(horas_trab) * float(val_hora)), 2)
        return salario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

user = Funcionario("caio", "caio@gmail.com", "14993")
print(user.nome)
user.name = "frigo"
print(user)