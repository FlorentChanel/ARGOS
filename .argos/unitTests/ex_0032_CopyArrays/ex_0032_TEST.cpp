extern "C"
{
  #include "../../../Exercises/ex_0032_CopyArrays/ex_0032_CopyArrays.c"
}

#include <gtest/gtest.h>

#include <string>
#include <vector>

#include "Common/Utils.h"

static std::string toString(const std::vector<int> &values)
{
  std::string text = "{";
  for (size_t i = 0; i < values.size(); i++)
  {
    if (i > 0)
    {
      text += ", ";
    }
    text += std::to_string(values[i]);
  }
  return text + "}";
}

static void checkCopy(const std::vector<int> &initial_src, const std::vector<int> &initial_dst, int n)
{
  std::vector<int> src = initial_src;
  std::vector<int> dst = initial_dst;

  std::vector<int> expected_dst = initial_dst;
  for (int i = 0; i < n; i++)
  {
    expected_dst[i] = initial_src[i];
  }

  ex_0032_CopyArrays(src.data(), dst.data(), n);

  std::string call = "ex_0032_CopyArrays(src, dst, " + std::to_string(n) + ") with src = " +
                     toString(initial_src) + " and dst = " + toString(initial_dst);
  EXPECT_EQ(dst, expected_dst) << Utils::formatError(call + ": dst should be " + toString(expected_dst) +
                                                     " but is " + toString(dst));
  EXPECT_EQ(src, initial_src) << Utils::formatError(call + ": src should still be " + toString(initial_src) +
                                                    " but is " + toString(src));
}

TEST(ex_0032, Examples)
{
  checkCopy({4, -1, 7, 0, 12}, {0, 0, 0, 0, 0}, 5);
  checkCopy({9, 8, 7, 6}, {1, 1, 1, 1, 1, 1}, 3);
  checkCopy({5, 5}, {3, 3}, 0);
}

TEST(ex_0032, PartialCopyKeepsRestOfDestination)
{
  checkCopy({42, 43, 44}, {-1, -2, -3, -4}, 1);
  checkCopy({10, 20, 30, 40, 50}, {7, 8, 9, 10, 11}, 2);
  checkCopy({1, 2, 3}, {9, 9, 9}, 0);
  checkCopy({-6, -5, -4, -3}, {100, 200, 300, 400}, 4);
}

TEST(ex_0032, OtherValues)
{
  checkCopy({2147483647, -2147483647 - 1, 0}, {1, 2, 3}, 3);
  checkCopy({3, 1, 4, 1, 5, 9, 2, 6, 5, 3}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, 10);
  checkCopy({-8}, {8}, 1);
  checkCopy({6, 6, 6}, {6, 6, 6}, 3);
}
