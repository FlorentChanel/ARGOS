extern "C"
{
  #include "../../../Exercises/ex_0013_SecondOrderEquation/ex_0013_SecondOrderEquation.c"
}

#include <gtest/gtest.h>

#include <cstdio>

#include "Common/Utils.h"

TEST(ex_0013, SecondOrderEquation)
{
  // Feed the coefficients through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0013_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0013_SecondOrderEquation();
  ex_0013_SecondOrderEquation();
  ex_0013_SecondOrderEquation();
  ex_0013_SecondOrderEquation();
  ex_0013_SecondOrderEquation();
  ex_0013_SecondOrderEquation();
  ex_0013_SecondOrderEquation();
  ex_0013_SecondOrderEquation();
  ex_0013_SecondOrderEquation();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: Any real is solution of this equation.\n"
                  "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: This equation has no real solution.\n"
                  "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: "
                  "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: "
                  "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: "
                  "The real solutions of this equation are: \nx1 = 1.2808\nx2 = -0.7808\n"
                  "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: "
                  "The real solutions of this equation are: \nx1 = 1.0000\nx2 = -2.0000\n"
                  "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: "
                  "The double real solution of this equation is: \nx = 1.0000\n"
                  "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: "
                  "The solution of this linear equation is: \nx = 2.0000\n"
                  "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: "
                  "This equation has no solution.\n"
                  "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: "
                  "The real solutions of this equation are: \nx1 = 2.0000\nx2 = 1.0000\n"
                  "Compute solutions of an equation of the form ax^2 + bx + c = 0\n"
                  "Please enter coefficients a, b, and c: "
                  "The real solutions of this equation are: \nx1 = 2.0000\nx2 = -2.0000\n";

  auto msg = std::string("CHECK ex_0013_SecondOrderEquation() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
