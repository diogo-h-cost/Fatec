#include <stdio.h>

int main()
{
	double fah, cent;
	cent = 0;
	
	printf("Fahrenheit: ");
	scanf("%lf", &fah);
	
	cent = 	(5 * (fah - 32)) / 9;
	
	printf("\n%.1lf Fahrenheit == %.1lf Centigrados\n", fah, cent);
	
	return 0;
}