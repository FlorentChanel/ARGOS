// Author: HE-Arc

#ifndef EX_0030_COMPLEX_H
#define EX_0030_COMPLEX_H

// Standard includes

// Local includes

// Types
typedef struct
{
    double real;
    double imaginary;
}Complex;
// Function prototypes
Complex ex_0030_InputComplex(void);
Complex ex_0030_SumComplex(Complex nb1, Complex nb2);
Complex ex_0030_DiffComplex(Complex nb1, Complex nb2);
void ex_0030_PrintComplex(Complex nbx);
void ex_0030_Complex(void);
#endif // EX_0030_COMPLEX_H
