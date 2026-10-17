extern "C"
{
  #include "../../../Exercises/ex_0024_PrintArray/ex_0024_PrintArray.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0024, PrintArray)
{
  int array[] = {1, 2, 3, 4, 5};

  auto values_to_test = {std::make_tuple(array, 0, ""), std::make_tuple(array, 4, "1 2 3 4"), std::make_tuple(array, 5, "1 2 3 4 5")};

  for (auto val : values_to_test)
  {
    auto arr = std::get<0>(val);
    auto nb_vals = std::get<1>(val);
    auto expected_output = std::get<2>(val);

    Utils::unitTestOutputWrapper(ex_0024_PrintArray, arr, nb_vals, "ex_0024_PrintArray", expected_output);
  }
}

TEST(ex_0024, PrintArrayOtherValues)
{
  int array[] = {-7, 0, 42};

  auto values_to_test = {std::make_tuple(array, 1, "-7"), std::make_tuple(array, 3, "-7 0 42")};

  for (auto val : values_to_test)
  {
    auto arr = std::get<0>(val);
    auto nb_vals = std::get<1>(val);
    auto expected_output = std::get<2>(val);

    Utils::unitTestOutputWrapper(ex_0024_PrintArray, arr, nb_vals, "ex_0024_PrintArray", expected_output);
  }
}
