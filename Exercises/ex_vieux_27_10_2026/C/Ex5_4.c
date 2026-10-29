    #include <stdio.h>

int main(void)
{
    int nb1, nb2,nb3, status;
    do
    {
        printf("Please enter 3 integers separated by commas:");
        status = scanf("%d %d %d", &nb1, &nb2, &nb3);
        if (status == EOF)
        {
            return 1;
        }
        int c;
        while ((c = getchar()) != '\n' && c != EOF)
        {
        }
    }while (status != 3);

    if( nb1 < nb2 && nb1 < nb3)
    {
        printf("%d ",nb1);
        if(nb2 < nb3)
        {
            printf("%d ",nb2);
            printf("%d",nb3);
        }
        else
        {
            printf("%d ",nb3);
            printf("%d",nb2);
        }
    }

        if( nb2 < nb1 && nb2 < nb3)
    {
        printf("%d ",nb2);
        if(nb1 < nb3)
        {
            printf("%d ",nb1);
            printf("%d",nb3);
        }
        else
        {
            printf("%d ",nb3);
            printf("%d",nb1);
        }
    }

        if( nb3 < nb1 && nb3 < nb2)
    {
        printf("%d ",nb3);
        if(nb2 < nb1)
        {
            printf("%d ",nb2);
            printf("%d",nb1);
        }
        else
        {
            printf("%d ",nb1);
            printf("%d",nb2);
        }
    }
    return 0;
}   