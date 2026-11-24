// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0025_FillArray.h"

// Function definitions
// TODO: implement ex_0025_FillArray
int ex_0025_FillArray(int array[], int max_capacity)
{

    if (max_capacity <= 0)
    {
        return 0;
    }

    int i = 0;
    for (; i < max_capacity; i++)
    {

        int status = 0;
        int value;
        while (status != 1 && status != EOF)
        {
            status = scanf(" %d", &value);

            {
                int c;
                do
                {
                    c = getchar();
                } while (c != '\n' && c != EOF);
            }
        }

        if (value < 0 || status == EOF)
        {
            break;
        }

        array[i] = value;
    }

    return i;
}