extern "C"
{
  #include "../../../Exercises/ex_0021_SumN/ex_0021_SumN.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0021, SumN)
{
  auto func_name = std::string("ex_0021_SumN");
  auto func_to_test = ex_0021_SumN;

  auto values_to_test = {std::make_tuple(10, 1, 55), std::make_tuple(1, 10, 55), std::make_tuple(1, 1, 1), std::make_tuple(1, 0, 1), std::make_tuple(0, 1, 1), std::make_tuple(0, 0, 0), std::make_tuple(1, 5, 15), std::make_tuple(5, 1, 15), std::make_tuple(1, 100, 5050), std::make_tuple(-3, 2, -3), std::make_tuple(2, -3, -3), std::make_tuple(-5, -1, -15), std::make_tuple(-1, -5, -15), std::make_tuple(-4, -4, -4), std::make_tuple(1, 10000, 50005000), std::make_tuple(10000, 1, 50005000), std::make_tuple(-10000, -1, -50005000), std::make_tuple(-1, -10000, -50005000), std::make_tuple(-10000, 10000, 0)};

  for (auto val : values_to_test)
  {
    Utils::unitTestResultWrapper(func_to_test, std::get<0>(val), std::get<1>(val), func_name, std::get<2>(val));
  }
}
