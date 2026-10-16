extern "C"
{
  #include "../../../Exercises/ex_0008_ScanfPrintf/ex_0008_ScanfPrintf.c"
}

#include <gtest/gtest.h>

#include <cstdio>

#include "Common/Utils.h"

TEST(ex_0008, ScanfPrintf)
{
  // Feed the letters through stdin (fixture shipped next to the binary):
  // space-separated, no separator, then one letter per line.
  ASSERT_NE(freopen("ex_0008_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0008_ScanfPrintf();
  ex_0008_ScanfPrintf();
  ex_0008_ScanfPrintf();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "\n\nPlease enter 3 letters:\n\nHere are the corresponding ASCII codes:\n"
                  "a--------->97\nb--------->98\nc--------->99\n"
                  "\n\nPlease enter 3 letters:\n\nHere are the corresponding ASCII codes:\n"
                  "x--------->120\ny--------->121\nz--------->122\n"
                  "\n\nPlease enter 3 letters:\n\nHere are the corresponding ASCII codes:\n"
                  "K--------->75\nL--------->76\nM--------->77\n";

  auto msg = std::string("CHECK ex_0008_ScanfPrintf() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
