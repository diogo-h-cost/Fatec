def inicial():
    print()
    print("=" * 40)
    print("Insira o ROL (0 -> Sair)".center(40))
    print("=" * 40)
    print()

def povoa_rol():
    i = 1
    dici = {}
    while True:
        num = int(input(f"Elemento {i}: "))
        if num == 0:
            break
        elif num in dici:
            dici[num] += 1
        else:
            dici[num] = 1
        i += 1
    return dici

def cabecalho_rol():
    print()
    print("=" * 40)
    print("ROL".center(40))
    print("=" * 40)
    print()

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
            print(f"MO{ind + 1}: {mod}")
    else:
        print(f"MO: {moda[0]}")

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

# ------------------------------------------------------------ Programa

inicial()

elementos = povoa_rol()

cabecalho_rol()

exibe_rol(elementos)

media = calc_media(elementos)

moda = calc_moda(elementos)
exibe_moda(moda)

mediana = cal_mediana(elementos)

#Funcao MENU / if 1 chama tal / elif 2 chama tal / elif 3 chama tal / else 4 chama todas