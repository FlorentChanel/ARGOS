extern "C"
{
  #include "../../../Exercises/ex_0007_Printf/ex_0007_Printf.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0007, Printf)
{
  testing::internal::CaptureStdout();
  ex_0007_Printf();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Initials: __\nCode: __\n\n\nBirthdate: __/__/__\nNumber: __\\__\nText: \"____\"\n";

  auto msg = std::string("CHECK ex_0007_Printf() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
