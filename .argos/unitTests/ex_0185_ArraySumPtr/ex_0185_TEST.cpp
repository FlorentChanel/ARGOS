extern "C"
{
  #include "../../../Exercises/ex_0185_ArraySumPtr/ex_0185_ArraySumPtr.c"
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

TEST(ex_0185, WholeArray)
{
  auto values_to_test = {std::make_tuple(std::vector<int>{1, 2, 3, 4}, 10), std::make_tuple(std::vector<int>{-5, 8, -3, 2, 7}, 9), std::make_tuple(std::vector<int>{42}, 42), std::make_tuple(std::vector<int>{-1, -2, -3}, -6), std::make_tuple(std::vector<int>{5, -5, 12, -12}, 0), std::make_tuple(std::vector<int>{100, 250, 0, 650, 1000, -1}, 1999)};

  for (auto val : values_to_test)
  {
    auto data = std::get<0>(val);
    auto expected = std::get<1>(val);
    int size = (int)data.size();

    int sum = ex_0185_ArraySumPtr(data.data(), size);

    std::string call = "ex_0185_ArraySumPtr(data, " + std::to_string(size) + ") with data = " + arrayToString(data);
    EXPECT_EQ(sum, expected) << Utils::formatError(call + ": returned " + std::to_string(sum) + ", expected " + std::to_string(expected));
  }
}

TEST(ex_0185, PartOfArray)
{
  std::vector<int> data = {10, 20, 30, 40};
  auto values_to_test = {std::make_tuple(1, 2, 50), std::make_tuple(0, 3, 60), std::make_tuple(2, 2, 70), std::make_tuple(3, 1, 40), std::make_tuple(0, 0, 0), std::make_tuple(2, 0, 0)};

  for (auto val : values_to_test)
  {
    auto offset = std::get<0>(val);
    auto size = std::get<1>(val);
    auto expected = std::get<2>(val);

    int sum = ex_0185_ArraySumPtr(data.data() + offset, size);

    std::string call = "ex_0185_ArraySumPtr(data + " + std::to_string(offset) + ", " + std::to_string(size) + ") with data = " + arrayToString(data);
    EXPECT_EQ(sum, expected) << Utils::formatError(call + ": returned " + std::to_string(sum) + ", expected " + std::to_string(expected));
  }
}

TEST(ex_0185, ArrayNotModified)
{
  auto values_to_test = {std::make_tuple(std::vector<int>{3, -7, 11, 2}, 9), std::make_tuple(std::vector<int>{-4, -4}, -8), std::make_tuple(std::vector<int>{0, 15, 0}, 15)};

  for (auto val : values_to_test)
  {
    auto original = std::get<0>(val);
    auto expected = std::get<1>(val);
    auto data = original;
    int size = (int)data.size();

    int sum = ex_0185_ArraySumPtr(data.data(), size);

    std::string call = "ex_0185_ArraySumPtr(data, " + std::to_string(size) + ") with data = " + arrayToString(original);
    EXPECT_EQ(sum, expected) << Utils::formatError(call + ": returned " + std::to_string(sum) + ", expected " + std::to_string(expected));
    EXPECT_EQ(data, original) << Utils::formatError(call + ": data became " + arrayToString(data) + ", expected it unchanged");
  }
}
