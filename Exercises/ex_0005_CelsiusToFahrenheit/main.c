// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0005_CelsiusToFahrenheit.h"

int main(void)
{
  double temperatureC = 0.;
  double temperatureF = 0.;

  printf("Enter a temperature in Celsius: ");
  scanf("%lf", &temperatureC);

  temperatureF = ex_0005_CelsiusToFahrenheit(temperatureC);

  printf("%.1f degrees Celsius corresponds to %.1f degrees Fahrenheit\n", temperatureC, temperatureF);

  return 0;
}
