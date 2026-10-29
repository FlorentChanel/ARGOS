#include <stdio.h>
#include <math.h>

int main (void)
{
    printf("Enter a number \n") ;
    double circle_radius;
    scanf(" %lf",&circle_radius);

    printf("Circle radius: %.2lf \n",circle_radius);
    double pi = 3.14159265358979323;
    printf("pi = %lf \n",pi );
    double circle_aire = pow(circle_radius,2)*pi ;
    printf("Circle surface = %.2lf \n",circle_aire);


    return 0;
}
