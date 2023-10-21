def head_rol():
    print("\033[1m\033[3m\033[92m")
    print("=" * 40)
    print(" Insira o ROL (0 -> Sair)".center(40))
    print("=" * 40)
    print("\033[0m")

def povoa_rol():
    i = 1
    dici = {}
    while True:
        num = int(input(f"\033[34m Elemento {i}: \033[0m"))
        if num == 0:
            break
        elif num in dici:
            dici[num] += 1
        else:
            dici[num] = 1
        i += 1
    return dici

def cabecalho_rol():
    print("\033[1m\033[3m\033[93m")
    print("=" * 40)
    print("ROL".center(40))
    print("=" * 40)
    print("\033[0m")

def exibe_rol(elementos):
    cont = 0
    elem_ord = sorted(elementos.items())
    for itens in elem_ord:
        key, value = itens
        for i in range(value):
            print(key, end=' ')
            cont += 1
            if cont % 5 == 0:
                print()
    print()

def menu():
    print("\033[1m\033[3m\033[36m")
    print("-" * 40)
    print("MENU".center(40))
    print("-" * 40)
    print("\033[0m")
    print("CALCULAR:\n"
          "\n1. Média\n" 
          "2. Moda\n"
          "3. Mediana\n"
          "4. Gerar todas\n")
    esc = int(input("Escolha -> "))
    print()
    return esc

def calc_media(elementos):
    multip = []
    for xi, fi in elementos.items():
        multip.append(xi * fi)
    return sum(multip) / sum(elementos.values())

def calc_moda(elementos):
    maior = max(elementos.values())
    modas = [key for key in elementos.keys() if elementos[key] == maior]
    return modas

def exibe_moda(moda):
    if len(moda) > 1:
        for ind, mod in enumerate(moda):
            print(f"MO{ind + 1} = {mod}")
        print()
    else:
        print(f"MO = {moda[0]}\n")

def cal_mediana(elementos):
    lista = []
    for key, values in elementos.items():
        for i in range(values):
            lista.append(key)
    lista.sort()
    meio = len(lista) // 2
    if len(lista) % 2 == 0:
        m1 = lista[meio - 1]
        m2 = lista[meio]
        return (m1 + m2) / 2
    else:
        return lista[int(meio)]
    
def laco():
    print("\033[1m\033[3m\033[32m")
    print("+" * 40)
    print("Deseja realizar outra vez?".center(40))
    print("+" * 40)
    print("\033[0m")
    print("\n1. SIM\n"
          "2. NÂO\n")
    laco = int(input("Escolha -> "))
    esc = True if laco != 1 else False
    return esc

while True:
    head_rol()
    elementos = povoa_rol()
    cabecalho_rol()
    exibe_rol(elementos)

    esc = menu()
    if esc == 1:
        print("-" * 20)
        print("\033[1m\033[3m\033[93m \nSeleciado: MÉDIA.\n \033[0m")
        media = calc_media(elementos)
        print(f"Média = {media:.2f}\n")
    elif esc == 2:
        print("-" * 20)
        print("\033[1m\033[3m\033[93m \nSeleciado: MODA.\n \033[0m")
        moda = calc_moda(elementos)
        exibe_moda(moda)
    elif esc == 3:
        print("-" * 20)
        print("\033[1m\033[3m\033[93m \nSeleciado: MEDIANA.\n \033[0m")
        mediana = cal_mediana(elementos)
        print(f"Mediana = {mediana:.2f}\n")
    elif esc == 4:
        print("-" * 20)
        print("\033[1m\033[3m\033[93m \nSeleciado: MÉDIA, MODA, MEDIANA.\n \033[0m")

        media = calc_media(elementos)
        print(f"\nMédia = {media:.2f}\n")

        moda = calc_moda(elementos)
        exibe_moda(moda)

        mediana = cal_mediana(elementos)
        print(f"Mediana = {mediana:.2f}\n")
    else:
        print("\033[1m\033[3m\033[31m >>>>> Opção invalida!!, escolha 1. Média, 2. Moda ou 3. Mediana 4. Gerar todas <<<<<\033[0m\n")

    repet = laco()
    if repet:
        break