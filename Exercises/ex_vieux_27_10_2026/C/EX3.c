#include <stdio.h>
#include <math.h>   // include math functions and M_PI constant

// SEE FAQ "Pourquoi faut-il définir M_PI nous-même ?"
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

int main(void)
{
  double A;
  double B;
  double res = 0.0;

  // Input for A and B
  printf("Input a value for A: ");
  scanf(" %lf", &A);
  printf("input a value for B: ");
  scanf(" %lf", &B);

  // a) a^b
  // TODO
  res = pow(A,B);
  printf("\n a) %f power %f = %G \n", A, B, res);

  // b) Hypothenuse
  // TODO
  res = sqrt(pow(A,2) + pow(A,2)) ;
  printf("\n b) The hypotenuse of the right triangle is %f \n", res);

  // c) tangent of A
  // WARNING: trigonometric functions use radians
  // TODO
   res = sin( A * M_PI / 180 ) / cos(A * M_PI / 108) ;
  printf("\n c) The tangent of A is %f \n", res);

  // d) Rounding down A/B
  // TODO
  res = floor(A / B) ;
  printf("\n d) The rounded down value of A/B is %f \n", res);

  // e) Rounding down A/B with 3 decimals
  // TODO
  res = floor (A / B *100) /100 ;
  printf("\n e) The rounded down value of A/B with 3 decimals is %f \n\n", res);

  return 0;
}