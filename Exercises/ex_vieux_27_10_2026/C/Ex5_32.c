#include <stdio.h>

int main(void)
{
    int status,N;
    do
    {
        printf("Number of values to read: ");
        status = scanf("%d",&N);
        if (status == EOF)
        {
            return 1;
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
                return 1;
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
    return 0;
}