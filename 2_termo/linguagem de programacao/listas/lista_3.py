""" 1º
Faça um programa que gere uma lista de 20 números aleatórios entre 1 e 10.
Leia um número x entre 1 e 10.
Imprima a lista e mostre quantos números iguais a x tem na lista.
"""

from random import randint

l = []
for i in range(20):
    l.append(randint(1, 10))
x = int(randint(1, 10))
print(f"Lista = {l} -> X = {x} ->  {l.count(x)} X")

""" 2º
Faça um programa que gere aleatoriamente duas listas de 10 posições (valores entre 1 e 50) 
e calcule outra lista contendo, nas posições pares os valores da primeira lista e nas posições 
ímpares os valores da segunda lista.
"""

from random import randint

a = []
b = []
c = []

for i in range(10):
    a.append(randint(1, 50))
    b.append(randint(1, 50))

for j in range(10):
    c.append(a[j])
    c.append(b[j])

print(a)
print(b)
print(c)

""" 3º
Gere uma lista 20 números aleatórios entre 1 e 50 e mostre qual o maior valor da lista, o menor e a média
dos valores.
"""

from random import randint

a = []

for i in range(20):
    a.append(randint(1, 50))

print(f"Lista = {a}")
print(f"Maior = {max(a)}")
print(f"Menor = {min(a)}")
print(f"Media = {sum(a)/len(a)}")

""" 4º
Faça um programa em Python para gerar uma lista de 20 números aleatórios entre 1 e 50. Imprima a
lista. Após isto, deverá ser lido um número qualquer e verificar se esse número existe na lista ou não. Se
existir, gerar uma nova lista sem esse número (remova todas as ocorrências do número). Imprima a nova
lista.
"""

from random import randint

a = []
for i in range(20):
    a.append(randint(1, 50))
print(a)
num = int(input("Insira Nº: "))
b = a[:]
for i in range(len(a)):
    if num in a:
        a.remove(num)
print(a)

""" 5º
João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem
certeza se conseguirá montar o número desejado. Considerando a configuração dos leds dos números
abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o
valor.

Entrada
A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste, seguido
de N linhas, cada linha contendo um número (1 ≤ V ≤ 10100) correspondente ao valor que João quer
montar com os leds.

Saída
Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para montar
o valor desejado, seguido da palavra "leds".
"""

def somaleds(numero):
    leds = 0
    l = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    num = str(numero)
    for n in num:
        leds += l[int(n)]
    return leds

num = int(input("Insira um N° de testes: "))

for i in range(num):
    tes = int(input("Numero -> "))
    print(f"{somaleds(tes)} leds")