extern "C"
{
  #include "../../../Exercises/ex_0012_DecreasingOutput/ex_0012_DecreasingOutput.c"
}

#include <gtest/gtest.h>

#include <cstdio>

#include "Common/Utils.h"

TEST(ex_0012, DecreasingOutput)
{
  // Feed the integers through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0012_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  for (int i = 0; i < 11; ++i)
  {
    ex_0012_DecreasingOutput();
  }

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: 3, 2, 1\n"
                  "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: -1, -2, -3\n"
                  "Please enter 3 integers separated by commas: "
                  "Please enter 3 integers separated by commas: "
                  "Please enter 3 integers separated by commas: "
                  "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: 45, 12, 0\n"
                  "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: 3, 2, 1\n"
                  "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: 1, 0, -2\n"
                  "Please enter 3 integers separated by commas: "
                  "Please enter 3 integers separated by commas: "
                  "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: 0, 0, 0\n"
                  "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: 3, 2, 1\n"
                  "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: 3, 2, 1\n"
                  "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: 1, 0, -2\n"
                  "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: 3, 2, 1\n"
                  "Please enter 3 integers separated by commas: The 3 integers sorted in decreasing order: 3, 2, 1\n";

  auto msg = std::string("CHECK ex_0012_DecreasingOutput() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
