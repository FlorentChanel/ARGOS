// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0011_MultiplicationSign.h"

// Function definitions
void ex_0011_MultiplicationSign(void)
{
  // TODO: read 2 integers, then print the sign of their product without computing it
  int nb1, nb2, status;
  do
  {
    printf("Please enter 2 integers: ");
    status = scanf(" %d %d", &nb1, &nb2);
    if (status == EOF)
    {
      return ;
    }
    int c;
    while ((c = getchar()) != '\n' && c != EOF)
    {
    }
  }while (status != 2);

  if ((nb1>0 && nb2>0) || (nb1<0 && nb2<0))
  {
   printf("%d * %d > 0\n",nb1,nb2);
  }
  if ((nb1>0 && nb2<0) || (nb1<0 && nb2>0))
  {
    printf("%d * %d < 0\n",nb1,nb2);
  }
    if (nb1==0 || nb2==0)
  {
   printf("%d * %d = 0\n",nb1,nb2);
  }
}
