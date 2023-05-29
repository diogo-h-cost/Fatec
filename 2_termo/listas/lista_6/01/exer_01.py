"""
Considere o arquivo notas_estudantes.txt que contém uma linha para cada aluno de uma turma de
estudantes. O nome de cada estudante está no início de cada linha e é seguido pelas suas notas.

jose 10 15 20 30 40
pedro 23 16 19 22
suzana 8 22 17 14 32 17 24 21 2 9 11 17
gisela 12 28 21 45 26 10
joao 14 32 25 16 89

>> Usando o arquivo texto notas_estudantes.txt escreva uma função que imprime o nome dos alunos
que têm mais de seis notas.

>> Usando o arquivo texto notas_estudantes.txt escreva uma função que calcula a média das notas de
cada estudante e imprime o nome e a média de cada estudante.

>> Usando o arquivo texto notas_estudantes.txt escreva uma função que calcula a nota mínima e
máxima de cada estudante e imprima o nome de cada aluno junto com a sua nota máxima e mínima.
>> No principal, chame as funções
"""

def mais6():
    arq.seek(0)
    for i in arq:
        ta = i.split()
        if len(ta) > 7:
            print(f">>> {ta[0]}")

def med():
    arq.seek(0)
    for i in arq:
        ta = i.split()
        l = []
        for j in ta[1:]:
            l.append(float(j))
        print(f"{ta[0]} >> {sum(l)/len(l):.1f}")

def minmax():
    arq.seek(0)
    for i in arq:
        ta = i.split()
        l = [] # ou l = list(map(float, ta[1:]))
        for j in ta[1:]: #
            l.append(float(j)) #
        print(f"{ta[0]} >> MIN - {min(l)} // MAX - {max(l)}")

with open("notas_estudantes(1).txt", "r") as arq:
    try:
        print("="*10)
        print("Alunos c/ + de 6 notas\n")
        mais6()
        print("=" * 10)
        print("Alunos e medias\n")
        med()
        print("=" * 10)
        print("Aluno e nota max e min\n")
        minmax()
    except FileNotFoundError:
        print("Nao tem arquivo")