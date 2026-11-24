extern "C"
{
  #include "../../../Exercises/ex_0188_ReverseArrayPtr/ex_0188_ReverseArrayPtr.c"
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

static void checkReverse(const std::vector<int> &initial_source, int fill)
{
  int size = (int)initial_source.size();
  std::vector<int> source = initial_source;
  std::vector<int> destination(initial_source.size(), fill);
  std::vector<int> expected(initial_source.rbegin(), initial_source.rend());

  ex_0188_ReverseArrayPtr(source.data(), destination.data(), size);

  std::string call = "ex_0188_ReverseArrayPtr(source, destination, " + std::to_string(size) +
                     ") with source = " + toString(initial_source);
  EXPECT_EQ(destination, expected) << Utils::formatError(call + ": destination should be " + toString(expected) +
                                                         " but is " + toString(destination));
  EXPECT_EQ(source, initial_source) << Utils::formatError(call + ": source should still be " +
                                                          toString(initial_source) + " but is " + toString(source));
}

TEST(ex_0188, Examples)
{
  checkReverse({1, 2, 3, 4, 5}, 0);
  checkReverse({-3, 8, 0, 12}, 0);
  checkReverse({7, 7, 2}, 0);
  checkReverse({42}, 0);
}

TEST(ex_0188, EvenAndOddSizes)
{
  checkReverse({10, 20}, -1);
  checkReverse({5, -6, 7}, -1);
  checkReverse({1, 2, 3, 4, 5, 6}, -1);
  checkReverse({3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}, -1);
}

TEST(ex_0188, OtherValues)
{
  checkReverse({2147483647, -2147483647 - 1, 0}, 99);
  checkReverse({-8}, 99);
  checkReverse({4, 9, 4}, 99);
  checkReverse({-1, -2, -3, -4}, 99);
}
