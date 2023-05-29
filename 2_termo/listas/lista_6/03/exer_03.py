"""
Faça um programa que receba o nome de dois arquivos do usuário, e crie um terceiro arquivo com
conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo).
"""

arqui = input()
arqui2 = input()

try:
    with open(arqui, "r") as arq, open(arqui2, "r") as arq2:
        with open("saida(3).txt", "w") as sai:
            sai.write(f"{arq.read()}\n")
            sai.write(arq2.read())
except FileNotFoundError:
    print("Nao tem")