// Author: HE-Arc

// Standard includes
#include <stdio.h>
#include <math.h>
// Local includes
#include "ex_0009_Circle.h"

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Function definitions
void ex_0009_Circle(void)
{
  
  // TODO: read the radius with scanf, then print pi and the circle surface

  double circle_radius;
  printf("Circle radius: ");
  scanf(" %lf",&circle_radius);
  double pi = 3.14159265358979323;
  printf("pi = %lf\n",pi );
  double circle_aire = pow(circle_radius,2)*pi ;
  printf("Circle surface = %.2lf\n",circle_aire);
}
