extern "C"
{
  #include "../../../Exercises/ex_0190_ReverseInplacePtr/ex_0190_ReverseInplacePtr.c"
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

static void checkReverse(const std::vector<int> &initial)
{
  int size = (int)initial.size();
  std::vector<int> array = initial;
  std::vector<int> expected(initial.rbegin(), initial.rend());

  ex_0190_ReverseInplacePtr(array.data(), size);

  std::string call = "ex_0190_ReverseInplacePtr(array, " + std::to_string(size) + ") with array = " +
                     toString(initial);
  EXPECT_EQ(array, expected) << Utils::formatError(call + ": array should be " + toString(expected) +
                                                   " but is " + toString(array));
}

TEST(ex_0190, Examples)
{
  checkReverse({1, 2, 3, 4, 5});
  checkReverse({-3, 8, 0, 12});
  checkReverse({7, 7, 2});
  checkReverse({42});
}

TEST(ex_0190, EvenAndOddSizes)
{
  checkReverse({10, 20});
  checkReverse({5, -6, 7});
  checkReverse({1, 2, 3, 4, 5, 6});
  checkReverse({3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5});
}

TEST(ex_0190, OtherValues)
{
  checkReverse({2147483647, -2147483647 - 1, 0});
  checkReverse({-8});
  checkReverse({4, 9, 4});
  checkReverse({-1, -2, -3, -4});
}
