def top(msg):
    print(f"\n------------------- {msg.upper()} -------------------\n")

def conv_dict(item, opc):
    values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, '.': 27, '!': 28, '#': 29, '_': 30}
    if opc == 1: # Retorna VALUE
        return values[item]
    else: # Retorna KEY
        for key, value in values.items():
            if item == value:
                return key   

def troca(msg):
    msg_list = list(msg)
    for i in range(len(msg_list)):
        if msg_list[i] == ' ':
            msg_list[i] = '_'
    return ''.join(msg_list)

def exibe(matriz, col):
    for i in range(2):
        for j in range(col):
            print(f'{matriz[i][j]:>2}', end=' ')
        print()

def convert(matriz, col, opc):
    if opc == 1: # Converte MSG -> MATRIZ
        for i in range(2):
            for j in range(col):
                val = conv_dict(matriz[i][j], 1)
                matriz[i][j] = val
    else: # Converte MATRIZ -> MSG
        for i in range(2):
            for j in range(col):
                val = conv_dict(matriz[i][j], 2)
                matriz[i][j] = val
    return matriz

def cod_dec(mat1, mat2, col):
    mat_cod = [[0 for _ in range(col)] for _ in range(2)]
    for i in range(2):
        for j in range(col):
            soma = 0
            for k in range(2):
                soma += mat1[i][k] * mat2[k][j]
            mat_cod[i][j] = soma
    return mat_cod

# ------------------------------ Msg -> Matriz

top('mensagem')
msg = input("Mensagem: ").upper()

if len(msg) % 2 == 0:
    msg_new = troca(msg)

    meio = len(msg) // 2
    lin1 = list(msg_new[0:meio])
    lin2 = list(msg_new[meio:])

    top('matriz')
    matriz = [lin1, lin2]
    exibe(matriz, meio)

    top('matriz mensagem')
    matriz_new = convert(matriz, meio, 1)
    exibe(matriz_new, meio)
else:
    msg_new = troca(msg)

    meio = (len(msg) // 2) + 1
    lin1 = list(msg_new[0:meio])
    lin2 = list(msg_new[meio:] + '_')

    top('matriz')
    matriz = [lin1, lin2]
    exibe(matriz, meio)

    top('matriz mensagem')
    matriz_new = convert(matriz, meio, 1)
    exibe(matriz_new, meio)

# ------------------------------ Codificar Matriz

top('matriz codificada')
cod = [[3, 1], [2, 1]] # Matriz codificacao
mat_cod = cod_dec(cod, matriz_new, meio)
exibe(mat_cod, meio)

# ------------------------------ Decodificar Matriz

top('matriz decodificada')
dec = [[1, -1], [-2, 3]] # Matriz decodificacao
mat_dec = cod_dec(dec, mat_cod, meio)
exibe(mat_dec, meio)

top('matriz mensagem')
matriz_ori = convert(mat_dec, meio, 2)
exibe(matriz_ori, meio)
print()