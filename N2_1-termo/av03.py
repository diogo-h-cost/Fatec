ger = []
a = [0, 1, 2, 3, 4, 5, 6] # limitador de 0 a 6 (entrada)
b = 0 # Total de votos
sis = ["Windows XP", "Unix", "Linux", "Netware", "Mac os", "Outros"]

print("\nQual o melhor Sistema operacional para uso em servidores ?\n")

while True:
    print("1-Windows XP, 2-Unix, 3-Linux, 4-Netware, 5-Mac os, 6-Outros, 0-Stop: ")
    vot = int(input("Voto: "))
    print()
    if vot not in a:
        print("Número Invalido")
    elif vot == 0:
        break
    else:
        ger.append(vot)
        b += 1

total = [0] * 6 # Quantidade de vezes c/ num
ma = 0
for i in range(1, 7):
    for j in range(len(ger)):
        if ger[j] == i:
            total[i-1] += 1 # total = quantas vezes cada foi sorteado posição
    if total[i-1] >= total[ma]:
        ma = i-1

print("Sistema operacional - votos - %")
for f in range(6):
    print(f"{sis[f]} - {total[f]} - {(total[f] / b) * 100:.0f} %")

print(f"\nTotal de {b} votos")
print(f"O Sistema Operacional mais votado foi o {sis[ma]}, com {total[ma]} votos, correspondendo a {total[ma] / b * 100:.0f} % dos votos")