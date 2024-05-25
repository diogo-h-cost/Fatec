from juridica import PessoaJuridica
from fisica import PessoaFisica

class MEI(PessoaJuridica, PessoaFisica):
    def __init__(self, id = "", cpf = "", nome = "", cnpj = "", razao_social = "", tipo = "", nome_fantasia = "", endereco = "", telefone = "", email = ""):
        super().__init__(id, cnpj, razao_social, tipo, nome_fantasia, endereco, telefone, email)
        self._nome = nome
        self._cpf = cpf
        self._razao_social = self.nome + ' ' + self.cpf

    def validaFaturamento(self, valor=0):
        if valor > 81000:
            print("O faturamento anual da MEI deve ser de até R$ 81.000")