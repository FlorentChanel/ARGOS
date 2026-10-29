#include <stdio.h>

int main(void)
{
    float temp;
    printf("Enter a temperature in Celsius: \n");
    scanf("%f",&temp);
    // variable intermediare
    printf("%.2f degres Celsius correspond to a %.2f degres Fahrenheit",temp,32 + (9 *temp) / 5);
    return 0;
}