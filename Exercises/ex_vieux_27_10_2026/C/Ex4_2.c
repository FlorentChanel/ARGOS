#include <stdio.h>

int main (void)

{
    printf("\n \n Please enter 3 letters:\n");
    char lettre1;
    char lettre2;
    char lettre3;
    scanf(" %c %c %c",&lettre1,&lettre2,&lettre3);

    printf("\n \n Here are the corresponding ASCII codes:\n");
    printf("%c--------->%d\n",lettre1,lettre1);
    printf("%c--------->%d\n",lettre2,lettre2);
    printf("%c--------->%d\n",lettre3,lettre3);


    return 0;
}