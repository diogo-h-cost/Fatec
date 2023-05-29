"""
Dado um arquivo contendo um conjunto de nome e data de nascimento (dd mm aa, isto é, 3
inteiros seguidos), construir outro arquivo contendo o nome e a idade.
O programa deve ler além do nome do arquivo a ser lido, a data de hoje.
"""

arqui = input()
data = input("Data: ")

try:
    with open(arqui, "r") as fil1:
        with open("saida-06.txt", "w") as fil2:
            dados = fil1.readlines()
            for i in dados:
                df = i.split(" ")
                dt = df[1:]
                dn, mn, an = dt
                dn, mn, an = int(dn), int(mn), int(an)
                dh, mh, ah = data.split(" ")
                dh, mh, ah = int(dh), int(mh), int(ah)
                idade = ah - an
                if mn > mh:
                    idade -= 1
                elif mn == mh and dn > dh:
                    idade -= 1
                print(f"{df[0]} - {idade} anos")
                fil2.write(f"{df[0]};{idade}")
except FileNotFoundError:
    print("Arquivo nao encontrado")