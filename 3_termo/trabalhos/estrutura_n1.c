#include <stdio.h>

int main()
{
	int andar, pessoa, i, escolha, elevador;
	elevador = 0;
	
	printf("Numero de andares: ");
	scanf("%d", &andar);
	
	for (i = 1; i <= andar; i++) {
		printf("\nAndar -> %d\n", i);
		printf("Pessoa(s) no elevador -> %d\n", elevador);
		
		printf("Escolha 1- Sair ou 2- Entrar: ");
		scanf("%d", &escolha);
		
		printf("Numero de pessoas: ");
		scanf("%d", &pessoa);
		
		if (escolha == 1) {
			if ((elevador - pessoa) >= elevador && pessoa > 0)
				elevador -= pessoa;
			else
				printf("\nElevador Vazio!!!\n");
		}
		else if (escolha == 2) {
			if ((elevador + pessoa) <= 15 && pessoa > 0)
				elevador += pessoa;
			else if (pessoa > 0) {
				printf("\n>> Excesso de Passageiros <<\n");
				if (elevador == 15)
					printf("Deve sair %d pessoa(s)!!!\n", pessoa);
				else
					printf("Deve sair %d pessoa(s)!!!\n", (elevador + pessoa) - 15);
				elevador = 15;
			}
			else
				printf("\nErro numero negativo!!\n");
		}
		else
			printf("\nEscolha 1 ou 2!!\n");
	}
	
	printf("\nPermaneceram %d pessoa(s) para descer\n", elevador);
	
	return 0;
}