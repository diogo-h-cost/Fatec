#include <stdio.h>

main()
{
	int tipo;
	float dis, cons, lt, gast;
	lt = 0;
	gast = 0;
	
	printf("Insira a distancia: ");
	scanf("%f", &dis);
	
	printf("Consumo (km/l): ");
	scanf("%f", &cons);
	
	printf("\nTipo do combustivel\n");
	printf("1 - Alcool, 2 - Diesel, 3 - Gasolina: ");
	scanf("%d", &tipo);
	
	lt = dis / cons;
	
	if (tipo == 1)
		gast = lt * 3.19;
	else if (tipo == 2)
		gast = lt * 6.47;
	else
		gast = lt * 5.66;
		
	printf("\nLitros necessarios: %.2f lt\n", lt);
	printf("Gasto: $ %.2f\n", gast);
	
	return 0;
}