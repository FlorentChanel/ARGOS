// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0012_DecreasingOutput.h"

// Function definitions
void ex_0012_DecreasingOutput(void)
{
  // TODO: read 3 integers separated by commas, then print them in decreasing order
  int nb1, nb2,nb3, status;
  do
  {
    printf("Please enter 3 integers separated by commas: ");
    status = scanf(" %d , %d , %d", &nb1, &nb2, &nb3);
    if (status == EOF)
    {
      return ;
    }
    int c;
    while ((c = getchar()) != '\n' && c != EOF)
    {
    }
  }while (status != 3);

  int temp;

if (nb1 < nb2)
{
  temp = nb1;
  nb1 = nb2;
  nb2 = temp;
}

if (nb1 < nb3)
{
  temp = nb1;
  nb1 = nb3;
  nb3 = temp;
}

if (nb2 < nb3)
{
  temp = nb2;
  nb2 = nb3;
  nb3 = temp;
}

printf("The 3 integers sorted in decreasing order: %d, %d, %d\n",nb1, nb2, nb3);

}
