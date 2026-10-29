  #include <stdio.h>
  #include <stdlib.h>

int main(void)
{
    int a, b, status;
    do
    {
        printf("Please enter 2 integers separated by commas:");
        status = scanf("%d %d", &a, &b);
        if (status == EOF)
        {
            return 1;
        }
        int c;
        while ((c = getchar()) != '\n' && c != EOF);

    }
    while (status != 2);

    if ((a > 0 && b > 0) || (a > 0 && abs(a) > abs(b)) || (b > 0 && abs(b) > abs(a)))
    {
        printf("%d + %d = +",a,b);
    }
    else if ((a < 0 && b < 0 )|| (a < 0 && abs(a) > abs(b)) || (b < 0 && abs(b) > abs(a)))
    {
        printf("%d + %d = -",a,b);
    }
    else if ((a > 0 && b < 0 && abs(a) == abs(b)) || (a < 0 && b > 0 && abs(a) == abs(b)))
    {
        printf("%d + %d = 0",a,b);
    }
    return 0;
}