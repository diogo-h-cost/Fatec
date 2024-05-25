class Animal:
    def __init__(self, nome, sexo, peso, especie, raca, data_nasc):
        self.__nome = nome
        self.__sexo = sexo
        self.__peso = peso
        self.__especie = especie
        self.__raca = raca
        self.__data_nasc = data_nasc

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, value):
        self.__sexo = value

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, value):
        self.__peso = value

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, value):
        self.__especie = value

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, value):
        self.__raca = value

    @property
    def data_nasc(self):
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, value):
        self.__data_nasc = value