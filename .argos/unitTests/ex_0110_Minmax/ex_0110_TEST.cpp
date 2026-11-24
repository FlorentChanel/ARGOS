extern "C"
{
  #include "../../../Exercises/ex_0110_Minmax/ex_0110_Minmax.c"
}

#include <gtest/gtest.h>

#include <climits>
#include <string>
#include <vector>

#include "Common/Utils.h"

struct MinmaxCase
{
  int a;
  int b;
  int c;
  int expected_min;
  int expected_max;
};

static void checkMinmax(const MinmaxCase &test_case)
{
  int lo = 123456;
  int hi = -123456;
  ex_0110_Minmax(test_case.a, test_case.b, test_case.c, &lo, &hi);

  std::string call = "ex_0110_Minmax(" + std::to_string(test_case.a) + ", " + std::to_string(test_case.b) +
                     ", " + std::to_string(test_case.c) + ", &lo, &hi)";
  EXPECT_EQ(lo, test_case.expected_min)
    << Utils::formatError(call + ": lo should be " + std::to_string(test_case.expected_min));
  EXPECT_EQ(hi, test_case.expected_max)
    << Utils::formatError(call + ": hi should be " + std::to_string(test_case.expected_max));
}

TEST(ex_0110, Examples)
{
  std::vector<MinmaxCase> cases = {
    {4, 9, 2, 2, 9}, {-3, 0, -8, -8, 0}, {5, 5, 1, 1, 5}, {7, 7, 7, 7, 7}};

  for (const auto &test_case : cases)
  {
    checkMinmax(test_case);
  }
}

TEST(ex_0110, AllOrders)
{
  std::vector<MinmaxCase> cases = {
    {1, 2, 3, 1, 3}, {1, 3, 2, 1, 3}, {2, 1, 3, 1, 3},
    {2, 3, 1, 1, 3}, {3, 1, 2, 1, 3}, {3, 2, 1, 1, 3},
    {-5, 0, 8, -5, 8}, {-5, 8, 0, -5, 8}, {0, -5, 8, -5, 8},
    {0, 8, -5, -5, 8}, {8, -5, 0, -5, 8}, {8, 0, -5, -5, 8}};

  for (const auto &test_case : cases)
  {
    checkMinmax(test_case);
  }
}

TEST(ex_0110, RepeatedValues)
{
  std::vector<MinmaxCase> cases = {
    {2, 6, 6, 2, 6}, {6, 2, 6, 2, 6}, {-4, -4, 10, -4, 10}, {10, -4, -4, -4, 10}, {0, 0, 0, 0, 0}};

  for (const auto &test_case : cases)
  {
    checkMinmax(test_case);
  }
}

TEST(ex_0110, ExtremeValues)
{
  std::vector<MinmaxCase> cases = {
    {INT_MAX, 0, INT_MIN, INT_MIN, INT_MAX},
    {INT_MIN, INT_MIN, -1, INT_MIN, -1},
    {INT_MAX, 1, INT_MAX, 1, INT_MAX},
    {-100, -200, -300, -300, -100}};

  for (const auto &test_case : cases)
  {
    checkMinmax(test_case);
  }
}
