    #include <stdio.h>

int main(void)
{
    int nb1, nb2, status;
    do
    {
        printf("Please enter 2 integers:");
        status = scanf("%d %d", &nb1, &nb2);
        if (status == EOF)
        {
            return 1;
        }
        int c;
        while ((c = getchar()) != '\n' && c != EOF)
        {
        }
    }while (status != 2);

    if ((nb1>0 && nb2>0) || (nb1<0 && nb2<0))
    {
    printf("%d * %d > 0",nb1,nb2);
    }
    if ((nb1>0 && nb2<0) || (nb1<0 && nb2>0))
    {
    printf("%d * %d < 0",nb1,nb2);
    }
    if (nb1==0 || nb2==0)
    {
    printf("%d * %d = 0",nb1,nb2);
    }
    return 0;
}
