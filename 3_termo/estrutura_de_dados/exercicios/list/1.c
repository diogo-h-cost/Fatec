#include <stdio.h>

int main()
{
	double a, b, sub, mult, div;
	sub = mult = div = 0;
	
	printf("Digite A: ");
	scanf("%lf", &a);
	
	printf("Digite B: ");
	scanf("%lf", &b);
	
	sub = a - b;
	mult = a * b;
	if (b == 0) {
		printf("Nao e possivel divisao por 0\n");
		printf("Sub = %.1lf\nmult = %.1lf\n", sub, mult); 
	}
	else {
		div = a / b;
		printf("Sub = %.1lf, mult = %.1lf, Div = %.1lf\n", sub, mult, div); 
	} 
		
	return 0;
}