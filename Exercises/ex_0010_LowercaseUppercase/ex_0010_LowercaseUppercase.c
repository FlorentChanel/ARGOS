// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0010_LowercaseUppercase.h"

// Function definitions
void ex_0010_LowercaseUppercase(void)
{
  // TODO: read a character, then tell whether it is lowercase, uppercase or not a letter
  int status;
  char letter;

  printf("Type a letter: ");
  status = scanf(" %c", &letter);
  if (status == EOF)
  {
    return ;
  }
  int c;
  while ((c = getchar()) != '\n' && c != EOF)
  {
  }
  if (letter<=90 && letter>=65)
  {
    printf("UPPERCASE\n");
  }
  else if (letter<=122 && letter>=97)
  {
    printf("lowercase\n");
  }
  else
  {
    printf("The character you entered is not a letter.\n");
  }
}
