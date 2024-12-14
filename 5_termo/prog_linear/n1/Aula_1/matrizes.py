# ENTREGUE - 27/08

from random import randint

def top(cor, tipo):
    print(f"\n|----------- {cor}{tipo.upper()}\033[0m -----------|\n")

def diagonal():
    top("\033[4m\033[35m", "Matriz Diagonal")

    mat = int(input("Ordem da Matriz: "))
    print()

    for i in range(mat):
        for j in range(mat):
            if i == j:
                print(f"\033[32m{randint(1, 9)}\033[0m", end=" ")
            else:
                print(f"\033[31m{0}\033[0m", end=" ")
        print()

def identidade():
    top("\033[4m\033[34m", "Matriz Identidade")

    mat = int(input("Ordem da Matriz: "))
    print()

    for i in range(mat):
        for j in range(mat):
            if i == j:
                print(f"\033[34m{1}\033[0m", end=" ")
            else:
                print(f"\033[33m{0}\033[0m", end=" ")
        print()

def simetrica():
    top("\033[4m\033[32m", "Matriz Simetrica")

    mat = int(input("Ordem da Matriz: "))

    matriz = [[0 for i in range(mat)] for j in range(mat)]

    for i in range(mat):
        for j in range(mat):
            valor = randint(1, 9)
            matriz[i][j] = valor
            matriz[j][i] = valor
    print()

    for linha in matriz:
        print(f"\033[34m{linha}\033[0m")

def transposta():
    top("\033[4m\033[33m", "Matriz Transposta")

    lin = int(input("Linhas da Matriz: "))
    col = int(input("Colunas da Matriz: "))

    matriz = []
    for i in range(lin):
        linha = [randint(1, 9) for _ in range(col)]
        matriz.append(linha)

    print("\n****** \033[33mMATRIZ ORIGINAL\033[0m ******\n")
    for linha in matriz:
        print(f"\033[31m{linha}\033[0m")

    matriz_transposta = [[matriz[j][i] for j in range(lin)] for i in range(col)]

    print("\n****** \033[33mMATRIZ TRANSPOSTA\033[0m ******\n")
    for linha in matriz_transposta:
        print(f"\033[32m{linha}\033[0m")
    print()

while True:
    top("\033[4m\033[1m", "Menu")
    opcao = int(input("""1- Matriz \033[35mDiagonal\033[0m
2- Matriz \033[34mIdentidade\033[0m
3- Matriz \033[32mSimetrica\033[0m
4- Matriz \033[33mTransposta\033[0m
5- \033[31mSair\033[0m\n
\033[36mEscolha -> \033[0m"""))
    match opcao:
        case 1:
            diagonal()
        case 2:
            identidade()
        case 3:
            simetrica()
        case 4:
            transposta()
        case 5:
            print("\nSaindo......\n")
            break
        case _:
            print("\n\033[31m>>> Erro, apenas numeros de 1 a 5 <<<\033[0m")