// Author: HE-Arc

// Standard includes
#include <stdio.h>
#include <stdbool.h> // for bool, true, false

// Local includes
#include "ex_0014_CurrencyConverter.h"

// Function definitions
void ex_0014_CurrencyConverter(void)
{


  // TODO: read an amount and a currency, validate them, then convert to Swiss francs

    const double WON2CHF = 0.00070;
    const double USD2CHF = 0.99;
    const double YEN2CHF = 0.0067;
    const double POUND2CHF = 1.13;
    double money;
    char x;
    int status;
    int valid=0;
    do
    {
        printf("USAGE: non-negative value [W | $ | Y | P]\nWon = W  Dollar = $  Yen = Y  Pound = P\nPlease enter the amount to convert: ");
        status = scanf("%lf %c",&money,&x);
        if (status == EOF)
        {
            return ;
        }
        if (status != 2)
        {
            printf("The input format is not correct!!\n");
        }
        if (x == 'W' || x == '$' || x == 'P' || x == 'Y')
        {
           valid = 1;
        }
        else
        {
            printf("Unsupported currency!!\n");   
        }
        if (money < 0)
        {
            printf("The input amount is negative!!\n");
        }
        
        int c;
        while((c=getchar()) != '\n' && c != EOF);
    }
    while( status != 2 || money < 0 || valid != 1);

    
    if (x == 'W')
    {
        printf("Swiss francs: %.3lf\n",money*WON2CHF);
    }
    else if (x == '$')
    {
        printf("Swiss francs: %.3lf\n",money*USD2CHF);
    }
    else if (x == 'Y')
    {
        printf("Swiss francs: %.3lf\n",money*YEN2CHF);
    }
    else if (x == 'P')
    {
        printf("Swiss francs: %.3lf\n",money*POUND2CHF);
    }

}
