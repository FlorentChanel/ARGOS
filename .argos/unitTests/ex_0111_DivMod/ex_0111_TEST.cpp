extern "C"
{
  #include "../../../Exercises/ex_0111_DivMod/ex_0111_DivMod.c"
}

#include <gtest/gtest.h>

#include <string>
#include <vector>

#include "Common/Utils.h"

struct DivModCase
{
  int dividend;
  int divisor;
  int expected_quotient;
  int expected_remainder;
};

static void checkDivMod(const DivModCase &c)
{
  int q = -12345;
  int r = -12345;
  ex_0111_DivMod(c.dividend, c.divisor, &q, &r);

  std::string call = "ex_0111_DivMod(" + std::to_string(c.dividend) + ", " +
                     std::to_string(c.divisor) + ", &q, &r)";
  EXPECT_EQ(q, c.expected_quotient)
    << Utils::formatError(call + ": q should be " + std::to_string(c.expected_quotient));
  EXPECT_EQ(r, c.expected_remainder)
    << Utils::formatError(call + ": r should be " + std::to_string(c.expected_remainder));
}

TEST(ex_0111, Examples)
{
  std::vector<DivModCase> cases = {
    {17, 5, 3, 2}, {20, 4, 5, 0}, {3, 8, 0, 3}, {-17, 5, -3, -2}};

  for (const auto &c : cases)
  {
    checkDivMod(c);
  }
}

TEST(ex_0111, PositiveDividend)
{
  std::vector<DivModCase> cases = {
    {100, 7, 14, 2}, {9, 3, 3, 0}, {1, 2, 0, 1}, {0, 6, 0, 0}, {25, 1, 25, 0}};

  for (const auto &c : cases)
  {
    checkDivMod(c);
  }
}

TEST(ex_0111, NegativeDividend)
{
  std::vector<DivModCase> cases = {
    {-23, 4, -5, -3}, {-20, 4, -5, 0}, {-3, 8, 0, -3}, {-9, 1, -9, 0}};

  for (const auto &c : cases)
  {
    checkDivMod(c);
  }
}

TEST(ex_0111, NegativeDivisor)
{
  std::vector<DivModCase> cases = {
    {17, -5, -3, 2}, {-17, -5, 3, -2}, {20, -4, -5, 0}, {3, -8, 0, 3}, {-7, -1, 7, 0}};

  for (const auto &c : cases)
  {
    checkDivMod(c);
  }
}
