def entrada():
    lin = int(input("Linhas: "))
    col = int(input("Colunas: "))

    return lin, col # Retorna uma tupla (lin, col)

def impressao(lin, col, matriz):
    for i in range(lin):
        for j in range(col):
            print(f"{matriz[i][j]:^3}", end = " | ")
        print()

def top(msg):
    print(f"\n-------------- {msg} --------------\n")

def formula_1(lin, col):
    matriz = []
    for i in range(1, lin + 1):
        linhas = []
        for j in range(1, col + 1):
            form = (3 * i) - j ** 2
            linhas.append(form)
        matriz.append(linhas)
    return matriz

def formula_2(lin, col):
    matriz = []
    for i in range(1, lin + 1):
        linhas = []
        for j in range(1, col + 1):
            if i == j:
                form = 2 * i - 3 * j
            else:
                form = 4 * i + 5 * j
            linhas.append(form)
        matriz.append(linhas)
    return matriz

def formula_3(lin, col):
    matriz = []
    for i in range(1, lin + 1):
        linhas = []
        for j in range(1, col + 1):
            if i == j:
                form = i * j
            elif i > j:
                form = i + j
            else:
                form = i - j
            linhas.append(form)
        matriz.append(linhas)
    return matriz

while True:
    print("\n\n\033[34m+++++++++++++++\033[0m \033[4mMATRIZES POR FORMULAS\033[0m \033[34m+++++++++++++++\033[0m\n")
    esc = int(input("""1- Formula \033[32munica\033[0m
2- Formula (\033[32mi = j\033[0m) \033[31m|\033[0m (\033[32mi != j\033[0m)
3- Formula (\033[32mi = j\033[0m) \033[31m|\033[0m (\033[32mi > j\033[0m) \033[31m|\033[0m (\033[32mi < j\033[0m)
4- Sair

\033[35mOpcao: \033[0m"""))
    match esc:
        case 1:
            top("\033[33mFormula:\033[0m \033[36m3.i-j²\033[0m")
            lin, col = entrada()
            matriz = formula_1(lin, col)
            top("MATRIZ")
            impressao(lin, col, matriz)
        case 2:
            top("\033[33mFormula:\033[0m (\033[32mi = j\033[0m) \033[36m2.i-3.j\033[0m | (\033[32mi != j\033[0m) \033[36m4.i+5.j\033[0m")
            lin, col = entrada()
            matriz = formula_2(lin, col)
            top("MATRIZ")
            impressao(lin, col, matriz)
        case 3:
            top("\033[33mFormula:\033[0m (\033[32mi = j\033[0m) \033[36mi.j\033[0m | (\033[32mi > j\033[0m) \033[36mi+j\033[0m | (\033[32mi < j\033[0m) \033[36mi-j\033[0m")
            lin, col = entrada()
            matriz = formula_3(lin, col)
            top("MATRIZ")
            impressao(lin, col, matriz)
        case 4:
            print("\n\033[31mSaindo .....\033[0m\n")
            break
        case _:
            print("\n\033[36m>>> ERRO [1 - 4] apenas <<<\033[0m")