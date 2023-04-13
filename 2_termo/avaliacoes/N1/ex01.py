"""
Faça um programa em Pythoncom uma função que receba como parâmetro uma string e imprima os caracteres repetidos contidos na string.

Ex.: 
Entrada: Renata  Saída: a a
Entrada: arvore  Saída: r r
Entrada: carrossel  Saída: r r s s
Entrada: estante  Saída: e t t e
Entrada: brasileira  Saída: r a i i r a

No programa principal, peçaa stringechame a função.
"""

def repet(stri):
    sai = " "
    st = list(stri)
    for i in range(len(stri)):
        if stri.count(st[i]) >= 2:
            sai += st[i] + " "
    print(sai)

stri = input().upper()
repet(stri)