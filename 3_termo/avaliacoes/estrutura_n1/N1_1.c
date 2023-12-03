#include <stdio.h>

main()
{
	float saco, gato1, gato2, consumo, gramas, dias;
	consumo = 0;
	gramas = 0;
	dias = 0;
	
	printf("Peso do saco (kg): ");
	scanf("%f", &saco);
	
	printf("Quantidade (gramas) do gato 1: ");
	scanf("%f", &gato1);
	
	printf("Quantidade (gramas) do gato 2: ");
	scanf("%f", &gato2);
	
	consumo = gato1 + gato2;
	
	gramas = saco * 1000;
	
	dias = (gramas - (consumo * 7)) / 1000;
	
	printf("\nRestara %.1f KG de racao apos 7 dias\n", dias);
	
	return 0;
}