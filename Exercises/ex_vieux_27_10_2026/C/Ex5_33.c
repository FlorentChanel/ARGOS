#include <stdio.h>
#include <float.h>

int main (void)
    {

        int nb,status;
        do
        {
            printf("Please enter a positive integer N: ");
            status = scanf("%d",&nb);
            if (status == EOF)
            {
                return 1;
            }
            int x;
            while((x= getchar()) != '\n' && x != EOF);
        }
        while( status != 1 || nb < 0);

        long double facto = 1;
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
            printf("%d! = %Lf\n",nb,facto);
        }

        return 0;
    }
