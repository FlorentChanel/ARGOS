extern "C"
{
  #include "../../../Exercises/ex_0033_SwapPtr/ex_0033_SwapPtr.c"
}

#include <gtest/gtest.h>

#include <string>
#include <utility>
#include <vector>

#include "Common/Utils.h"

static void checkSwap(int initial_x, int initial_y)
{
  int x = initial_x;
  int y = initial_y;
  ex_0033_SwapPtr(&x, &y);

  std::string call = "ex_0033_SwapPtr(&x, &y) with x = " + std::to_string(initial_x) +
                     " and y = " + std::to_string(initial_y);
  EXPECT_EQ(x, initial_y) << Utils::formatError(call + ": x should be " + std::to_string(initial_y));
  EXPECT_EQ(y, initial_x) << Utils::formatError(call + ": y should be " + std::to_string(initial_x));
}

TEST(ex_0033, Examples)
{
  std::vector<std::pair<int, int>> values_to_test = {{3, 8}, {-5, 0}, {7, 7}};

  for (const auto &values : values_to_test)
  {
    checkSwap(values.first, values.second);
  }
}

TEST(ex_0033, OtherValues)
{
  std::vector<std::pair<int, int>> values_to_test = {
    {1, 2}, {100, -100}, {-42, -13}, {0, 0}, {2147483647, -2147483647 - 1}};

  for (const auto &values : values_to_test)
  {
    checkSwap(values.first, values.second);
  }
}
