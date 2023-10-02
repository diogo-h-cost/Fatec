#include <stdio.h>

int main()
{
	int a, b, soma;
	soma = 0;
	
	printf("A: ");
	scanf("%d", &a);
	
	printf("B: ");
	scanf("%d", &b);
	
	soma = a + b;
	
	if (soma > 20)
		soma += 8;
	else
		soma -= 5;
		
	printf("\nSoma = %d\n", soma);
	
	return 0;
}