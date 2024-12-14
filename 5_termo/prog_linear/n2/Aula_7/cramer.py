def matriz():
    mat = []
    let = ["X", "Y", "B"]
    for i in range(2): # 2x Linhas
        lis = [] # Linha
        for j in range(3): # 3x Itens em cada linha
            val = int(input(f"Insira Linha[{i + 1}] {let[j]}: "))
            lis.append(val)
            if i == 0 and j == 2:
                print()
        mat.append(lis)
    return mat

def det_d(mat):
    l1 = mat[0]
    l2 = mat[1]
    return (l1[0] * l2[1]) - (l1[1] * l2[0])

def det_dx(mat):
    l1 = mat[0]
    l2 = mat[1]
    return (l1[2] * l2[1]) - (l1[1] * l2[2])

def det_dy(mat):
    l1 = mat[0]
    l2 = mat[1]
    return (l1[0] * l2[2]) - (l1[2] * l2[0])

def calc_xy(d, dx, dy):
    return (dx / d, dy / d)

vez = int(input("\nQuantos calculos: "))
for i in range(vez):
    print(f"\n>> {i + 1}º Calculo\n")
    mat = matriz()
    d = det_d(mat)
    dx = det_dx(mat)
    dy = det_dy(mat)

    if d != 0:
        x, y = calc_xy(d, dx, dy)
        print("\nSistema Possivel e Determinado (SPD)")
        print(f"X: {x:.2f} | Y: {y:.2f}\n")
    elif dx == 0 and dy == 0:
        print("\nSistema Possivel e Indeterminado (SPI)")
        print(f"D: {d:.2f} | Dx: {dx:.2f} | Dy: {dy:.2f}\n")
    else:
        print("\nSistema Impossivel (SI)")
        print(f"D: {d:.2f} | Dx: {dx:.2f} | Dy: {dy:.2f}\n")
    print(20 * "-")