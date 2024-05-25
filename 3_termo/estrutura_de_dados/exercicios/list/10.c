#include <stdio.h>

int main()
{
	double salar, nov_sal;
	
	nov_sal = 0;
	
	printf("Salario: ");
	scanf("%lf", &salar);
	
	nov_sal = ((salar * 25) / 100) + salar;
	
	printf("\nSalario Old: %.2lf reais\nSalario New: %.2lf reais\n", salar, nov_sal);
	
	return 0;
}