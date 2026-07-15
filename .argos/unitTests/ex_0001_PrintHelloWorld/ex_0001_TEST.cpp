extern "C"
{
  #include "../../../Exercises/ex_0001_PrintHelloWorld/ex_0001_PrintHelloWorld.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0001, PrintHelloWorld)
{
  testing::internal::CaptureStdout();
  ex_0001_PrintHelloWorld();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "hello, world\n";

  auto msg = std::string("CHECK ex_0001_PrintHelloWorld() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
