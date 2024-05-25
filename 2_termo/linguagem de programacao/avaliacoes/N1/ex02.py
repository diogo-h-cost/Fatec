"""
Faça uma função que receba uma lista de números armazenados de forma crescente, e dois valores (limite inferior e limite superior), 
e retornea sublista cujos elementos são maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.

Exemplo:
lista inicial = [12,14,15,16,18,20,24,26,28,32,34,38]
limite inferior = 13
limite superior = 26
lista exibida: [14,15,16,18,20,24,26]

No programa principal, gere uma lista de 15 números inteiros, aleatórios, entre 1 e 50. 
Ordene a lista. Peça os valores do intervalo, validando para que o inícioseja menor que o final. 
(Pode fazer função para essa validação).Chame a função e imprima a lista resultante.
"""

from random import randint

def sublist(lis, liminf, limsup):
    sub = []
    for i in range(len(lis)):
        if lis[i] > liminf and lis[i] <= limsup:
            sub.append(lis[i])
    return sub

lis = []
for i in range(15):
    lis.append(randint(1, 50))
lis.sort()

print(f"Lista inicial = {lis}")
liminf = int(input("Limite inferior = "))
limsup = int(input("Limite superior = "))

if liminf > limsup:
    liminf, limsup = limsup, liminf

print(f"Lista exibida: {sublist(lis, liminf, limsup)}")