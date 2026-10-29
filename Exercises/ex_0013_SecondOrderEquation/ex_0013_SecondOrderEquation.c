// Author: HE-Arc

// Standard includes
#include <stdio.h>
#include <math.h>

// Local includes
#include "ex_0013_SecondOrderEquation.h"

// Function definitions
void ex_0013_SecondOrderEquation(void)
{


  // TODO: read coefficients a, b and c, then print the real solutions of the equation
  double a, b ,c;
  int status;

  do
  {
    printf("Compute solutions of an equation of the form ax^2 + bx + c = 0\n");
    printf("Please enter coefficients a, b, and c: ");
    status = scanf("%lf %lf %lf",&a,&b,&c);
    if (status == EOF)
    {
        return ;
    }
    int x;
    while((x= getchar()) != '\n' && x != EOF);
  }
  while( status != 3);

  double x1, x2;
  if (a == 0 && b == 0 && c == 0)
  {
    printf("Any real is solution of this equation.\n");
  }
  else if(a == 0 && b == 0)
  {
    printf("This equation has no solution.\n");
  }
  else if(a == 0)
  {
    x1 = -(double)c/b;
    printf("The solution of this linear equation is: \nx = %.4f\n",x1);
  }
  else
  {
    if ((pow(b,2)-4*a*c)<0)
    {
      printf("This equation has no real solution.\n");
    }
    else if((pow(b,2)-4*a*c)==0)
    {
      x1 = ((-b + sqrt(pow(b,2)-(4*a*c)))/(2*a));
      printf("The double real solution of this equation is: \nx = %.4f\n",x1);
    }
    else
    {
      x1 = ((-b + sqrt(pow(b,2)-(4*a*c)))/(2*a));
      x2 = ((-b - sqrt(pow(b,2)-(4*a*c)))/(2*a));
      printf("The real solutions of this equation are: \nx1 = %.4f\nx2 = %.4f\n",x1,x2);
    }
  }
}
