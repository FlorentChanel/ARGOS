// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0030_Complex.h"

// Function definitions
// TODO: implement ex_0030_InputComplex, ex_0030_SumComplex, ex_0030_DiffComplex, ex_0030_PrintComplex and ex_0030_Complex
Complex ex_0030_InputComplex(void)
{
    int status = 0;
    int valid = 1;
    Complex nbx;

    do
    {
        valid = 1;
        printf("Please enter a complex number (r,i): ");
        status = scanf(" ( %lf , %lf )", &nbx.real, &nbx.imaginary);

        int c;
        do
        {
            c = getchar();
            if (c != '\n' && c != EOF && c != ' ' && c != '\t')
            {
                valid = 0;
            }
        } while (c != '\n' && c != EOF);

    } while ((status != 2 || !valid) && status != EOF);

    return nbx;
}
//
Complex ex_0030_SumComplex(Complex nb1, Complex nb2)
{
    Complex nbx;
    nbx.real = nb1.real + nb2.real;
    nbx.imaginary = nb1.imaginary + nb2.imaginary;
    return nbx;
}
//
Complex ex_0030_DiffComplex(Complex nb1, Complex nb2)
{
    Complex nbx;
    nbx.real = nb1.real - nb2.real;
    nbx.imaginary = nb1.imaginary - nb2.imaginary;
    return nbx;
}
//
void ex_0030_PrintComplex(Complex nbx)
{
    printf("%.2lf + %.2lfi\n",nbx.real,nbx.imaginary);
}
//
void ex_0030_Complex(void)
{
    Complex nb1 = ex_0030_InputComplex();
    Complex nb2 = ex_0030_InputComplex();

    Complex nbx = ex_0030_SumComplex(nb1,nb2);
    printf("\nSum = ");
    ex_0030_PrintComplex(nbx);

    nbx = ex_0030_DiffComplex(nb1,nb2);
    printf("\nDiff = ");
    ex_0030_PrintComplex(nbx);
}
//