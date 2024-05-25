"""
>> A linguagem do P <<

Elabore um programa em Python que leia uma string contendo uma mensagem codificada na linguagem do
P. A string contém a letra 'p' minúscula antes de cada letra da palavra. O programa deve exibir a mensagem
decodificada.

Um exemplo de mensagem codificada e a respectiva mensagem decodificada é mostrada abaixo.

-> Mensagem codificada: pVpapmpops papo pcpipnpepmpa
-> Mensagem decodificada: Vamos ao cinema

Obs.: Não precisa validar a entrada.
"""

frase = input("Frase codificada -> ").upper().strip() #Tira o espaço da palavra
frase = frase.replace("PP", "P*")
frase = frase.replace("P", "")
frasedec = frase.replace("*", "P")
print(f"Frase decodificada -> {frasedec}")

"""
>> Senha <<

Faça um programa que peça o cadastro de uma senha. Faça a validação, 
imprimindo “Senha válida” ou
“Senha inválida”. Para validar a senha, ela tem que ter exatamente 8 caracteres, 
sendo pelo menos 1 letra
maiúscula, 1 número e 1 caractere especial.

Exemplos de senhas válidas

Ren@ta21
Progr@3@
test3SE!
prof@Un1

Faça uma função que sugira uma senha válida aleatória. Chame essa função caso a senha 
digitada pelo
usuário seja inválida.

Obs.: Crie quantas funções achar necessário para validar a senha
"""

# >>> CODIGO EM COMENTARIO PORQUE TEM QUE IMPORTAR TERMCOLOR <<<<<

"""
from random import randint, choice, sample
from termcolor import colored

def geraSenha():
    ce = ['@','&','!','#','%','*','?']
    #ce = string.punctuation
    senha = chr(randint(65,90))
    senha += str(randint(0,9))
    senha += choice(ce)
    for i in range(2):
        senha += str(randint(0,9))
    for i in range(3):
        senha += chr(randint(97,122))
    senha = ''.join(sample(senha, len(senha)))
    return senha

def validaSenha():
    if len(senha) != 8:
        return False
    contM = contN = contCE = 0
    for c in senha:
        if c.isupper():
            contM += 1
        elif c.isdigit():
            contN += 1
        elif not c.isalnum():
            contCE += 1
    if contM == 0 or contN == 0 or contCE == 0:
        return False
    return True

print("~" * 44)
senha = input('Insira uma senha de 8 caracteres >> ')
print("~" * 44)
if validaSenha():
    print(colored("Senha cadastrada com sucesso!!","blue"))
else:
    print(colored("Senha inválida!!","red"))
    senha = geraSenha()
    print("~" * 44)
    print(f"Senha gerada aleatoriamente >> {senha}")
"""

"""
>> Conversão de bases <<

Fazer um programa em Python para transformar números de uma base qualquer para qualquer outra
base, considere as bases binária, octal, decimal e hexadecimal.

Faça quantas funções precisar, mas apenas 2 para as conversões.

O programa deverá fazer a entrada de dados, pedindo a base de origem, o número e a base destino.
Exiba o resultado.

Faça sempre a validação de entrada, para que o número esteja correto para a base de origem informada.
"""

def validaEntrada(num,base):
    for i in range(len(num)):
        if base == 16:
            if num[i] not in aldigit:
                return False
        else:
            if int(num[i]) >= base:
                return False
    return True

def decToqq(num,base):
    l = []
    num = int(num)
    while num != 0:
        l.append(aldigit[num % base])
        num //= base
    l = l[::-1]
    num = "".join(l)
    return num

def qqTodec(num,base):
    dec = 0
    j = len(num)-1
    for i in range(len(num)):
        dec += aldigit.index(num[i]) * base ** j
        j -= 1
    return dec

aldigit = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

baseO = int(input("Informe a base inicial: "))
while True:
    numero = input("Informe o número que deseja converter: ").upper()
    if baseO == 16:
        if numero.isalnum() and validaEntrada(numero, baseO):
            break
        else:
            print(f"Números inválidos para a base {baseO}")
    elif numero.isdigit():
        if validaEntrada(numero, baseO):
            break
        else:
            print(f"Números inválidos para a base {baseO}")
    else:
        print("Informe apenas números")

baseD = int(input("Informe a base final: "))
if baseO != 10 and baseD != 10:
    dec = qqTodec(numero,baseO)
    conv = decToqq(dec,baseD)
elif baseO == 10:
    conv = decToqq(numero,baseD)
else:
    conv = qqTodec(numero, baseO)

print(f"O número {numero} na base {baseO} é {conv} na base {baseD}")

"""
>> Texto embaralhado <<

Observe o texto abaixo 

                        De aorcdo com uma peqsiusa
                        de uma uinrvesriddae ignlsea,
                        não ipomtra em qaul odrem as
                        Lteras de uma plravaa etãso,
                        a úncia csioa iprotmatne é que
                        a piremria e útmlia Lteras etejasm
                        no lgaur crteo. O rseto pdoe ser
                        uma bçguana ttaol, que vcoê
                        anida pdoe ler sem pobrlmea.
                        Itso é poqrue nós não lmeos
                        cdaa Ltera isladoa, mas a plravaa
                        cmoo um tdoo.
                        Sohw de bloa.

Faça um programa em Python que leia um texto e para cada palavra maior de 3 letras, conserve a
primeira e a última letra no mesmo lugar e embaralhe as letras no interior da palavra. Pode-se apenas
inverter as letras de posição como nos exemplos:

Renata >> Rnetaa                  Linguagem >> Lniuggaem
"""

from random import shuffle

textoI = input('Texto -> ')
listaT = textoI.split()

for i,palavra in enumerate(listaT):
    if len(palavra) > 3:
        embaralhado = list(palavra[1:len(palavra)-1])
        shuffle(embaralhado)
        embaralhado = palavra[0] + ''.join(embaralhado) + palavra[-1]
        listaT[i] = embaralhado
textoE = ' '.join(listaT)
print(textoE)