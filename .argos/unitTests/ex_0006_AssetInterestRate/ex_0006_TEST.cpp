extern "C"
{
  #include "../../../Exercises/ex_0006_AssetInterestRate/ex_0006_AssetInterestRate.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0006, AssetInterestRate)
{
  auto func_name = std::string("ex_0006_AssetInterestRate");
  auto func_to_test = ex_0006_AssetInterestRate;

  auto values_to_test = {
      std::make_tuple(1000.0, 2.5, 30, 2097.5675790817859),
      std::make_tuple(1000.0, 2.5, 0, 1000.0),
      std::make_tuple(1000.0, 0.0, 30, 1000.0),
      std::make_tuple(0.0, 5.0, 10, 0.0),
      std::make_tuple(1000.0, 2.5, 1, 1025.0),
  };

  for (auto val : values_to_test)
  {
    Utils::unitTestResultWrapper(func_to_test, std::get<0>(val), std::get<1>(val), std::get<2>(val), func_name, std::get<3>(val));
  }
}
