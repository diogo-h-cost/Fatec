import numpy as np

def det_2x2(matriz):
    if matriz.shape == (2, 2):
        return matriz[0, 0] * matriz[1, 1] - matriz[0, 1] * matriz[1, 0]
    else:
        return "A matriz deve ser 2x2"

def det_3x3(matriz):
    if matriz.shape == (3, 3):
        return (matriz[0, 0] * matriz[1, 1] * matriz[2, 2] +
                matriz[1, 0] * matriz[2, 1] * matriz[0, 2] +
                matriz[2, 0] * matriz[0, 1] * matriz[1, 2]) - (
                matriz[0, 2] * matriz[1, 1] * matriz[2, 0] +
                matriz[1, 0] * matriz[0, 1] * matriz[2, 2] +
                matriz[2, 1] * matriz[1, 2] * matriz[0, 0])
    else:
        return "A matriz deve ser 3x3"

def det_4x4(matriz):
    if matriz.shape == (4, 4):
        minor_00 = np.linalg.det(matriz[1:, 1:])
        minor_01 = np.linalg.det(np.delete(np.delete(matriz, 0, axis=0), 1, axis=1))
        minor_02 = np.linalg.det(np.delete(np.delete(matriz, 0, axis=0), 2, axis=1))
        minor_03 = np.linalg.det(np.delete(np.delete(matriz, 0, axis=0), 3, axis=1))

        return (matriz[0, 0] * minor_00 -
                matriz[0, 1] * minor_01 +
                matriz[0, 2] * minor_02 -
                matriz[0, 3] * minor_03)
    else:
        return "A matriz deve ser 4x4"

matriz_2x2 = np.array([[1, 2], [3, 4]])
matriz_3x3 = np.array([[2, 4, 1], [0, 3, -2], [-3, 2, 1]])
matriz_4x4 = np.array([[4, 5, -3, 0], [2, -1, 3, 1], [1, -3, 2, 1], [0, 2, -2, 5]])

print(f"\nDeterminante 2x2: {det_2x2(matriz_2x2):.2f}\n")
print(f"Determinante 3x3: {det_3x3(matriz_3x3):.2f}\n")
print(f"Determinante 4x4: {det_4x4(matriz_4x4):.2f}\n")