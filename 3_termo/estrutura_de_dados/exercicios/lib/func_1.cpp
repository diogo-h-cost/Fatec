#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void lerDados(float &a, float &b, float &c)
{
	printf("Insira A: ");
	scanf("%f", &a);
	printf("Insira B: ");
	scanf("%f", &b);
	printf("Insira C: ");
	scanf("%f", &c);
}

float func1(float a, float b, float c)
{
	float res = 0;
	
	res = ((2 + a) / (b + 3)) - (2 * c);
	
	return res;
}

float func2(float a, float b, float c)
{
	float res = 0;
	
	res = (2 * b + 5 + 3 * a) / (2 * c);
	
	return res;
}

float func3(float a, float b, float c)
{
	float res = 0;
	
	res = pow((a * 2 - a * 1), 2) + (b * 2 - b * 1);
	
	return res;
}

main()
{
	float a, b, c;
	
	lerDados(a, b, c);
	
	printf("\n %f -- %f --- %f", a, b, c);
	
	printf("\nFuncao 1 = %.2f\n", func1(a, b, c));
	printf("Funcao 2 = %.2f\n", func2(a, b, c));
	printf("Funcao 3 = %.2f\n", func3(a, b, c));
	
	system("pause");
}
