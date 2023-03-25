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