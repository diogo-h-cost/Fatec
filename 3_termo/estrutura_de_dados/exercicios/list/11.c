#include <stdio.h>

int main()
{
	double venda, desc;
	
	desc = 0;
	
	printf("Valor s/ desconto: ");
	scanf("%lf", &venda);
	
	desc = venda - ((venda * 12.5) / 100);
	
	printf("Venda: %.2lf reais\nVenda c/ desconto: %.2lf\n", venda, desc);
	
	return 0;
}