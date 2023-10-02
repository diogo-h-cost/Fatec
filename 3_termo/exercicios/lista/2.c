#include <stdio.h>

int main()
{
	double base, altura, perim, area;
	
	printf("Base: ");
	scanf("%lf", &base);
	
	printf("Perimetro: ");
	scanf("%lf", &altura);
	
	perim = 2.0 * (base + altura);
	area = base * altura;
	
	printf("\nPerimetro = %.1lf\nArea = %.1lf\n", perim, area);
	
	return 0;
}