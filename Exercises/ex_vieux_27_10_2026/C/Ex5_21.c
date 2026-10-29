#include <stdio.h>

int main (void)
{
    int x = 2;
    switch (x)
    {
        case 0:
        {
            printf("Error\n");
            break;
        }
        default :
        {
            printf("100/%d = %lf\n", x, 100./x);
            break;
        }
    }
    return 0;
}