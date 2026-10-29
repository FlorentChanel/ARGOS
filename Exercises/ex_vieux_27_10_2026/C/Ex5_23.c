#include <stdio.h>

int main (void)
{
    int month ,status;
        do
        {
            printf("Please enter the number of the month (january=1, ... , december=12): ");
            status = scanf("%d",&month);
            if (status == EOF)
            {
                return 1;
            }
            int x;
            while((x= getchar()) != '\n' && x != EOF);
        }
        while( status != 1 || month > 12 || month < 1);

        if (month == 2)
        {
            printf("The %dth month has 28 days.",month);
        }
        else if (month == 4 || month == 6 || month == 9 || month == 11)
        {
            printf("The %dth month has 30 days.",month);
        }
        else 
        {
            printf("The %dth month has 31 days.",month);
        }
    return 0;
}