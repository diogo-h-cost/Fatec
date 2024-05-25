"""
Faça um programa que receba do usuário um nome de arquivo, e mostre na tela quantas linhas esse
arquivo possui.
"""

arqui = input()
try:
    with open(arqui, "r") as arq:
        qt = arq.readlines()
        print(len(qt))
except FileNotFoundError:
    print("Nao tem")