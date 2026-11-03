// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0019_MultiplicationTable.h"

// Function definitions
// TODO: implement ex_0019_Read and ex_0019_MultiplicationTable
int ex_0019_Read(int min,int max)
{
    int status,number;
    do
    {
        printf("Please enter the multiplication table (in [%d..%d]): ",min,max);
        status = scanf(" %d",&number);
        if (status == EOF)
        {
         return 1;
        }

        int x;
        while((x=getchar()) != '\n' && x != EOF);
    }
    while( status != 1 || number>max || number<min);
    return number;
}

void ex_0019_MultiplicationTable(int number)
{
    printf("\nMULTIPLICATION TABLE FOR %d\n",number);
    for (int i=1; i<11; i++)
    {
        printf("%d X %d = %d\n",number,i,number*i);
    }
}