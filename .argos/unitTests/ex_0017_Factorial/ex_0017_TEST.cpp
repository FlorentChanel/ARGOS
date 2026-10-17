extern "C"
{
  #include "../../../Exercises/ex_0017_Factorial/ex_0017_Factorial.c"
}

#include <gtest/gtest.h>

#include <cstdio>
#include <string>

#include "Common/Utils.h"

TEST(ex_0017, Factorial)
{
  // Feed N through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0017_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0017_Factorial();
  ex_0017_Factorial();
  ex_0017_Factorial();
  ex_0017_Factorial();
  ex_0017_Factorial();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Please enter a non-negative integer N: 6! = 720\n"
                  "Please enter a non-negative integer N: "
                  "Please enter a non-negative integer N: "
                  "Please enter a non-negative integer N: 6! = 720\n"
                  "Please enter a non-negative integer N: 0! = 1\n"
                  "Please enter a non-negative integer N: 1! = 1\n"
                  "Please enter a non-negative integer N: 20! = 2432902008176640000\n";

  auto msg = std::string("CHECK ex_0017_Factorial() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
