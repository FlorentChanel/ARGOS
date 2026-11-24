extern "C"
{
  #include "../../../Exercises/ex_0183_CountViaPtr/ex_0183_CountViaPtr.c"
}

#include <gtest/gtest.h>

#include <string>
#include <tuple>
#include <vector>

#include "Common/Utils.h"

static std::string arrayToString(const std::vector<int> &values)
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

static void checkCount(const std::vector<int> &data, int size, int target, int initial, int expected)
{
  std::vector<int> values = data;
  int count = initial;
  ex_0183_CountViaPtr(values.data(), size, target, &count);

  std::string call = "ex_0183_CountViaPtr(" + arrayToString(data) + ", " + std::to_string(size) + ", " + std::to_string(target) + ", &n) with n = " + std::to_string(initial);
  EXPECT_EQ(count, expected) << Utils::formatError(call + ": n is " + std::to_string(count) + ", expected " + std::to_string(expected));
  EXPECT_EQ(values, data) << Utils::formatError(call + ": values is " + arrayToString(values) + ", expected unchanged " + arrayToString(data));
}

TEST(ex_0183, ReadmeExamples)
{
  checkCount({3, 1, 3, 7, 3}, 5, 3, 0, 3);
  checkCount({-2, 4, -2, 0}, 4, -2, 0, 2);
  checkCount({5, 6, 8}, 3, 9, 42, 0);
  checkCount({1, 1, 1}, 3, 1, 10, 3);
  checkCount({7}, 0, 7, 5, 0);
}

TEST(ex_0183, VariousArrays)
{
  auto values_to_test = {std::make_tuple(std::vector<int>{4, 0, 4, 0, 0, 9}, 0, 3),
                         std::make_tuple(std::vector<int>{4, 0, 4, 0, 0, 9}, 4, 2),
                         std::make_tuple(std::vector<int>{4, 0, 4, 0, 0, 9}, 9, 1),
                         std::make_tuple(std::vector<int>{-5, -5, -5, -5}, -5, 4),
                         std::make_tuple(std::vector<int>{12}, 12, 1),
                         std::make_tuple(std::vector<int>{12}, 13, 0)};

  for (auto val : values_to_test)
  {
    auto data = std::get<0>(val);
    checkCount(data, static_cast<int>(data.size()), std::get<1>(val), 99, std::get<2>(val));
  }
}

TEST(ex_0183, OnlyFirstSizeElements)
{
  checkCount({2, 2, 5, 2, 2}, 3, 2, 7, 2);
  checkCount({2, 2, 5, 2, 2}, 1, 2, 7, 1);
  checkCount({8, 1, 8, 8}, 2, 8, -3, 1);
  checkCount({8, 1, 8, 8}, 0, 8, 6, 0);
}
