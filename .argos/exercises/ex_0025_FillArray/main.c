// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0025_FillArray.h"

int main(void)
{
  const int max_capacity = 10;
  int array[] = {-2, -2, -2, -2, -2, -2, -2, -2, -2, -2};

  int nb_values = ex_0025_FillArray(array, max_capacity);

  printf("%d values read:\n", nb_values);
  for (int i = 0; i < max_capacity; ++i)
  {
    printf("%d ", array[i]);
  }
  printf("\n");

  return 0;
}
