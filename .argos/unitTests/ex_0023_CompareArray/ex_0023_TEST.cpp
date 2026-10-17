extern "C"
{
  #include "../../../Exercises/ex_0023_CompareArray/ex_0023_CompareArray.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0023, CompareArray)
{
  int array1[] = {1, 2, 3, 4, 4};
  int array2[] = {1, 2, 3, 4, 5};

  auto values_to_test = {std::make_tuple(array1, array2, 0, true), std::make_tuple(array1, array2, 4, true), std::make_tuple(array1, array2, 5, false)};

  for (auto val : values_to_test)
  {
    auto arr1 = std::get<0>(val);
    auto arr2 = std::get<1>(val);
    auto nb_vals = std::get<2>(val);
    auto expected_result = std::get<3>(val);

    Utils::unitTestStatusWrapper(ex_0023_CompareArray, arr1, arr2, nb_vals, "ex_0023_CompareArray", expected_result);
  }
}

TEST(ex_0023, MismatchPosition)
{
  int reference[] = {1, 2, 3};
  int first_differs[] = {9, 2, 3};
  int middle_differs[] = {1, 9, 3};
  int five[] = {5};
  int other_five[] = {5};
  int six[] = {6};

  auto values_to_test = {std::make_tuple(first_differs, reference, 3, false), std::make_tuple(middle_differs, reference, 3, false), std::make_tuple(five, other_five, 1, true), std::make_tuple(five, six, 1, false)};

  for (auto val : values_to_test)
  {
    auto arr1 = std::get<0>(val);
    auto arr2 = std::get<1>(val);
    auto nb_vals = std::get<2>(val);
    auto expected_result = std::get<3>(val);

    Utils::unitTestStatusWrapper(ex_0023_CompareArray, arr1, arr2, nb_vals, "ex_0023_CompareArray", expected_result);
  }
}
