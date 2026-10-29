    #include <stdio.h>

    int main (void)
    {
            int status;
            char letter;

        printf("Type a letter: \n");
        status = scanf("%c", &letter);
        if (status == EOF)
        {
            return 1;
        }
        int c;
        while ((c = getchar()) != '\n' && c != EOF)
        {
        }
        printf("%d",letter);
        if (letter<=90 && letter>=65)
        {
            printf("UPPERCASE \n");
        }
        else if (letter<=122 && letter>=97)
        {
            printf("lowercase \n");
        }
        else
        {
            printf("Not a letter \n");
        }
    return 0;

    }