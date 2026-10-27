// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0003_SomeCalculus.h"

int main(void)
{
  double a = 0.0;
  double b = 0.0;

  printf("Input a value for A: ");
  scanf("%lf", &a);
  printf("Input a value for B: ");
  scanf("%lf", &b);

  ex_0003_SomeCalculus(a, b);

  return 0;
}
