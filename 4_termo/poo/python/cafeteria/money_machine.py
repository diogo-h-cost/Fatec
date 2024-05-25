class MoneyMachine:

    DINHEIRO = "$"

    VALOR_MOEDAS = {
        "vinte_e_cinco": 0.25,
        "dez": 0.10,
        "cinco": 0.05,
        "um": 0.01
    }

    def __init__(self):
        self.lucro = 0
        self.dinheiro_recebido = 0

    def report(self):
        """Prints the current profit"""
        print(f"Dinheiro: {self.DINHEIRO}{self.lucro}")

    def processar_moedas(self):
        """Returns the total calculated from coins inserted."""
        print("Por favor, insira as moedas.")
        for coin in self.VALOR_MOEDAS:
            self.dinheiro_recebido += int(input(f"Quantos/as {coin}?: ")) * self.VALOR_MOEDAS[coin]
        return self.dinheiro_recebido

    def fazer_pagamento(self, custo):
        """Returns True when payment is accepted, or False if insufficient."""
        self.processar_moedas()
        if self.dinheiro_recebido >= custo:
            change = round(self.dinheiro_recebido - custo, 2)
            print(f"\nAqui estão {self.DINHEIRO}{change} em trocados.")
            self.lucro += custo
            self.dinheiro_recebido = 0
            return True
        else:
            print("Desculpe, o dinheiro não é suficiente. Vamos reembolsar.")
            self.dinheiro_recebido = 0
            return False
