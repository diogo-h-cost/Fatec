"""
>> Jogo da palavra embaralhada <<

Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que 
será mostrada com as letras  embaralhadas(utilize  funçãoparaembaralhar  a  palavra).  
O  programa  terá  uma  lista  de palavras e deverá sortear uma palavra aleatoriamente. 
O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada 
na tela, informando  se  o  usuário  ganhou  ou  perdeu  o  jogo.
Se  o  jogador  acertar  a  palavra  antes  das  seis tentativas, pode encerrar o jogo.
"""

from random import randint, shuffle
pal = ["CADERNO", "GELADEIRA", "PYTHON", "PRODESK", "APLICATIVO", "FAVORITO", "PALAVRA"]

indic = randint(0, len(pal)-1)
sorteada = pal[indic]

def embaralha(palavra):
    trocada = list(palavra)
    shuffle(trocada)
    return "".join(trocada)

inversa = embaralha(sorteada)
print(f"Palavra embaralhada : {inversa}")

tent = 0
while tent != 6:
    letr = input("Insira: ").upper()
    if letr == sorteada:
        print(f"\nPalavra acertada: {sorteada}")
        print("GANHOU O JOGO!!!")
        break
    else:
        tent += 1
        print(f"\nTentativas restantes: {6-tent}")
        if tent == 6:
            print(f"\nPalavra certa: {sorteada}")
            print("PERDEU O JOGO!!!")