#include <stdio.h>
#include <ctype.h> // Converter minusculo em maiusculo

int main()
{
	float lt, desc, prec, pag;
	char comb;

	desc = 0;
	prec = 0;
	pag = 0;

	printf("Quantos litros: ");
	scanf("%f", &lt);
	fseek(stdin, 0, SEEK_END); //fflush(stdin);

	printf("A-Alcool ou G-Gasolina: ");
	scanf("%c", &comb); //comb = getchar();
	
	comb = toupper(comb); //Reduz processamento -> busca a funcao e realiza
	
	if (comb == 'A') {
		prec = lt * 3.34;
		if (lt <= 20)
            desc = 3.0 * prec / 100;
		else
			desc = 5.0 * prec / 100;
	}
	else {
        prec = lt * 4.30;
		if (lt <= 20)
			desc = 4.0 * prec / 100;
		else
			desc = 6.0 * prec / 100;
	}

	pag = prec - desc;

	printf("\nPagar = $ %.2f\n", pag);

	return 0;
}