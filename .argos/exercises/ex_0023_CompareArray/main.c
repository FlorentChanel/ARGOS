// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0023_CompareArray.h"

int main(void)
{
  int array1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int array2[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9};

  bool equal = ex_0023_CompareArray(array1, array2, 10);
  printf("Arrays are %s\n", equal ? "equal" : "different");

  equal = ex_0023_CompareArray(array1, array2, 9);
  printf("Arrays are %s\n", equal ? "equal" : "different");

  return 0;
}
