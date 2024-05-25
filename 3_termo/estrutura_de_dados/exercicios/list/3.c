#include <stdio.h>

int main()
{
	double a, b, som;
	som = 0;
	
	printf("A: ");
	scanf("%lf", &a);
	
	printf("B: ");
	scanf("%lf", &b);
	
	som = (a + b) * a;
	
	printf("Soma = %.1lf\n", som);
	
	return 0;
}