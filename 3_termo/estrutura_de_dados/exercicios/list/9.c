#include <stdio.h>
#define pote 18

int main()
{
	double alt, lar, mt, poten;
	
	printf("Altura: ");
	scanf("%lf", &alt);
	
	printf("Largura: ");
	scanf("%lf", &lar);
	
	mt = alt * lar;
	poten = mt * pote;
	
	printf("\nArea: %.1lf\nPotencia: %.0lf W\n", mt, poten);
	
	return 0;
}