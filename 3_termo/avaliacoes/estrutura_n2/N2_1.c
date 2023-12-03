#include <stdio.h>
#include <stdlib.h>

main()
{
	int i, acima;
	float seman[7], soma, maior;
	
	soma = 0;
	for (i = 0; i < 7; i++) {
		printf("Temperatura dia %d= ", i+1);
		scanf("%f", &seman[i]);
		soma += seman[i];
	}
	
	printf("\nMedia Temperatura = %.2f\n", soma / 7);
	
	maior = 0;
	acima = 0;
	for (i = 0; i < 7; i++) {
		if (seman[i] > maior)
			maior = seman[i];
		if (seman[i] > 25.0)
			acima ++;
	}
	
	printf("\nMaior temperatura = %.2f\n", maior);
	
	printf("\nAcima de 25 graus = %d dia(s)\n", acima);
	
	system("pause");
}