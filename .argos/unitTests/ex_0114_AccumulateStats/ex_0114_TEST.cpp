extern "C"
{
  #include "../../../Exercises/ex_0114_AccumulateStats/ex_0114_AccumulateStats.c"
}

#include <gtest/gtest.h>

#include <string>
#include <vector>

#include "Common/Utils.h"

static std::string describe(const std::vector<int> &values, int count)
{
  std::string text = "ex_0114_AccumulateStats({";
  for (size_t i = 0; i < values.size(); ++i)
  {
    if (i > 0)
    {
      text += ", ";
    }
    text += std::to_string(values[i]);
  }
  return text + "}, " + std::to_string(count) + ", &sum, &mean)";
}

static void checkStats(const std::vector<int> &initial_values, int count, int expected_sum, double expected_mean)
{
  std::vector<int> values = initial_values;
  int sum = 123456;
  double mean = -98765.25;
  ex_0114_AccumulateStats(values.data(), count, &sum, &mean);

  std::string call = describe(initial_values, count);
  EXPECT_EQ(sum, expected_sum) << Utils::formatError(call + ": sum should be " + std::to_string(expected_sum));
  EXPECT_NEAR(mean, expected_mean, 1e-9) << Utils::formatError(call + ": mean should be " + std::to_string(expected_mean));
  EXPECT_EQ(values, initial_values) << Utils::formatError(call + ": values should not be modified");
}

TEST(ex_0114, Examples)
{
  checkStats({1, 2, 3, 4}, 4, 10, 2.5);
  checkStats({-3, 7, 2}, 3, 6, 2.0);
  checkStats({-4, -1}, 2, -5, -2.5);
  checkStats({5}, 1, 5, 5.0);
}

TEST(ex_0114, OnlyFirstCountValues)
{
  checkStats({1, 2, 3, 4}, 2, 3, 1.5);
  checkStats({10, 20, 30, 40, 50}, 3, 60, 20.0);
  checkStats({-7, 100, 100}, 1, -7, -7.0);
}

TEST(ex_0114, OtherValues)
{
  checkStats({1, 2, 4}, 3, 7, 7.0 / 3.0);
  checkStats({0, 0, 0}, 3, 0, 0.0);
  checkStats({-1, 0}, 2, -1, -0.5);
  checkStats({1000, -250, 3, 8, 9}, 5, 770, 154.0);
  checkStats({2, 3}, 2, 5, 2.5);
}
