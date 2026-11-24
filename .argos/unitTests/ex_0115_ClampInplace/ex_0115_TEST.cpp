extern "C"
{
  #include "../../../Exercises/ex_0115_ClampInplace/ex_0115_ClampInplace.c"
}

#include <gtest/gtest.h>

#include <string>
#include <vector>

#include "Common/Utils.h"

struct ClampCase
{
  int value;
  int min;
  int max;
  int expected;
};

static void checkClamp(const ClampCase &test_case)
{
  int value = test_case.value;
  ex_0115_ClampInplace(&value, test_case.min, test_case.max);

  std::string call = "ex_0115_ClampInplace(&value, " + std::to_string(test_case.min) + ", " +
                     std::to_string(test_case.max) + ") with value = " +
                     std::to_string(test_case.value);
  EXPECT_EQ(value, test_case.expected)
    << Utils::formatError(call + ": value should be " + std::to_string(test_case.expected));
}

TEST(ex_0115, Examples)
{
  std::vector<ClampCase> cases = {
    {15, 0, 10, 10}, {-3, 0, 10, 0}, {7, 0, 10, 7}, {-20, -10, -5, -10}};

  for (const auto &test_case : cases)
  {
    checkClamp(test_case);
  }
}

TEST(ex_0115, Boundaries)
{
  std::vector<ClampCase> cases = {
    {0, 0, 10, 0}, {10, 0, 10, 10}, {-1, 0, 10, 0}, {11, 0, 10, 10}, {-4, -10, -5, -5}};

  for (const auto &test_case : cases)
  {
    checkClamp(test_case);
  }
}

TEST(ex_0115, SingleValueInterval)
{
  std::vector<ClampCase> cases = {
    {3, 5, 5, 5}, {5, 5, 5, 5}, {8, 5, 5, 5}, {0, -2, -2, -2}, {-9, -2, -2, -2}};

  for (const auto &test_case : cases)
  {
    checkClamp(test_case);
  }
}

TEST(ex_0115, LargeValues)
{
  std::vector<ClampCase> cases = {
    {2147483647, -100, 100, 100}, {-2147483647 - 1, -100, 100, -100}, {42, -100, 100, 42}};

  for (const auto &test_case : cases)
  {
    checkClamp(test_case);
  }
}
