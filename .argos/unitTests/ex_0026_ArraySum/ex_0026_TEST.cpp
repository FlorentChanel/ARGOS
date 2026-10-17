extern "C"
{
  #include "../../../Exercises/ex_0026_ArraySum/ex_0026_ArraySum.c"
}

#include <gtest/gtest.h>

#include <cstdio>
#include <string>

#include "Common/Utils.h"

TEST(ex_0026, ArraySum)
{
  // Feed the values through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0026_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0026_ArraySum();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Nb values (max.50): "
                  "Nb values (max.50): "
                  "Nb values (max.50): "
                  "Nb values (max.50): "
                  "Nb values (max.50): array:\n\n"
                  "Total sum: 0\n";

  EXPECT_EQ(expected, actual) << Utils::formatError("CHECK ex_0026_ArraySum() output!");

  testing::internal::CaptureStdout();
  ex_0026_ArraySum();

  actual = testing::internal::GetCapturedStdout();
  expected = "Nb values (max.50): "
             "Value 0? "
             "Value 1? "
             "Value 2? "
             "Value 3? "
             "array:\n-2 -1 0 1\n"
             "Total sum: -2\n";

  EXPECT_EQ(expected, actual) << Utils::formatError("CHECK ex_0026_ArraySum() output with 4 values!");

  testing::internal::CaptureStdout();
  ex_0026_ArraySum();

  actual = testing::internal::GetCapturedStdout();
  expected = "Nb values (max.50): "
             "Nb values (max.50): "
             "Value 0? "
             "Value 1? "
             "array:\n3 4\n"
             "Total sum: 7\n";

  EXPECT_EQ(expected, actual) << Utils::formatError("CHECK ex_0026_ArraySum() rejects n above 50!");

  testing::internal::CaptureStdout();
  ex_0026_ArraySum();

  actual = testing::internal::GetCapturedStdout();
  std::string expectedMax = "Nb values (max.50): ";
  std::string arrayLine;
  for (int i = 0; i < 50; ++i)
  {
    expectedMax += "Value " + std::to_string(i) + "? ";
    arrayLine += (i == 0 ? "" : " ") + std::to_string(i + 1);
  }
  expectedMax += "array:\n" + arrayLine + "\nTotal sum: 1275\n";

  EXPECT_EQ(expectedMax, actual) << Utils::formatError("CHECK ex_0026_ArraySum() accepts n = 50!");

  testing::internal::CaptureStdout();
  ex_0026_ArraySum();

  actual = testing::internal::GetCapturedStdout();
  expected = "Nb values (max.50): "
             "Value 0? "
             "Value 0? "
             "Value 1? "
             "array:\n5 6\n"
             "Total sum: 11\n";

  EXPECT_EQ(expected, actual) << Utils::formatError("CHECK ex_0026_ArraySum() prompts again after an invalid value!");
}
