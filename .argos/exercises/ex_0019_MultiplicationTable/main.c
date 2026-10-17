// Author: HE-Arc

// Standard includes

// Local includes
#include "ex_0019_MultiplicationTable.h"

int main(void)
{
  const int MIN_TABLE = 1;
  const int MAX_TABLE = 12;

  int number;
  number = ex_0019_Read(MIN_TABLE, MAX_TABLE);
  ex_0019_MultiplicationTable(number);

  return 0;
}
