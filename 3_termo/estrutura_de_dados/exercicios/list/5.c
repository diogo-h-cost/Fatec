#include <stdio.h>
#include <math.h>

int main()
{
	double cat1, cat2, hipo;
	
	printf("Cateto 1 = ");
	scanf("%lf", &cat1);
	
	printf("Cateto 2 = ");
	scanf("%lf", &cat2);
	
	hipo = sqrt(pow(cat1, 2) + pow(cat2, 2));
	
	printf("Hipotenusa = %.1lf\n", hipo);
	
	return 0;
}