"""
1. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os
resultados em uma lista. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor
de contadores(1-6) e uma função para gerar números aleatórios, simulando os lançamentos dos
dados.
"""

from random import randint

lista = [randint(1, 6) for i in range(100)]

dic = {}
for i in lista:
    dic[i] = dic.get(i, 0) + 1

for chav, valu in sorted(dic.items()): # Ordena pela chave
    print(f"{chav} = {valu}")

# -------------------------------------------------------------

"""
2. Faça um programa para simular um tradutor de palavras Português/Inglês - Inglês/Português. 

Para isto crie um dicionário com duas palavras, uma para armazenar a palavra em português e a outra
para o inglês. 

Faça um laço para armazenar N palavras, informando as duas, após dê a opção ao
usuário escolher se ele quer entrar com uma palavra em inglês e saber a tradução ou vice-versa. 

Faça uma busca da palavra informada e a mostre na outra língua. Permita quantas consultas o usuário
desejar.
"""

def barra(tex):
    print()
    print("=" * 25)
    print(tex.upper().center(25))
    print("=" * 25)
    print()

def inserir():
    print("=" * 25)
    print("Informe a palavra em portugues e ingles (fim -> sair)")
    print("=" * 25)
    while True:
        port = input("Portugues = ").upper()
        if port == "FIM":
            break
        if port not in dic:
            ing = input("Ingles = ").upper()
            dic[port] = ing
        else:
            print()
            print("Palavra ja cadastrada")
        print("=" * 25)

def port():
    palav = input("Palavra em portugues -> ").upper()
    if palav in dic:
        print(f"A traducao de {palav} em ingles = {dic[palav]}")
    else:
        print("Palavra nao cadastra!!!".upper())

def ingl():
    palav = input("Palavra em ingles -> ").upper()
    if palav in dic.values():
        for port, ing in dic.items():
            if ing == palav:
                print(f"A traducao da {ing} em portugues = {port}")
    else:
        print("Palavra nao cadastra!!!".upper())

def listar():
    for port, ing in dic.items():
        print(f"portugues = {port} | ingles = {ing}")

dic = {}
inserir()
while True:
    barra("Menu")
    busc = int(input("1 -> Portugues para ingles\n"
                     "2 -> Ingles para portugues\n"
                     "3 -> Listar\n"
                     "4 -> Sair\n"
                     "Escolha -> "))
    if busc == 1:
        barra("Portugues")
        port()
    elif busc == 2:
        barra("Ingles")
        ingl()
    elif busc == 3:
        barra("Listar")
        listar()
    elif busc == 4:
        print("Fim de programa")
        break
    else:
        barra("Erro")
        print("Opcao invalida".upper())