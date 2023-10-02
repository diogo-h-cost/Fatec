#include <stdio.h>

int main()
{
	float atual, max, min, media;
	media = 0;
	
	printf("Quantidade Atual: ");
	scanf("%f", &atual);
	printf("Quantidade Maxima: ");
	scanf("%f", &max);
	printf("Quantidade Minima: ");
	scanf("%f", &min);
	
	media = (max + min) / 2.00;
	
	if (atual >= media)
		printf("\nNao efetuar compra\n");
	else
		printf("\nEfetuar compra\n");
	
	return 0;
}