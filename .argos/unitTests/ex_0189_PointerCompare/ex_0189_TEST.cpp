extern "C"
{
  #include "../../../Exercises/ex_0189_PointerCompare/ex_0189_PointerCompare.c"
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

static void checkCompare(const std::vector<int> &first, const std::vector<int> &second, int size, int expected)
{
  std::vector<int> a = first;
  std::vector<int> b = second;
  int result = ex_0189_PointerCompare(a.data(), b.data(), size);

  std::string call = "ex_0189_PointerCompare(" + arrayToString(first) + ", " + arrayToString(second) + ", " + std::to_string(size) + ")";
  EXPECT_EQ(result, expected) << Utils::formatError(call + " returned " + std::to_string(result) + ", expected " + std::to_string(expected));
  EXPECT_EQ(a, first) << Utils::formatError(call + ": first was modified to " + arrayToString(a));
  EXPECT_EQ(b, second) << Utils::formatError(call + ": second was modified to " + arrayToString(b));
}

TEST(ex_0189, ReadmeExamples)
{
  checkCompare({1, 2, 3, 4}, {1, 2, 3, 4}, 4, 0);
  checkCompare({1, 2, 3, 4}, {1, 2, 5, 0}, 4, -1);
  checkCompare({7, -2, 9}, {7, -8, 100}, 3, 1);
  checkCompare({5, 6, 7}, {5, 6, 8}, 2, 0);
  checkCompare({1}, {2}, 0, 0);

  int data[] = {3, 4, 3, 4, 9};
  int result = ex_0189_PointerCompare(data, data + 2, 3);
  EXPECT_EQ(result, -1) << Utils::formatError("data = {3, 4, 3, 4, 9}; ex_0189_PointerCompare(data, data + 2, 3) returned " + std::to_string(result) + ", expected -1");
}

TEST(ex_0189, DifferenceAtVariousPositions)
{
  checkCompare({9, 1, 1}, {2, 1, 1}, 3, 1);
  checkCompare({-5, 0, 0}, {3, 0, 0}, 3, -1);
  checkCompare({4, 8, 15, 16}, {4, 8, 15, 23}, 4, -1);
  checkCompare({4, 8, 15, 42}, {4, 8, 15, 23}, 4, 1);
  checkCompare({0, -1, 6, 2}, {0, -3, 1, 9}, 4, 1);
  checkCompare({10, 20, 30, 40, 50}, {10, 20, 30, 40, 50}, 5, 0);
}

TEST(ex_0189, FirstDifferenceDecides)
{
  checkCompare({1, 100, 100}, {2, 0, 0}, 3, -1);
  checkCompare({3, -50}, {1, 50}, 2, 1);
  checkCompare({6, 6, 0, 99}, {6, 6, 1, -99}, 4, -1);
  checkCompare({-2, 7, 8}, {-2, 7, 8}, 3, 0);
}

TEST(ex_0189, OnlyFirstSizeElements)
{
  checkCompare({1, 2, 3, 99}, {1, 2, 3, -99}, 3, 0);
  checkCompare({1, 2, 3, 99}, {1, 2, 3, -99}, 4, 1);
  checkCompare({8, 0}, {8, 5}, 1, 0);
  checkCompare({8, 0}, {8, 5}, 2, -1);
  checkCompare({-4}, {-9}, 1, 1);
}

TEST(ex_0189, ZonesInsideTheSameArray)
{
  struct Case
  {
    int firstOffset;
    int secondOffset;
    int size;
    int expected;
  };
  const std::vector<int> original = {2, 5, 2, 5, 2, 7, 1};
  std::vector<Case> cases = {{0, 2, 4, -1},
                             {2, 0, 4, 1},
                             {0, 2, 2, 0},
                             {1, 3, 1, 0},
                             {5, 0, 2, 1},
                             {6, 0, 1, -1}};

  for (const Case &c : cases)
  {
    std::vector<int> data = original;
    int result = ex_0189_PointerCompare(data.data() + c.firstOffset, data.data() + c.secondOffset, c.size);

    std::string call = "data = " + arrayToString(original) + "; ex_0189_PointerCompare(data + " + std::to_string(c.firstOffset) + ", data + " + std::to_string(c.secondOffset) + ", " + std::to_string(c.size) + ")";
    EXPECT_EQ(result, c.expected) << Utils::formatError(call + " returned " + std::to_string(result) + ", expected " + std::to_string(c.expected));
    EXPECT_EQ(data, original) << Utils::formatError(call + ": data was modified to " + arrayToString(data));
  }
}
