#include <stdio.h>
#include <stdlib.h>

float vist(float gast)
{
	return gast - (gast * 0.10);
}

float parc2(float gast)
{
	return gast / 2.0;
}

float maior100(float gast, int parc)
{
	int i;
	
	for (i = 0; i < parc; i++) {
		gast += gast * 0.03;
	}
	
	return gast / (float) parc;
}

main()
{
	int esc, parc;
	float gast;

	printf("\n**************************************************\n");

	do {
		printf("\nTotal gasto: ");
		scanf("%f", &gast);

		printf("\n++++++++++++++++++++++++++++++++++++++++++++++++++\n");

		printf("\nFormas de pagamento\n"
	    	   "\n1- A vista (10%% desc.)\n"
			   "2- 2x vezes (preco da etiqueta)\n"
			   "3- 3x a 10x vezes \n"
			   "\nEscolha -> ");
		scanf("%d", &esc);

		printf("\n--------------------------------------------------\n");

		if (esc == 1)
			printf("\nPagar a vista c/ 10%% desconto = $%.2f\n", vist(gast));
		else if (esc == 2)
			printf("\nPagar 2 parcelas de $%.2f\n", parc2(gast));
		else if (esc == 3) {
			printf("\nInsira N de parcelas 3x a 10x: ");
			scanf("%d", &parc);
			if (parc >= 3 && parc <= 10) {
				if (gast > 100.00) {
					printf("\nJuros de 3%% ao mes\n");
					printf("\nPagar $%.2f em %d parcelas de $%.2f\n", gast, parc, maior100(gast, parc));
				}
				else
					printf("\n>>> Apenas a vista ou 2x vezes!! <<<\n");
			}
			else
				printf("\n>>>> Erro !!!, apenas 3x a 10x <<<<\n");
		}
		else
			printf("\n>>>> Erro !!!, apenas 1, 2 e 3 <<<<\n");

		printf("\n--------------------------------------------------\n");

		printf("\nDesejar realizar novamente?\n"
		       "1- Sim\n"
			   "2- Nao\n\n"
			   "Escolha -> ");
		scanf("%d", &esc);

		printf("\n**************************************************\n");
	}while (esc == 1);

	system("pause");
}
