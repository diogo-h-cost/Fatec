"""
>> Número por extenso <<

Escreva um programa que solicite ao usuário a digitação de um número até 99 
e imprima-o na tela por extenso. Utilizar funçãoe lista.
"""

def extenso(num):
    dec = ["Dez", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]
    uni = ["um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    onz = ["Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]

    ext = ""

    if num >= 11 and num <= 19:
        on = num % 10
        ext = onz[on - 1]
    else:
        deci = num // 10
        unit = num % 10
        if unit == 0:
            ext = dec[deci - 1]
        elif deci == 0:
            ext = uni[unit - 1]
        else:
            ext = dec[deci - 1] + " e " + uni[unit - 1]
    return ext

num = int(input("Insira [1..99]: "))
if num >= 1 and num <= 99:
    print(f"\nNumero por extenso: {extenso(num).upper()}")
else:
    print("Digite um numero de 1 ate 99")