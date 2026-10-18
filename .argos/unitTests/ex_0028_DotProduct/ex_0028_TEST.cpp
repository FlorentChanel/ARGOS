extern "C"
{
  #include "../../../Exercises/ex_0028_DotProduct/ex_0028_DotProduct.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0028, DotProduct)
{
  int X[] = {1, 0, 0};
  int Y[] = {0, 1, 0};
  int Z[] = {0, 0, 1};

  int A[] = {3, 2, -4};
  int B[] = {2, -3, 5};

  int C[] = {7};
  int D[] = {-3};

  int E[] = {1, -2, 3, 0, 4};
  int F[] = {5, 6, -1, 9, 2};

  auto values_to_test = {std::make_tuple(X, Y, 3, 0), std::make_tuple(X, Z, 3, 0), std::make_tuple(Y, Z, 3, 0), std::make_tuple(X, X, 3, 1), std::make_tuple(Y, Y, 3, 1), std::make_tuple(Z, Z, 3, 1), std::make_tuple(A, B, 3, -20), std::make_tuple(C, D, 1, -21), std::make_tuple(E, F, 5, -2)};

  for (auto val : values_to_test)
  {
    auto x = std::get<0>(val);
    auto y = std::get<1>(val);
    auto n = std::get<2>(val);
    auto expected_result = std::get<3>(val);

    Utils::unitTestStatusWrapper(ex_0028_DotProduct, x, y, n, "ex_0028_DotProduct", expected_result);
  }
}
