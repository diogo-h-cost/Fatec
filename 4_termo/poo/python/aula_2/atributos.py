class Funcionario:
    def __init__(self, nome, email, telefone):
        self.nome = nome # Atributo Publico
        self._email = email # Atributo Protected
        self.__telefone = telefone # Atributo Private

func1 = Funcionario("Fradu", "frigo@gmail.com", "14 8405-6432")
print(func1.nome)
print(func1._email)
print(func1.__telefone)