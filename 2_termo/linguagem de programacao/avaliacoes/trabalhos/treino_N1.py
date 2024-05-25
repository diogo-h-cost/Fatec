"""
Elabore um programa em Python com uma função que receba uma string por parâmetro, contendo um número. A função deve
retornar a soma dos algarismos desse número. Peça a entrada da string contendo o número (como string), chame a função e imprima a soma.
"""

def gener(a):
    l = []
    for i in a:
        l.append(int(i))
    return sum(l)

stri = input()
print(f"A soma dos algarismos {stri} == {gener(stri)}")

"""
Escreva um programa em Python que tenha uma função que receba por parâmetro a quantidade de votos 
em uma eleição entre 3 candidatos e a quantidade de votos de cada candidato. 
A função deverá retornar True 
caso a eleição deva ter segundo turno ou False se não haverá segundo turno. 
Para não ter o segundo turno, 
o mais votado deve ter mais do que 50% da quantidade de votos totais.
Peça a entrada da quantidade dos votos e imprima se haverá ou não o segundo turno da eleição. 
Não precisa validar a entrada dos votos.
"""

def verif(vot, c1, c2, c3):
    venc = max(c1, c2, c3)
    if venc > ((50/100)*vot):
        return False
    return True

vot = int(input("Quantidade de votos -> "))
c1 = int(input("Candidato 1º -> "))
c2 = int(input("Candidato 2º -> "))
c3 = int(input("Candidato 3º -> "))

print(f"Tera segundo turno == {verif(vot, c1, c2, c3)}")

"""
Uma biblioteca distribui um cartão magnético para que os alunos possam frequentá-la. 
A senha inicial, enviada pelo correio, é gerada automaticamente a partir da data de nascimento do aluno ('dd/mm/aaaa') do seguinte modo:
dd+'$'+mm(invertido) + '#' + mm+'!'+dd(invertido) + '\'+aaaa

Exemplo:
Data de nascimento: 25/10/1995
25 $ 01 # 10 ! 52 \ 1995

Escreva um programa em Python leia a data de nascimento e crie uma variável com a senha de acordo com as regras acima. 
Imprima a senha.
"""

def senh(d, m, a):
    mm = m[::-1]
    dd = d[::-1]
    alt = [d, mm, m, dd, a]
    l = ["", "$", "", "#", "", "!", "", "\\", ""]
    i = x = 0
    while i <= len(l):
        l[i] = alt[x]
        i += 2
        x += 1
    return "".join(l)

d, m, a = input("Data de nascimento: ").split("/")
print(senh(d, m, a))

# >>> OU <<<

def senh(d, m, a):
    senha = d + "$" + m[::-1] + "#" + m + "!" + d[::-1] + "\\" + a
    return senha

d, m, a = input("Data de nascimento: ").split("/")
print(senh(d, m, a))

"""
Elabore um programa em Python com que armazene 6 notas em uma lista. 
O programa deve calcular a média desses valores, descontando a menor e a maior nota da lista.
A lista pode ser gerada aleatoriamente ou pedir a entrada dos valores.
"""

from random import randint
l = []
for i in range(6):
    l.append(randint(0, 10))

l.remove(min(l))
l.remove(max(l))
med = sum(l) / len(l)
print(f"Notas -> {l}")
print(f"Média das notas -> {med:.2f}")