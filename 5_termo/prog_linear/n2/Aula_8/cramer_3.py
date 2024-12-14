def matriz():
    mat = []
    let = ["X", "Y", "Z", "B"]
    for i in range(3): # 3x Linhas
        lis = [] # Linha
        for j in range(4): # 4x Itens em cada linha
            val = int(input(f"Insira Linha[{i + 1}] {let[j]}: "))
            lis.append(val)
            if j == 3:
                print() # Pular linha entre os append
        mat.append(lis)
    return mat

def det_d(mat):
    l1 = mat[0]
    l2 = mat[1]
    l3 = mat[2]
    return ((l1[0]*l2[1]*l3[2]) + (l1[1]*l2[2]*l3[0]) + (l1[2]*l2[0]*l3[1])) - ((l1[2]*l2[1]*l3[0]) + (l1[0]*l2[2]*l3[1]) + (l1[1]*l2[0]*l3[2]))

def det_dx(mat):
    l1 = mat[0]
    l2 = mat[1]
    l3 = mat[2]
    return ((l1[3]*l2[1]*l3[2]) + (l1[1]*l2[2]*l3[3]) + (l1[2]*l2[3]*l3[1])) - ((l1[2]*l2[1]*l3[3]) + (l1[3]*l2[2]*l3[1]) + (l1[1]*l2[3]*l3[2]))

def det_dy(mat):
    l1 = mat[0]
    l2 = mat[1]
    l3 = mat[2]
    return ((l1[0]*l2[3]*l3[2]) + (l1[3]*l2[2]*l3[0]) + (l1[2]*l2[0]*l3[3])) - ((l1[2]*l2[3]*l3[0]) + (l1[0]*l2[2]*l3[3]) + (l1[3]*l2[0]*l3[2]))

def det_dz(mat):
    l1 = mat[0]
    l2 = mat[1]
    l3 = mat[2]
    return ((l1[0]*l2[1]*l3[3]) + (l1[1]*l2[3]*l3[0]) + (l1[3]*l2[0]*l3[1])) - ((l1[3]*l2[1]*l3[0]) + (l1[0]*l2[3]*l3[1]) + (l1[1]*l2[0]*l3[3]))

def calc_xyz(d, dx, dy, dz):
    return (dx/d, dy/d, dz/d)

print("\n>>> REGRA DE CRAMER 3x3 <<<\n")
vez = int(input("Quantos calculos: "))
for i in range(vez):
    print(f"\n>> {i + 1}º Calculo\n")
    mat = matriz()
    d = det_d(mat)
    dx = det_dx(mat)
    dy = det_dy(mat)
    dz = det_dz(mat)

    if d != 0:
        x, y, z = calc_xyz(d, dx, dy, dz)
        print("\nSistema Possivel e Determinado (SPD)")
        print(f"X: {x:.2f} | Y: {y:.2f} | Z: {z:.2f}\n")
    elif dx == dy == dz == 0:
        print("\nSistema Possivel e Indeterminado (SPI)")
        print(f"D: {d:.2f} | Dx: {dx:.2f} | Dy: {dy:.2f} | Dz: {dz:.2f}\n")
    else:
        print("\nSistema Impossivel (SI)")
        print(f"D: {d:.2f} | Dx: {dx:.2f} | Dy: {dy:.2f} | Dz: {dz:.2f}\n")
    print(20 * "-")