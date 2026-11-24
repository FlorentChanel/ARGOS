// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0025_FillArray.h"

// Function definitions
// TODO: implement ex_0025_FillArray
int ex_0025_FillArray(int array[], int max_capacity)
{
    int status;
    int data;
    int count = 0;
    do
    {
        status = scanf(" %d",&data);
        if (status == EOF)
        {
            break;
        }
        int x;
        while((x= getchar()) != '\n' && x != EOF);
        if (data<0)
        {
            break;
        }
        else
        {
        array[count] = data;
        count++;
        }
    }
    while(count < max_capacity);

    return count;
}