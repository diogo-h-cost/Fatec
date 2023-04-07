""" 1º
Defina a função soma_nat que recebe como argumento um número natural n e devolve a soma
de todos os números naturais até n.
"""

def soma_nat(n):
    return sum([i for i in range(1, n+1)])

N = int(input("Informe um numero: "))
print(f"A soma de 1 até {N} é igual a {soma_nat(N)}")

""" 2º
Defina a função quadrados que recebe como argumento um número natural n devolve a lista
dos n primeiros quadrados perfeitos.
"""

def quadrados(num):
    return [i**2 for i in range(1, num+1)]

num = int(input("Informe Nº: "))
print(f"Os {num} primeiros quadrados perfeitos sao: {quadrados(num)}")

""" 3º
Defina a função indices_pares que recebe como argumento uma lista de números
inteiros w e devolve a lista dos elementos de w em posições pares.
"""

from random import randint

def indices_pares(w):
    return [w[i] for i in range(0, len(w), 2)]
    #return [n for n in w[::2]]  -> C/ fatiamento de lista

w = [randint(1, 20) for i in range(10)]
print(f"Antes > {w} /// Após > {indices_pares(w)}")

""" 4º
Defina a função prod_lista que recebe como argumento uma lista de números inteiros e
devolve o produto dos seus elementos.
"""

from random import randint
from functools import reduce # Reduzir em apenas 1 numero
from operator import mul # -> funcao p/ multiplicar os numeros

def prod_lista(lista):
    #return reduce(lambda x, y: x * y, lista)
    return reduce(mul, lista)

w = [randint(1, 20) for i in range(5)]
print(f"O produto de {w} ->> {prod_lista(w)}")

""" 5º
Defina a função media_digitos que recebe como argumento um número natural e devolve a
média dos seus dígitos.
"""

def media_digitos(n):
    return sum(list(map(int, str(n)))) / len(str(n))

n = int(input("Nº: "))
print(f"A media de {n} ->> {media_digitos(n)}")