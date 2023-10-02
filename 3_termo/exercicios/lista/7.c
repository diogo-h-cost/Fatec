#include <stdio.h>
#define ano_atual 2023

int main()
{
	int ano_nas, a, b, c;
	
	printf("Ano nascimento: ");
	scanf("%d", &ano_nas);
	
	a = ano_atual - ano_nas;
	b = (a * 365) / 7;
	c = 2028 - ano_nas;
	
	printf("Idade: %d ano(s)\nIdade em semanas: %d semana(s)\nIdade em 2028: %d ano(s)\n", a, b, c);
	
	return 0;
}