"""
>> A Conjectura de Collatz <<

Por exemplo, suponha que x seja inicialmente igual a 11. O número 11 é ímpar, dessa forma o novo
valor de x será (3*11)+1 = 34. Repetindo o processo temos que o número 34 é par, logo o novo valor
de x será 34/2 = 17. Repetindo esse processo chegaremos eventualmente no número 1, quando o
processo acaba.

-> ENTRADA
Como entrada, seu programa receberá um número inteiro positivo N. Em seguida, seu programa
receberá N números inteiros positivos. Para cada um dos N números inteiros positivos, seu
programa deverá gerar a sequência de números seguindo a descrição apresentada pela Conjectura
de Collatz, armazenando os números em uma lista. Além disso, o programa deverá ser capaz de
computar a quantidade de números pares e ímpares na sequência, bem como o maior número
presente na mesma.

-> SAÍDA
Como saída, para cada um dos N números inteiros positivos, seu programa deverá imprimir essas
informações no seguinte padrão:

Valor inicial: <X>
Numeros Pares: <PARES>
Numeros Impares: <IMPARES>
Maior Numero: <MAX>

>> EXEMPLOS

- Entrada
1
11

- Saida
Valor inicial: 11
Numeros Pares: 10
Numeros Impares: 5
Maior Numero: 52
"""

def collatz(num):
    par = 0
    impar = 1 #Inicia c/ 1 por conta que nao conta o 1,00 do final da lista
    L = [num]      #While encerra quando da 1, com isso nao contando (+1 impar)
    while num != 1:
        if num % 2 == 0:
            par += 1
            num //= 2
        else:
            impar += 1
            num = num*3 + 1
        L.append(num)
    print(f'Valor inicial: {L[0]}')
    print(f'Numeros Pares: {par}')
    print(f'Numeros Impares: {impar}')
    print(f'Maior numero: {max(L)}')

N = int(input("Quantos números? => ")) #Numero de vezes a repetir

for i in range(N):
    V = int(input('Número => '))
    collatz(V)