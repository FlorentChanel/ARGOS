extern "C"
{
  #include "../../../Exercises/ex_0020_Calculator/ex_0020_Calculator.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0020, Operations)
{
  auto func_name = std::string("ex_0020_Calculator");
  auto func_to_test = ex_0020_Calculator;

  auto values_to_test = {
      std::make_tuple(1.0, 2.0, '+', 3.0),
      std::make_tuple(1.0, 2.0, '-', -1.0),
      std::make_tuple(1.1, 9.9, '*', 10.89),
      std::make_tuple(1.0, 2.0, '/', 0.5),
      std::make_tuple(-2.5, 4.0, '+', 1.5),
      std::make_tuple(3.0, 7.5, '-', -4.5),
      std::make_tuple(-3.0, 4.0, '*', -12.0),
      std::make_tuple(9.0, -4.0, '/', -2.25),
  };

  for (auto val : values_to_test)
  {
    Utils::unitTestResultWrapper(func_to_test, std::get<0>(val), std::get<1>(val), std::get<2>(val), func_name, std::get<3>(val));
  }
}

TEST(ex_0020, DivisionByZero)
{
  auto func_name = std::string("ex_0020_Calculator");
  auto func_to_test = ex_0020_Calculator;

  auto values_to_test = {
      std::make_tuple(1.0, 0.0, '/', 0.0),
      std::make_tuple(-7.5, 0.0, '/', 0.0),
      std::make_tuple(7.5, 2.5, '/', 3.0),
  };

  for (auto val : values_to_test)
  {
    Utils::unitTestResultWrapper(func_to_test, std::get<0>(val), std::get<1>(val), std::get<2>(val), func_name, std::get<3>(val));
  }
}

TEST(ex_0020, UnknownOperator)
{
  auto func_name = std::string("ex_0020_Calculator");
  auto func_to_test = ex_0020_Calculator;

  auto values_to_test = {
      std::make_tuple(1.0, 2.0, 'z', 0.0),
      std::make_tuple(5.0, 3.0, '%', 0.0),
      std::make_tuple(5.0, 3.0, 'x', 0.0),
      std::make_tuple(5.0, 3.0, '*', 15.0),
  };

  for (auto val : values_to_test)
  {
    Utils::unitTestResultWrapper(func_to_test, std::get<0>(val), std::get<1>(val), std::get<2>(val), func_name, std::get<3>(val));
  }
}
