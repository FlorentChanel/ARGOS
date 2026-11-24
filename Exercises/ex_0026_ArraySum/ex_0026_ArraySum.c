// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0026_ArraySum.h"

// Function definitions
// TODO: implement ex_0026_ArraySum
void ex_0026_ArraySum(void)
{
    int tab[50];
    int status;
    int nb;

    do
    {
        printf("Nb values (max.50): ");
        status = scanf(" %d",&nb);
        if (status == EOF)
        {
            return;
        }
        int x;
        while((x= getchar()) != '\n' && x != EOF);

    }
    while(status != 1 || nb < 0 || nb > 50);
    for(int i=0; i < nb ; i++)    
    {
        do
        {
            printf("Value %d? ",i);
            status = scanf(" %d",&tab[i]);
            if (status == EOF)
            {
                return;
            }
            int x;
            while((x= getchar()) != '\n' && x != EOF);
        }
        while(status != 1);
    }
    printf("array:\n");

    for (int i = 0; i < nb; i++)
    {
        if (i > 0)
        {
            printf(" ");
        }
        printf("%d", tab[i]);
    }
    printf("\n");
    
    int Sum =0;
    for(int i=0; i < nb ; i++)
    {
        Sum = Sum + tab[i];
    }
    printf("Total sum: %d\n",Sum);
}