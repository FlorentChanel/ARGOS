// Author: HE-Arc

// Standard includes

// Local includes
#include "ex_0005_CelsiusToFahrenheit.h"

// Function definitions
double ex_0005_CelsiusToFahrenheit(double temperatureC)
{
  double temperatureF = 0.;

  // TODO: convert temperatureC to Fahrenheit and return it

  // variable intermediare
  temperatureF =32 + ((9 *temperatureC) / 5);

  return temperatureF;
}
