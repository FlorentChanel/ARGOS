// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0028_DotProduct.h"

int main(void)
{
  int X[] = {1, 0, 0};
  int Y[] = {0, 1, 0};
  int Z[] = {0, 0, 1};

  int dot = ex_0028_DotProduct(X, Y, 3);
  printf("Dot product: %d\n", dot);

  dot = ex_0028_DotProduct(Y, Z, 3);
  printf("Dot product: %d\n", dot);

  dot = ex_0028_DotProduct(Z, X, 3);
  printf("Dot product: %d\n", dot);

  dot = ex_0028_DotProduct(X, X, 3);
  printf("Dot product: %d\n", dot);

  return 0;
}
