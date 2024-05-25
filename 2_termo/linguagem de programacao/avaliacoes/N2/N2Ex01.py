def media(lista):
    lista.remove(max(lista))
    lista.remove(min(lista))
    med = sum(lista) / len(lista)
    return med

lista = []
print("INSIRA AS NOTAS\n".center(25))
for i in range(6):
    nota = float(input(f"Insira a nota {i+1}: "))
    lista.append(nota)
print(f"\nMedia = {media(lista):.2f}")