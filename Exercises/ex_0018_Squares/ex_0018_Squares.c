// Author: HE-Arc

// Standard includes
#include <stdio.h>
#include <stdbool.h>

// Local includes
#include "ex_0018_Squares.h"

// Function definitions
int ex_0018_Square(int num)
{
    return num*num;
}
// TODO: implement ex_0018_Square and ex_0018_Squares
bool ex_0018_Squares (int num)
{

    if (num < 1 || num > 1000)
    {
        return false;
    }

    for (int i=1; i<=num; i++)
    {
        printf("%d ",ex_0018_Square(i));
    }
    printf("\n");
    return true;
}