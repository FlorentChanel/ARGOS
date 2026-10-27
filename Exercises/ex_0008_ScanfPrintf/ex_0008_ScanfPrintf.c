// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0008_ScanfPrintf.h"

// Function definitions
void ex_0008_ScanfPrintf(void)
{
  printf("\n\nPlease enter 3 letters:\n");
  char lettre1;
  char lettre2;
  char lettre3;
  scanf(" %c %c %c",&lettre1,&lettre2,&lettre3);

  printf("\nHere are the corresponding ASCII codes:\n");
  printf("%c--------->%d\n",lettre1,lettre1);
  printf("%c--------->%d\n",lettre2,lettre2);
  printf("%c--------->%d\n",lettre3,lettre3);
  // TODO: read 3 letters with scanf, then print their ASCII codes
}
