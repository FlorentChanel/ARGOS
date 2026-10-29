// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0017_Factorial.h"

// Function definitions
void ex_0017_Factorial(void)
{
  // Use the following message
  // print with printf("%s", input_message);
  //const char *input_message = "Please enter a non-negative integer N: ";

  // TODO: read a non-negative integer N, then compute and print N!
  
        int nb,status;
        do
        {
            printf("Please enter a non-negative integer N: ");
            status = scanf("%d",&nb);
            if (status == EOF)
            {
                return ;
            }
            int x;
            while((x= getchar()) != '\n' && x != EOF);
        }
        while( status != 1 || nb < 0);

       double facto = 1;
        if (nb == 0)
        {
            printf("0! = 1\n");
        }
        else 
        {
            for (int i = nb; i > 0; --i)
            {
                facto *= i;
            }
            printf("%d! = %.0lf\n",nb,facto);
        }
}
