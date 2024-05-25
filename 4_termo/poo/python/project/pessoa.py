class Pessoa:
    def __init__(self, nome, telefone, email, endereco, cpf):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, value):
        self.__endereco = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

class Medico(Pessoa):
    def __init__(self,nome, telefone, email, endereco, cpf, registro_prof, especialidade, carga_hor_sem):
        super().__init__(nome, telefone, email, endereco, cpf)
        self.__reg_prof = registro_prof
        self.__espec = especialidade
        self.__carga_hor_sem = carga_hor_sem

    @property
    def reg_prof(self):
        return self.__reg_prof

    @reg_prof.setter
    def reg_prof(self, value):
        self.__reg_prof = value

    @property
    def espec(self):
        return self.__espec

    @espec.setter
    def espec(self, value):
        self.__espec = value

    @property
    def carga_hor_sem(self):
        return self.__carga_hor_sem

    @carga_hor_sem.setter
    def carga_hor_sem(self, value):
        self.__carga_hor_sem = value

class Funcionario(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf, carga_hor_sem, sindicalizado, funcao):
        super().__init__(nome, telefone, email, endereco, cpf)
        self.__carga_hor_sem = carga_hor_sem
        self.__sindic = sindicalizado
        self.__funcao = funcao

    @property
    def carga_hor_sem(self):
        return self.__carga_hor_sem

    @carga_hor_sem.setter
    def carga_hor_sem(self, value):
        self.__carga_hor_sem = value

    @property
    def sindic(self):
        return self.__sindic

    @sindic.setter
    def sindic(self, value):
        self.__sindic = value

    @property
    def funcao(self):
        return self.__funcao

    @funcao.setter
    def funcao(self, value):
        self.__funcao = value

class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf, animal, status_inadimplencia):
        super().__init__(nome, telefone, email, endereco, cpf)
        self.__animal = animal
        self.__status = status_inadimplencia

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, value):
        self.__animal = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value