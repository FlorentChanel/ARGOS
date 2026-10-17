extern "C"
{
  #include "../../../Exercises/ex_0025_FillArray/ex_0025_FillArray.c"
}

#include <gtest/gtest.h>

#include <cstdio>
#include <string>
#include <tuple>

#include "Common/Utils.h"

TEST(ex_0025, FillArray)
{
  const int array_size = 4;

  // Redirected before the bound cases, so a stray read consumes fixture lines and the next cases fail
  ASSERT_NE(freopen("ex_0025_inputs.txt", "r", stdin), nullptr);

  int unchanged[] = {-2, -2, -2, -2};
  int array_result_1[] = {1, -2, -2, -2};
  int array_result_2[] = {2, 2, -2, -2};
  int array_result_3[] = {3, 3, -2, -2};
  int array_result_4[] = {0, 4, -2, -2};
  int array_result_5[] = {5, 6, -2, -2};
  int array_result_6[] = {7, -2, -2, -2};
  int array_result_7[] = {8, 9, -2, -2};

  auto values_to_test = {
    std::make_tuple(-1, 0, unchanged),
    std::make_tuple(0, 0, unchanged),
    std::make_tuple(4, 1, array_result_1),
    std::make_tuple(4, 2, array_result_2),
    std::make_tuple(4, 2, array_result_3),
    std::make_tuple(4, 2, array_result_4),
    std::make_tuple(2, 2, array_result_5),
    std::make_tuple(4, 1, array_result_6),
    std::make_tuple(4, 2, array_result_7)};

  for (auto val : values_to_test)
  {
    auto max_capacity = std::get<0>(val);
    auto expected_count = std::get<1>(val);
    auto expected_array = std::get<2>(val);

    int array[] = {-2, -2, -2, -2};
    int count = ex_0025_FillArray(array, max_capacity);

    std::string call = "ex_0025_FillArray(array, " + std::to_string(max_capacity) + ")";
    EXPECT_EQ(count, expected_count) << Utils::formatError(call + " returned a wrong count");
    for (int i = 0; i < array_size; ++i)
    {
      EXPECT_EQ(array[i], expected_array[i])
        << Utils::formatError(call + " left a wrong value at index " + std::to_string(i));
    }
  }
}
