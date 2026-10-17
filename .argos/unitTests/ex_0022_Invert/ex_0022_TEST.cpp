extern "C"
{
  #include "../../../Exercises/ex_0022_Invert/ex_0022_Invert.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0022, Invert)
{
  auto func_name = std::string("ex_0022_Invert");
  auto func_to_test = ex_0022_Invert;

  auto values_to_test = {std::make_tuple(123, 321), std::make_tuple(0, 0), std::make_tuple(1, 1), std::make_tuple(123456789, 987654321), std::make_tuple(-123, -1), std::make_tuple(1234, 4321), std::make_tuple(1200, 21), std::make_tuple(10, 1), std::make_tuple(-12, -1)};

  for (auto val : values_to_test)
  {
    Utils::unitTestResultWrapper(func_to_test, std::get<0>(val), func_name, std::get<1>(val));
  }
}
