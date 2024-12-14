from random import randint

def validacao(lin_a, lin_b, col_a, col_b):
    return lin_a == lin_b and col_a == col_b

def exibir(lin, col, matriz, tit):
    print(f"--------- {tit} ---------")
    for i in range(lin):
        for j in range(col):
            print(f"{matriz[i][j]:>3}", end=" ")
        print()
    print()

# ------------------- Soma

print("\n-------------------- SOMA --------------------\n")

lin_a = int(input("Linha da Matriz A: "))
col_a = int(input("Coluna da Matriz A: "))
lin_b = int(input("Linha da Matriz B: "))
col_b = int(input("Coluna da Matriz B: "))

if validacao(lin_a, lin_b, col_a, col_b):
    mat_a = []
    mat_b = []
    mat_c = []

    for i in range(lin_a):
        la = []
        lb = []
        lc = []
        for j in range(col_a):
            la.append(randint(1, 9))
            lb.append(randint(1, 9))
            lc.append(la[j] + lb[j])
        mat_a.append(la)
        mat_b.append(lb)
        mat_c.append(lc)

    print()
    exibir(lin_a, col_a, mat_a, "MATRIZ A")
    exibir(lin_a, col_a, mat_b, "MATRIZ B")
    exibir(lin_a, col_a, mat_c, "MATRIZ SOMA (A + B)")
else:
    print("\n>>> Nao existe soma <<<\n")

# ------------------- Subtracao

print("\n-------------------- SUBTRACAO --------------------\n")

lin_a = int(input("Linha da Matriz A: "))
col_a = int(input("Coluna da Matriz A: "))
lin_b = int(input("Linha da Matriz B: "))
col_b = int(input("Coluna da Matriz B: "))

if validacao(lin_a, lin_b, col_a, col_b):
    mat_a = []
    mat_b = []
    mat_c = []

    for i in range(lin_a):
        la = []
        lb = []
        lc = []
        for j in range(col_a):
            la.append(randint(1, 9))
            lb.append(randint(1, 9))
            lc.append(la[j] - lb[j])
        mat_a.append(la)
        mat_b.append(lb)
        mat_c.append(lc)

    print()
    exibir(lin_a, col_a, mat_a, "MATRIZ A")
    exibir(lin_a, col_a, mat_b, "MATRIZ B")
    exibir(lin_a, col_a, mat_c, "MATRIZ SUBTRACAO (A - B)")
else:
    print("\n>>> Nao existe subtracao <<<\n")

# ------------------- Multiplicacao

print("\n-------------------- MULTIPLICACAO --------------------\n")

lin = int(input("Linha da Matriz: "))
col = int(input("Coluna da Matriz: "))
const = int(input("Constante: "))

mat_a = []
mat_b = []

for i in range(lin):
    la = []
    lb = []
    for j in range(col):
        la.append(randint(1, 9))
        lb.append(const * la[j])
    mat_a.append(la)
    mat_b.append(lb)

print()
exibir(lin, col, mat_a, "MATRIZ A")
exibir(lin, col, mat_b, "MATRIZ MULTIPLICACAO")