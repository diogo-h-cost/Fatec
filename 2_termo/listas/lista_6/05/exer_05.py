"""
Faça um programa que permita que o usuário entre com diversos nomes e telefones para cadastro, e
crie um arquivo com essas informações, uma por linha.
"""

with open("cadast-05.txt", "a") as file:
    while True:
        print("=" * 25)
        esc = input("1 -> Stop\n"
              "2 -> Cadastrar\n"
              "Escolha >> ")
        if esc == "1":
            break
        else:
            print("=" * 25)
            nom = input("Nome: ")
            num = input("Numero: ")
            file.write(f"{nom};{num}\n")