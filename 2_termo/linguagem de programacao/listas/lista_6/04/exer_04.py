"""
Faça um programa no qual o usuário informa o nome do arquivo, e uma palavra, e retorne o número de
vezes que aquela palavra aparece no arquivo.
"""

arqu = input()

try:
    with open(arqu, "r", encoding='utf-8') as file:
        palav = input()
        arq = file.readlines()
        cont = 0
        for i in arq:
            cont += i.count(palav)
        print(f"{palav} == {cont}x")
except FileNotFoundError:
    print("Nao tem o arquivo")