class Funcionario:
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    def cal_salario(self, horas_trab, val_hora):
        salario = round((float(horas_trab) * float(val_hora)), 2)
        return salario

    def __eq__(self, other):
        if self.__nome != other.nome:
            return False
        elif self.__email != other.email:
            return False
        elif self.__telefone != other.telefone:
            return False
        else:
            return True

    def __str__(self):
        return f"Nome: {self.__nome}, Email: {self.__email}, Telefone: {self.__telefone}"

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

print("-" * 40)

func1 = Funcionario("Jose", "jose@jose.com", "14 1234-5678")
print(f"O salario de {func1.nome} e {func1.cal_salario(100, 2)}")

func2 = Funcionario("Joao", "joao@joao.com", "14 5555-2346")
print(f"O salario de {func2.nome} e {func2.cal_salario(110, 2)}")


func2.nome = "Jose"
func2.email = "jose@jose.com"
func2.telefone = "14 1234-5678"

print("-" * 40)

print(f"Funcionario 1 == Funcionario 2 -> {func1 is func2}")

x = func1
print(f"Funcionario 1 == X -> {func1 is x}")

print("-" * 40)

print(f"Funcionario 1 ID -> {id(func1)}")
print(f"x ID -> {id(x)}")
print(f"Funcionario 2 ID -> {id(func2)}")

print("-" * 40)

print(f"Funcionario 1 == Funcionario 2 -> {func1 == func2}")

print("-" * 40)

print(func1)

func1._Funcionario__nome = "caio"
print(func1)