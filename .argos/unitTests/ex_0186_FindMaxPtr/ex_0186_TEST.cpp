extern "C"
{
  #include "../../../Exercises/ex_0186_FindMaxPtr/ex_0186_FindMaxPtr.c"
}

#include <gtest/gtest.h>

#include <string>
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

static void checkMax(const std::vector<int> &data, int size, int expectedIndex)
{
  std::vector<int> values = data;
  int *p = ex_0186_FindMaxPtr(values.data(), size);

  std::string call = "p = ex_0186_FindMaxPtr(" + arrayToString(data) + ", " + std::to_string(size) + ")";
  std::string expected = "&values[" + std::to_string(expectedIndex) + "]";
  if (p == nullptr)
  {
    ADD_FAILURE() << Utils::formatError(call + ": p is NULL, expected " + expected);
    return;
  }

  ptrdiff_t offset = p - values.data();
  if (offset < 0 || offset >= size)
  {
    ADD_FAILURE() << Utils::formatError(call + ": p does not point into values, expected " + expected);
    return;
  }

  EXPECT_EQ(p, values.data() + expectedIndex) << Utils::formatError(call + ": p is &values[" + std::to_string(offset) + "], expected " + expected);
  EXPECT_EQ(*p, data[expectedIndex]) << Utils::formatError(call + ": *p is " + std::to_string(*p) + ", expected " + std::to_string(data[expectedIndex]));
}

TEST(ex_0186, ReadmeExamples)
{
  checkMax({3, 8, 1, 6}, 4, 1);
  checkMax({-7, -2, -9}, 3, 1);
  checkMax({5, 9, 2, 9}, 4, 1);
  checkMax({4}, 1, 0);
}

TEST(ex_0186, MaxAtVariousPositions)
{
  checkMax({10, 3, 7, 2}, 4, 0);
  checkMax({1, 4, 6, 15}, 4, 3);
  checkMax({0, -3, 0, -1}, 4, 0);
  checkMax({-4, -8, -1, -6, -2}, 5, 2);
  checkMax({6, 6, 6}, 3, 0);
  checkMax({2, 11, 5, 11, 11, 0}, 6, 1);
}

TEST(ex_0186, OnlyFirstSizeElements)
{
  checkMax({3, 1, 20, 50}, 2, 0);
  checkMax({3, 7, 5, 50}, 3, 1);
  checkMax({-1, -5, 9}, 1, 0);
}

TEST(ex_0186, WriteThroughReturnedPointer)
{
  struct Case
  {
    std::vector<int> data;
    int newValue;
    std::vector<int> expected;
  };
  std::vector<Case> cases = {{{2, 7, 4}, 0, {2, 0, 4}},
                             {{9, 1, 5}, -3, {-3, 1, 5}},
                             {{1, 5, 8}, 12, {1, 5, 12}}};

  for (const Case &c : cases)
  {
    std::vector<int> values = c.data;
    int size = static_cast<int>(values.size());
    int *p = ex_0186_FindMaxPtr(values.data(), size);

    std::string call = "*ex_0186_FindMaxPtr(" + arrayToString(c.data) + ", " + std::to_string(size) + ") = " + std::to_string(c.newValue);
    if (p == nullptr || p < values.data() || p >= values.data() + size)
    {
      ADD_FAILURE() << Utils::formatError(call + ": the returned pointer does not point into values");
      continue;
    }

    *p = c.newValue;
    EXPECT_EQ(values, c.expected) << Utils::formatError(call + ": values is " + arrayToString(values) + ", expected " + arrayToString(c.expected));
  }
}
