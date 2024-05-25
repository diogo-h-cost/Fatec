from question_model import Questao
from data import dados_pergunta
from quiz_brain import Quiz_funcoes

banco_questoes = []
for questao in dados_pergunta:
    texto_questao = questao["question"]
    resposta_questao = questao["correct_answer"]
    nova_questao = Questao(texto_questao, resposta_questao)
    banco_questoes.append(nova_questao)

quiz = Quiz_funcoes(banco_questoes)

while quiz.ainda_tem_questoes():
    quiz.proxima_questao()

print("Você completou o Quiz")
print(f"Sua pontuação final é: {quiz.pontos} / {quiz.numero_questao}")