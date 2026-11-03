// Author: HE-Arc

// Standard includes

// Local includes
#include "ex_0022_Invert.h"

// Function definitions
// TODO: implement ex_0022_Invert
int ex_0022_Invert(int n)
{
    int result;
    if (n<0)
    {
        result = -1;
    }
    else
    {
        while(n > 0)
        {
            int unit = n % 10;
            result = (10 * result) + unit;
            n = n /10;
        }
    }
    return result;
}