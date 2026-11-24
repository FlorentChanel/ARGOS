extern "C"
{
  #include "../../../Exercises/ex_0192_ArraySlice/ex_0192_ArraySlice.c"
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

static void checkSlice(const std::vector<int> &initial_source, int start, int end, int fill)
{
  int size = (int)initial_source.size();
  std::vector<int> source = initial_source;
  std::vector<int> destination(initial_source.size(), fill);

  bool valid = start >= 0 && end <= size && start <= end;
  int expected_count = valid ? end - start : -1;
  std::vector<int> expected(initial_source.size(), fill);
  if (valid)
  {
    for (int i = start; i < end; i++)
    {
      expected[i - start] = initial_source[i];
    }
  }

  int count = ex_0192_ArraySlice(source.data(), size, start, end, destination.data());

  std::string call = "ex_0192_ArraySlice(source, " + std::to_string(size) + ", " + std::to_string(start) + ", " +
                     std::to_string(end) + ", destination) with source = " + toString(initial_source) +
                     " and destination = " + toString(std::vector<int>(initial_source.size(), fill));
  EXPECT_EQ(count, expected_count) << Utils::formatError(call + ": should return " + std::to_string(expected_count) +
                                                         " but returns " + std::to_string(count));
  EXPECT_EQ(destination, expected) << Utils::formatError(call + ": destination should be " + toString(expected) +
                                                         " but is " + toString(destination));
  EXPECT_EQ(source, initial_source) << Utils::formatError(call + ": source should still be " +
                                                          toString(initial_source) + " but is " + toString(source));
}

TEST(ex_0192, Examples)
{
  checkSlice({10, 20, 30, 40, 50, 60}, 1, 4, 0);
  checkSlice({-5, 7, 0, 3}, 0, 4, 0);
  checkSlice({1, 2, 3, 4, 5}, 4, 5, 0);
  checkSlice({1, 2, 3}, 2, 2, 9);
  checkSlice({1, 2, 3}, 1, 4, 9);
  checkSlice({1, 2, 3}, -1, 2, 9);
  checkSlice({1, 2, 3}, 2, 1, 9);
}

TEST(ex_0192, ValidSlices)
{
  checkSlice({42}, 0, 1, -7);
  checkSlice({3, 1, 4, 1, 5, 9, 2, 6}, 0, 3, -7);
  checkSlice({3, 1, 4, 1, 5, 9, 2, 6}, 5, 8, -7);
  checkSlice({3, 1, 4, 1, 5, 9, 2, 6}, 2, 7, -7);
  checkSlice({2147483647, -2147483647 - 1, 0, -12}, 0, 2, -7);
  checkSlice({8, -8, 16}, 1, 2, -7);
}

TEST(ex_0192, EmptySlices)
{
  checkSlice({4, 5, 6, 7}, 0, 0, 11);
  checkSlice({4, 5, 6, 7}, 4, 4, 11);
  checkSlice({4, 5, 6, 7}, 1, 1, 11);
  checkSlice({4, 5, 6, 7}, 1, 2, 11);
  checkSlice({4, 5, 6, 7}, 3, 2, 11);
}

TEST(ex_0192, InvalidBounds)
{
  checkSlice({6, 2, 8, 4, 1}, -1, 3, 0);
  checkSlice({6, 2, 8, 4, 1}, -3, 0, 0);
  checkSlice({6, 2, 8, 4, 1}, 0, 6, 0);
  checkSlice({6, 2, 8, 4, 1}, 2, 10, 0);
  checkSlice({6, 2, 8, 4, 1}, 4, 1, 0);
  checkSlice({6, 2, 8, 4, 1}, 5, 4, 0);
  checkSlice({6, 2, 8, 4, 1}, 0, 5, 0);
}
