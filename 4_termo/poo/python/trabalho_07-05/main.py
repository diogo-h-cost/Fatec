from classe import Estado

def inspecionar(est, cap, lis):
    if len(lis) == 0:
        return False
    else:
        for item in lis:
            for key, value in item.items():
                if key == est or value == cap:
                    return True
                return False

def create(lis):
    est = input("Estado: ").upper()
    cap = input("Capital: ").upper()
    if inspecionar(est, cap, lis) == False:
        lis.append({est: cap})
        est = Estado(est, cap)
        lis_obj.append(est)
        return "\nCriado com sucesso\n"
    else:
        return "\n>> Já está Armazenado <<\n"

def read(lis, lis_obj):
    if len(lis) > 0:
        print("ESTADO | CAPITAL\n")
        for item in lis:
            for key, value in item.items():
                print(f"{key} | {value}")
        print(f"\nLista: {lis}\n")
        print(f"lista de objetos: {lis_obj}\n")
    else:
        print(">> Vazio <<\n")

def update(lis, lis_obj):
    est = input("Estado: ").upper()
    cap = input("Capital [update]: ").upper()
    for item in lis:
        for key in item.keys():
            if key == est:
                item[key] = cap
    for i in lis_obj:
        if i.sigla == est:
            i.capital = cap
            return "\nUpdate realizado\n"
    return "\n>> Update não realizado <<\n"

def delete(lis, lis_obj):
    est = input("Estado: ").upper()
    for pos, item in enumerate(lis):
        for key in item.keys():
            if key == est:
                lis.pop(pos)
                for obj in lis_obj:
                    if obj.sigla == est:
                        lis_obj.remove(obj)
                return "\nDelete realizado\n"
    return "\n>> Delete não realizado <<\n"

lis = []
lis_obj = []
cont = True
while cont:
    print("-" * 25)
    print("MENU".center(25))
    print("+" * 25)
    print("1. Create\n"
          "2. Read All\n"
          "3. Update\n"
          "4. Delete\n"
          "5. Sair\n")
    esc = int(input("Escolha: "))
    print("+" * 25)
    if esc == 1:
        print("Create\n".center(25))
        print(create(lis))
    elif esc == 2:
        print("Read All\n".center(25))
        read(lis, lis_obj)
    elif esc == 3:
        print("Update\n".center(25))
        print(update(lis, lis_obj))
    elif esc == 4:
        print("Delete\n".center(25))
        print(delete(lis, lis_obj))
    elif esc == 5:
        print("Sair".center(25))
        print("-" * 25)
        break
    else:
        print(">> ERRO [1 - 4] <<")