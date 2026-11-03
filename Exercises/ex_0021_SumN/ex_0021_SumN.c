// Author: HE-Arc

// Standard includes

// Local includes
#include "ex_0021_SumN.h"

// Function definitions
// TODO: implement ex_0021_SumN
int ex_0021_SumN(int a,int b)
{
    int Sum;
    if(a > b)
    {
        int c=a;
        a=b;
        b=c;
    }

    for(int i = a; i<=b;i++)
    {
        Sum += i;
    }
    return Sum;
}
