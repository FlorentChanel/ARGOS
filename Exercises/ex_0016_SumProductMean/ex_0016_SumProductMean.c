// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0016_SumProductMean.h"

// Function definitions
void ex_0016_SumProductMean(void)
{
  // Use the following messages
  // print with printf("%s", input_message);
  //const char *input_message = "Number of values to read: ";
  // print with printf(value_message, i); where i is the value number, starting at 1
  //const char *value_message = "%d. number: ";

  // TODO: read N (between 1 and 15), then N integers, and print their sum, product and mean
      int status,N;
    do
    {
        printf("Number of values to read: ");
        status = scanf("%d",&N);
        if (status == EOF)
        {
            return ;
        }
        int x;
        while((x= getchar()) != '\n' && x != EOF);
    }
    while(status != 1 || N < 1 || N > 15);

    int str[N + 1];

    for(int i=0; i < N; i++)
    {
        do
        {
            printf("%d. number: ",i+1);
            status = scanf("%d",&str[i]);
            if (status == EOF)
            {
                return ;
            }
            int x;
            while((x= getchar()) != '\n' && x != EOF);
        }
        while(status != 1 );
    }

    int somme = 0;
    for (int i = 0; i < N; i++)
    {
        somme += str[i];
    }
    printf("Sum = %d\n",somme);

    int produit = 1;
    for (int i = 0; i < N; i++)
    {
        produit *= str[i];
    }
    printf("Product = %d\n",produit);

    printf("Mean = %.4lf\n",(double)somme/N);
}
