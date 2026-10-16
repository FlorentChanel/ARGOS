extern "C"
{
  #include "../../../Exercises/ex_0011_MultiplicationSign/ex_0011_MultiplicationSign.c"
}

#include <gtest/gtest.h>

#include <cstdio>

#include "Common/Utils.h"

TEST(ex_0011, MultiplicationSign)
{
  // Feed the integers through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0011_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0011_MultiplicationSign();
  ex_0011_MultiplicationSign();
  ex_0011_MultiplicationSign();
  ex_0011_MultiplicationSign();
  ex_0011_MultiplicationSign();
  ex_0011_MultiplicationSign();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Please enter 2 integers: 1 * 2 > 0\n"
                  "Please enter 2 integers: -2 * -3 > 0\n"
                  "Please enter 2 integers: -3 * 0 = 0\n"
                  "Please enter 2 integers: "
                  "Please enter 2 integers: "
                  "Please enter 2 integers: 12 * -13 < 0\n"
                  "Please enter 2 integers: 0 * 0 = 0\n"
                  "Please enter 2 integers: -1 * 3 < 0\n";

  auto msg = std::string("CHECK ex_0011_MultiplicationSign() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
