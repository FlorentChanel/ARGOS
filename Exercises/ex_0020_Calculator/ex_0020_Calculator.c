// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0020_Calculator.h"

// Function definitions
// TODO: implement ex_0020_Calculator
double ex_0020_Calculator(double nb1, double nb2, char opp)
{
    double result;
    switch(opp)
    {
        case '+' : result = nb1 + nb2;
                 break;
        case '-' : result = nb1 - nb2;
                 break;
        case '*' : result = nb1 * nb2;
                 break;
        case '/' : if (nb2 != 0)
                 {
                    result = nb1 / nb2;
                 }
                 else
                 {
                    result = 0;
                 }
                 break;
        default: result = 0;
                 break;
    }
    return result;
}
