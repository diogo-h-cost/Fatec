def entrada(stri): # funcao p/ o calculo do numero de cada entrada
    cont = 0
    if stri[0] == "*":
        cont += 4
    elif stri[1] == "*":
        cont += 2
    elif stri[2] == "*":
        cont += 1
    return cont

grito = 0
t = 0
while grito != 3: # enquanto grito for diferente de 3
    stri = input() # entrada
    if stri == "caw caw":
        print(t)
        grito += 1
        t = 0 # zera variavel T
    else:
        t += entrada(stri) # Acumula retorno da funcao