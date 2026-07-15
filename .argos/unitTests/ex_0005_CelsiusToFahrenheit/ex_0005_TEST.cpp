extern "C"
{
  #include "../../../Exercises/ex_0005_CelsiusToFahrenheit/ex_0005_CelsiusToFahrenheit.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0005, CelsiusToFahrenheit)
{
  auto func_name = std::string("ex_0005_CelsiusToFahrenheit");
  auto func_to_test = ex_0005_CelsiusToFahrenheit;

  auto values_to_test = {
      std::make_tuple(0.0, 32.0),
      std::make_tuple(100.0, 212.0),
      std::make_tuple(-40.0, -40.0),
      std::make_tuple(37.5, 99.5),
  };

  for (auto val : values_to_test)
  {
    Utils::unitTestResultWrapper(func_to_test, std::get<0>(val), func_name, std::get<1>(val));
  }
}
