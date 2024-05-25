""" 1º
Escreva um programa com uma função que receba duas strings e retorne uma terceira com os
caracteres comuns às duas strings lidas.
1ª string: AAACTBF
2ª string: CBTD
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns
a ambas.
"""

def igual(l1, l2):
    l3 = []
    for i in l1:
        if i in l2 and i not in l3:
            l3.append(i)
    return "".join(l3)

l1 = input("1º string: ").upper()
l2 = input("2º string: ").upper()

print(igual(l1, l2))

""" 2º
Faça um programa em Python que tenha uma função desenha_retangulo_solido que exibe um
retângulo sólido composto inteiramente do mesmo caractere. A função deverá ser capaz de
desenhar retângulos de tamanho parametrizável, de modo que os parâmetros deverão incluir
quantidade de linhas, quantidade de colunas e caractere desejado. Por exemplo, se a quantidade de
linhas for 5, quantidade de colunas for 20 e o caractere for 'M', a função deverá exibir:
"""

def desenha_retangulo_solido(lin, col, car):
    for i in range(lin):
        for j in range(col):
            print(car, end="")
        print()

lin = int(input("linha: "))
col = int(input("coluna: "))
car = input("Caractere: ").upper()
desenha_retangulo_solido(lin, col, car)