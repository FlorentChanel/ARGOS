extern "C"
{
  #include "../../../Exercises/ex_0009_Circle/ex_0009_Circle.c"
}

#include <gtest/gtest.h>

#include <cstdio>

#include "Common/Utils.h"

TEST(ex_0009, Circle)
{
  // Feed the radii through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0009_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0009_Circle();
  ex_0009_Circle();
  ex_0009_Circle();
  ex_0009_Circle();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Circle radius: pi = 3.141593\nCircle surface = 3.14\n"
                  "Circle radius: pi = 3.141593\nCircle surface = 19.63\n"
                  "Circle radius: pi = 3.141593\nCircle surface = 0.00\n"
                  "Circle radius: pi = 3.141593\nCircle surface = 314.16\n";

  auto msg = std::string("CHECK ex_0009_Circle() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
