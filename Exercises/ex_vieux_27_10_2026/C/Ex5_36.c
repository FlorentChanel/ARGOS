#include <stdio.h>

int main (void)

{
    int nb,status;
    do
    {
        printf("line count: ");
        status = scanf("%d",&nb);
        if(status == EOF)
        {
            return 1;
        }
        int x;
        while((x = getchar()) != '\n' && x != EOF);
    }
    while(status != 1 || nb < 1 || nb > 10);

    printf("X*Y   I");
    for (int j = 0; j <= nb; j++)
    {
        printf("%4d", j);
    }
    printf("\n--------");
    for (int g = 0;g <= nb;g++)
    {
        printf("----");
    }
    printf("\n");
    for (int i = 0; i <= nb; i++)
    {
        printf("%3d   I", i);

        for (int j = 0; j <= nb; j++)
        {
            printf("%4d", i * j);
        }

        printf("\n");
    }


    return 0;
}