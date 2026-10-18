extern "C"
{
  #include "../../../Exercises/ex_0030_Complex/ex_0030_Complex.c"
}

#include <gtest/gtest.h>

#include <cstdio>

#include "Common/Utils.h"

// Members set by name: the README does not impose their declaration order.
static Complex MakeComplex(double real, double imaginary)
{
  Complex c;
  c.real = real;
  c.imaginary = imaginary;
  return c;
}

TEST(ex_0030, ComplexSum)
{
  auto msg = std::string("CHECK ex_0030_SumComplex() result!");

  Complex r = ex_0030_SumComplex(MakeComplex(1.0, 1.0), MakeComplex(2.0, 3.0));
  EXPECT_DOUBLE_EQ(3.0, r.real) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(4.0, r.imaginary) << Utils::formatError(msg);

  r = ex_0030_SumComplex(MakeComplex(-1.5, 2.25), MakeComplex(0.5, -4.0));
  EXPECT_DOUBLE_EQ(-1.0, r.real) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(-1.75, r.imaginary) << Utils::formatError(msg);

  r = ex_0030_SumComplex(MakeComplex(0.0, 0.0), MakeComplex(-2.0, 7.0));
  EXPECT_DOUBLE_EQ(-2.0, r.real) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(7.0, r.imaginary) << Utils::formatError(msg);
}

TEST(ex_0030, ComplexDiff)
{
  auto msg = std::string("CHECK ex_0030_DiffComplex() result!");

  Complex r = ex_0030_DiffComplex(MakeComplex(1.0, 1.0), MakeComplex(2.0, 3.0));
  EXPECT_DOUBLE_EQ(-1.0, r.real) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(-2.0, r.imaginary) << Utils::formatError(msg);

  r = ex_0030_DiffComplex(MakeComplex(2.0, 3.0), MakeComplex(1.0, 1.0));
  EXPECT_DOUBLE_EQ(1.0, r.real) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(2.0, r.imaginary) << Utils::formatError(msg);

  r = ex_0030_DiffComplex(MakeComplex(-1.5, 2.25), MakeComplex(0.5, -4.0));
  EXPECT_DOUBLE_EQ(-2.0, r.real) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(6.25, r.imaginary) << Utils::formatError(msg);
}

TEST(ex_0030, PrintComplex)
{
  testing::internal::CaptureStdout();
  ex_0030_PrintComplex(MakeComplex(5.0, -3.0));
  ex_0030_PrintComplex(MakeComplex(-1.5, 2.25));
  ex_0030_PrintComplex(MakeComplex(0.5, 4.0));
  auto actual = testing::internal::GetCapturedStdout();

  auto expected = "5.00 + -3.00i\n"
                  "-1.50 + 2.25i\n"
                  "0.50 + 4.00i\n";

  auto msg = std::string("CHECK ex_0030_PrintComplex() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}

TEST(ex_0030, InputComplex)
{
  ASSERT_NE(freopen("ex_0030_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  Complex c1 = ex_0030_InputComplex();
  Complex c2 = ex_0030_InputComplex();
  Complex c3 = ex_0030_InputComplex();
  Complex c4 = ex_0030_InputComplex();
  testing::internal::GetCapturedStdout();

  auto msg = std::string("CHECK ex_0030_InputComplex() result!");

  EXPECT_DOUBLE_EQ(1.0, c1.real) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(1.0, c1.imaginary) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(2.5, c2.real) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(-4.0, c2.imaginary) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(-3.0, c3.real) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(0.5, c3.imaginary) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(7.0, c4.real) << Utils::formatError(msg);
  EXPECT_DOUBLE_EQ(-8.0, c4.imaginary) << Utils::formatError(msg);
}

TEST(ex_0030, Complex)
{
  ASSERT_NE(freopen("ex_0030_complex_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0030_Complex();
  ex_0030_Complex();
  auto actual = testing::internal::GetCapturedStdout();

  auto expected = "Please enter a complex number (r,i): "
                  "Please enter a complex number (r,i): "
                  "Please enter a complex number (r,i): "
                  "Please enter a complex number (r,i): "
                  "\nSum = 3.00 + 4.00i\n"
                  "\nDiff = -1.00 + -2.00i\n"
                  "Please enter a complex number (r,i): "
                  "Please enter a complex number (r,i): "
                  "\nSum = 1.75 + 1.00i\n"
                  "\nDiff = -0.75 + -5.00i\n";

  auto msg = std::string("CHECK ex_0030_Complex() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
