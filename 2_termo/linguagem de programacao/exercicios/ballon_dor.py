"""
>> Ballon d'Or <<

O prêmio Ballon d'Or (Bola de Ouro) foi criado pela revista France Football e premia o melhor jogador de futebol desde 1956. Entre 1956 e 1994, o prêmio era concedido apenas
para o futebol europeu, e a partir de 1995 passou a premiar o melhor jogador de futebol do mundo.

A votação é feita por jornalistas que devem indicar, em ordem, 5 jogadores no seu voto.

Para cada voto, é atribuído a seguinte pontuação aos jogadores:
• O primeiro lugar recebe 6 pontos;
• O segundo lugar recebe 4 pontos;
• O terceiro lugar recebe 3 pontos;
• O quarto lugar recebe 2 pontos;
• O quinto lugar recebe 1 ponto.

Desde 2018, a revista France Football também premia a melhor jogadora de futebol usandoum sistema de votação semelhante.

A revista France Football contratou você para criar um programa que recebe os votos de todos os jornalistas e imprime a classificação final da votação.

O seu programa receberá como entrada um inteiro n indicando a quantidade de votos e os n votos, sendo que cada voto consiste de 5 linhas contendo o nome dos jogadores,
onde a primeira linha do voto indica o primeiro colocado, a segunda linha indica o segundo colocado, e assim por diante.

Você deve imprimir a classificação da premiação, sendo que a i-ésima linha contém o nome e a pontuação do i-ésimo colocado na premiação.

Neste laboratório você não precisará se preocupar com casos de empate, a pontuação de todos os jogadores será distinta.
"""

dic = {}

lista = [6, 4, 3, 2, 1] # Pontos por posicao
num = int(input())
for i in range(num): # Quantidade de jornalista
    for j in range(5): # 5 Jogador por jornalista
        nome = input()
        dic[nome] = dic.get(nome, 0) + lista[j]
print()
for chav in sorted(dic, key = dic.get, reverse=True): # Ordena pelo valor (e inverte)
    print(f"{chav}: {dic[chav]}")