// Author: HE-Arc

// Standard includes
#include <stdio.h>
#include <math.h> // math functions (pow, sqrt, sin, cos, floor)

// Local includes
#include "ex_0003_SomeCalculus.h"

// M_PI is not guaranteed by the C standard; define it when the toolchain does not provide it
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Function definitions
void ex_0003_SomeCalculus(double a, double b)
{
  double res = 0; // To store the result of the calculations

  // a) a^b
  // TODO
  printf("\n a) %f power %f = %G \n", a, b, res);

  // b) Hypotenuse
  // TODO
  printf("\n b) The hypotenuse of the right triangle is %f \n", res);

  // c) tangent of A
  // NOTE: we consider that A is in degrees
  // WARNING: trigonometric functions use radians
  // TODO
  printf("\n c) The tangent of A is %f \n", res);

  // d) Rounding down A/B
  // TODO
  printf("\n d) The rounded down value of A/B is %f \n", res);

  // e) Rounding down A/B with 3 decimals
  // TODO
  printf("\n e) The rounded down value of A/B with 3 decimals is %f \n\n", res);
}
