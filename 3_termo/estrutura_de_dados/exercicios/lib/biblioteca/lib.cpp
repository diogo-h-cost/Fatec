#include <stdio.h>
#include <stdlib.h>
#include <Caminho ate \peso.h>

main()
{
	float alt;
	char sex;
	
	printf(">>>> CALCULAR ")
	printf("\nInsira a altura: ");
	scanf("%f", &alt);
	fflush(stdin);
	printf("Insira o sexo [F/M]: ");
	scanf("%c", &sex);
	
	if (sex == 'F' || sex == 'f')
		printf("\nPeso ideal para %.2f metros: %.2f Kg\n", alt, fem(alt));
	else if (sex == 'M' || sex == 'm')
		printf("\nPeso ideal para %.2f metros: %.2f Kg\n", alt, masc(alt));
	else
		printf(">>>> Erro [F ou M] <<<<");
		
	system("pause");
}
