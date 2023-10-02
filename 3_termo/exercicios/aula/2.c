#include <stdio.h>

int main()
{
	int comp;
	float cust = 0;
	
	printf("Compra: ");
	scanf("%d", &comp);
	
	if (comp < 12)
		cust += comp * 1.30;
	else
		cust += comp * 1.00;
		
	printf("\nCusto = $%.2f\n", cust);	
	
	return 0;
}