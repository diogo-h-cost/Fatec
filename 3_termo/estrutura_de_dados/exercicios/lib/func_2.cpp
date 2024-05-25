#include <stdio.h>
#include <math.h>
#include <stdlib.h>

float perim(float bas, float alt)
{
	return 2 * (bas + alt);
}

float area(float bas, float alt)
{
	return bas * alt;
}

float diag(float bas, float alt)
{	
	return sqrt(pow(bas, 2) + pow(alt, 2));
}

main()
{
	float bas, alt;
	
	printf("Insira a BASE: ");
	scanf("%f", &bas);
	
	printf("Insira a ALTURA: ");
	scanf("%f", &alt);
	
	printf("Perimetro = %.2f\n", perim(bas, alt));
	printf("Area = %.2f\n", area(bas, alt));
	printf("Diagonal = %.2f\n", diag(bas, alt));
		
	system("pause");
}
