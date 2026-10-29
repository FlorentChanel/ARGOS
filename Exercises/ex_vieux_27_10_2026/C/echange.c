#include <stdio.h>

int main (void)
{
    int variable1 = 10;
    int variable2 = 5;
    int memory = 0;

    printf ("La Variable 1 est egal a %d \n", variable1); // avant l'échange
    printf ("La Variable 2 est egal a %d \n", variable2);

    memory = variable1;
    variable1 = variable2;
    variable2 = memory;

    printf ("La Variable 1 est egal a %d \n", variable1); // après l'échange
    printf ("La Variable 2 est egal a %d \n", variable2);
    return 0;
}