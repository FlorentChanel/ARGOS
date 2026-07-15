extern "C"
{
  #include "../../../Exercises/ex_0004_Swap/ex_0004_Swap.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0004, Swap)
{
  testing::internal::CaptureStdout();
  ex_0004_Swap();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Variable 1: 10\nVariable 2: 5\nVariable 1: 5\nVariable 2: 10\n";

  auto msg = std::string("CHECK ex_0004_Swap() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
