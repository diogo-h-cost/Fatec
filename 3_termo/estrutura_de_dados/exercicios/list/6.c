#include <stdio.h>

int main()
{
	double a, b, c, media;
	
	printf("A: ");
	scanf("%lf", &a);	
	
	printf("B: ");
	scanf("%lf", &b);
	
	printf("C: ");
	scanf("%lf", &c);
	
	media = (a + b + c) / 3.0;
	
	printf("Meida: %.1lf\n", media);
	
	return 0;
}