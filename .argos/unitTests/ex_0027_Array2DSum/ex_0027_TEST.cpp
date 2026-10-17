extern "C"
{
  #include "../../../Exercises/ex_0027_Array2DSum/ex_0027_Array2DSum.c"
}

#include <gtest/gtest.h>

#include <cstdio>
#include <string>

#include "Common/Utils.h"

static std::string callAndCapture()
{
  testing::internal::CaptureStdout();
  ex_0027_Array2DSum();
  return testing::internal::GetCapturedStdout();
}

static std::string valuePrompts(int nbLines, int nbColumns)
{
  std::string prompts;
  for (int i = 0; i < nbLines; ++i)
  {
    for (int j = 0; j < nbColumns; ++j)
    {
      prompts += "array[" + std::to_string(i) + "][" + std::to_string(j) + "]: ";
    }
  }
  return prompts;
}

TEST(ex_0027, Array2DSum)
{
  // Feed the sizes and values through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0027_inputs.txt", "r", stdin), nullptr);

  auto msg = std::string("CHECK ex_0027_Array2DSum() output!");

  std::string expected = "Nb lines (max.50): "
                         "Nb lines (max.50): "
                         "Nb lines (max.50): "
                         "Nb columns (max.50): "
                         "Nb columns (max.50): "
                         "Nb columns (max.50): array[0][0]: array[0][1]: array[1][0]: array[1][1]: Total sum: 10\n";
  EXPECT_EQ(expected, callAndCapture()) << Utils::formatError(msg + " (README example 1)");

  expected = "Nb lines (max.50): Nb columns (max.50): Total sum: 0\n";
  EXPECT_EQ(expected, callAndCapture()) << Utils::formatError(msg + " (0 lines, 9 columns)");
  EXPECT_EQ(expected, callAndCapture()) << Utils::formatError(msg + " (9 lines, 0 columns)");
  EXPECT_EQ(expected, callAndCapture()) << Utils::formatError(msg + " (0 lines, 0 columns)");

  expected = "Nb lines (max.50): Nb lines (max.50): "
             "Nb columns (max.50): Nb columns (max.50): " +
             valuePrompts(1, 50) + "Total sum: 1275\n";
  EXPECT_EQ(expected, callAndCapture()) << Utils::formatError(msg + " (51 rejected, 1 line, 50 columns)");

  expected = "Nb lines (max.50): Nb columns (max.50): " + valuePrompts(50, 1) + "Total sum: 1275\n";
  EXPECT_EQ(expected, callAndCapture()) << Utils::formatError(msg + " (50 lines, 1 column)");

  expected = "Nb lines (max.50): Nb columns (max.50): "
             "array[0][0]: array[0][1]: array[0][1]: Total sum: 12\n";
  EXPECT_EQ(expected, callAndCapture()) << Utils::formatError(msg + " (invalid array value)");

  expected = "Nb lines (max.50): Nb columns (max.50): " + valuePrompts(2, 3) + "Total sum: 5\n";
  EXPECT_EQ(expected, callAndCapture()) << Utils::formatError(msg + " (2 lines, 3 columns, negative values)");
}
