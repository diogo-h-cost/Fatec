"""
                             >> Sistema de Login <<

Faça um programa em Python que permita o usuário criar um login ou entrar no sistema.

> Para criar um login, o usuário deverá informar um nome, o qual deverá ser consultado se já não
existe gravado no arquivo. Se existir, emita uma mensagem de “Usuário existente”. Se não existir,
permita que ele entre com a senha e grave no arquivo texto o login e a senha (criptografada).

> Para entrar no sistema, o usuário deverá entrar com o login e com a senha. O sistema deverá
informar “Acesso liberado” ou “Acesso negado”. Verificar no arquivo se o login existe e se existir,
de criptografar a senha para comparar com a senha informada. Se o usuário ou a senha estiverem
incorretas o acesso será negado, caso contrário, o acesso será liberado.
"""

def barra():
    print("=" * 25)

def criptografar(senha):
    senh = ""
    for i in senha:
        senh += str(ord(i))
    cripto = senh[::-1]
    return cripto

def cadas_senha(user):
    with open("sistema.txt", "a") as fil2:
        senha = input("Informe a senha: ")
        sen_crip = criptografar(senha)
        print(">> Usuário cadastrado <<".center(25))
        fil2.write(f"{user};{sen_crip}\n")

def cadastrar():
    user = input("Informe o usuário: ")
    with open("sistema.txt", "r") as arq:
        for i in arq:
            usr, sen = i.split(";")
            if user == usr:
                return print("!! Usuário existente !!".center(25))
        return cadas_senha(user)

def acesso():
    with open("sistema.txt", "r") as arq:
        user = input("Informe o usuário: ")
        senha = input("Informe a senha: ")
        senha_cript = criptografar(senha)
        for i in arq:
            usr, sen = i.split(";")
            sen_sist = sen.strip('\n')
            if user == usr and senha_cript == sen_sist:
                return print(">> Acesso liberado <<".center(25))
        return print("!! Acesso negado !!".center(25))

while True:
    barra()
    print("MENU".center(25))
    op = input("1 -> Entrar no sistema\n"
               "2 -> Cadastrar\n"
               "3 -> Stop\n"
               "Escolha >> ")
    if op == "3":
        break
    if op == "1":
        barra()
        acesso()

    elif op == "2":
        barra()
        cadastrar()
    else:
        barra()
        print("Escolha entre 1 ou 2")