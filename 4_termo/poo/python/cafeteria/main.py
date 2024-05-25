from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()

ligado = True

while ligado:
    opcoes = menu.get_items()
    print(f"Materia P: {coffee.status()}")
    escolha = input(f"O que voce gostaria?\n"
                    f"{opcoes}\n"
                    f"Escolha -> ")
    if escolha == "off":
        ligado = False
    elif escolha == "report":
        coffee.report()
        money.report()
    else:
        bebida = menu.achar_bebida(escolha)
        print(bebida)
        if coffee.recursso_e_suficiente(bebida):
            if money.fazer_pagamento(bebida.custo):
                coffee.fazer_cafe(bebida)