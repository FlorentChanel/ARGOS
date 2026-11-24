// Author: HE-Arc

// Standard includes

// Local includes
#include "ex_0028_DotProduct.h"

// Function definitions
// TODO: implement ex_0028_DotProduct
int ex_0028_DotProduct (int Vect1[],int Vect2[], int n)
{
    int ProductV=0;
    for(int i=0; i < n ; i++)
    {
        ProductV += Vect1[i] * Vect2[i];
    }
    return ProductV;
}