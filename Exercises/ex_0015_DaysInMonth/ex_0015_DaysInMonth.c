// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0015_DaysInMonth.h"

// Function definitions
void ex_0015_DaysInMonth(void)
{
  // Use the following message
  // print with printf("%s", input_message);
  //const char *input_message = "Please enter the number of the month (january=1, ... , december=12): ";

  // TODO: read a month number between 1 and 12, then print its number of days

      int month ,status;
        do
        {
            printf("Please enter the number of the month (january=1, ... , december=12): ");
            status = scanf("%d",&month);
            if (status == EOF)
            {
                return ;
            }
            int x;
            while((x= getchar()) != '\n' && x != EOF);
        }
        while( status != 1 || month > 12 || month < 1);

        if (month == 2)
        {
            printf("Month %d has 28 days.\n",month);
        }
        else if (month == 4 || month == 6 || month == 9 || month == 11)
        {
            printf("Month %d has 30 days.\n",month);
        }
        else 
        {
            printf("Month %d has 31 days.\n",month);
        }
}
