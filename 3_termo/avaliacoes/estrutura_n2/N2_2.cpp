#include <stdio.h>
#include <stdlib.h>

void tabuada(int &tab) {
	printf("Tabuada = ");
	scanf("%d", &tab);
}

int cal(int tab) {
	int i, soma;

	soma = 0;
	for (i = 1; i < 11; i++){
		soma += tab * i;
	}
	
	return soma;
}

main()
{
	int tab;
	
	tabuada(tab);
	
	if (tab >= 1 && tab <= 10)
		printf("\nSoma da Tabuada do %d = %d\n", tab, cal(tab));
	else
		printf(">>> Erro, fora da faixa de 1 a 10! <<<\n");
	
	system("pause");
}