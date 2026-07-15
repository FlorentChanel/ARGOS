extern "C"
{
  #include "../../../Exercises/ex_0002_PrintMathCalc/ex_0002_PrintMathCalc.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0002, PrintMathCalc)
{
  testing::internal::CaptureStdout();
  ex_0002_PrintMathCalc();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "The result of 37 * 12 = 444\n";

  auto msg = std::string("CHECK ex_0002_PrintMathCalc() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
