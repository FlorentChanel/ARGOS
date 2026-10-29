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
    while(status != 1);



    for(int i = 0; i < nb; i++)
    {
        for(int j = nb; j > i; j-- )
        {
            printf(" ");
        }
        for(int j = 0;j < 1+(i*2); j++ )
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}