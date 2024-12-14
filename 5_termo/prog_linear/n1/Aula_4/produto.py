from random import randint

def gerar_matriz(lin, col):
    return [[randint(1, 9) for _ in range(col)] for _ in range(lin)]

def multiplicar_matrizes(mat_a, mat_b, m, k, n):
    mat_c = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for p in range(k):
                mat_c[i][j] += mat_a[i][p] * mat_b[p][j]
    return mat_c

def exibir_matriz(matriz, tit):
    print(f"--------- {tit} ---------")
    for linha in matriz:
        for elem in linha:
            print(f"{elem:>3}", end=" ")
        print()
    print()

print()
m = int(input("Linhas da Matriz A (m): "))
k = int(input("Colunas da Matriz A (e linhas de B) (k): "))
n = int(input("Colunas da Matriz B (n): "))
print()

mat_a = gerar_matriz(m, k)
mat_b = gerar_matriz(k, n)

if k != len(mat_b):
    print("\n>>> Numero de colunas de A != numero de linhas de B <<<\n")
else:
    mat_c = multiplicar_matrizes(mat_a, mat_b, m, k, n)

    exibir_matriz(mat_a, "MATRIZ A")
    exibir_matriz(mat_b, "MATRIZ B")
    exibir_matriz(mat_c, "MATRIZ PRODUTO (A * B)")