extern "C"
{
  #include "../../../Exercises/ex_0010_LowercaseUppercase/ex_0010_LowercaseUppercase.c"
}

#include <gtest/gtest.h>

#include <cstdio>

#include "Common/Utils.h"

TEST(ex_0010, LowercaseUppercase)
{
  // Feed the characters through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0010_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  for (int i = 0; i < 12; i++)
  {
    ex_0010_LowercaseUppercase();
  }

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Type a letter: lowercase\n"
                  "Type a letter: lowercase\n"
                  "Type a letter: lowercase\n"
                  "Type a letter: UPPERCASE\n"
                  "Type a letter: UPPERCASE\n"
                  "Type a letter: UPPERCASE\n"
                  "Type a letter: The character you entered is not a letter.\n"
                  "Type a letter: The character you entered is not a letter.\n"
                  "Type a letter: The character you entered is not a letter.\n"
                  "Type a letter: The character you entered is not a letter.\n"
                  "Type a letter: The character you entered is not a letter.\n"
                  "Type a letter: The character you entered is not a letter.\n";

  auto msg = std::string("CHECK ex_0010_LowercaseUppercase() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
