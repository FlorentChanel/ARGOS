extern "C"
{
  #include "../../../Exercises/ex_0018_Squares/ex_0018_Squares.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0018, Square)
{
  auto func_name = std::string("ex_0018_Square");
  auto func_to_test = ex_0018_Square;

  Utils::unitTestResultWrapper(func_to_test, 0, func_name, 0);
  Utils::unitTestResultWrapper(func_to_test, 1, func_name, 1);
  Utils::unitTestResultWrapper(func_to_test, 3, func_name, 9);
  Utils::unitTestResultWrapper(func_to_test, -4, func_name, 16);
  Utils::unitTestResultWrapper(func_to_test, 12, func_name, 144);
}

TEST(ex_0018, Squares)
{
  auto func_name = std::string("ex_0018_Squares");
  auto func_to_test = ex_0018_Squares;

  auto errors_to_test = {-1, 0, 1001};
  for (auto err : errors_to_test)
  {
    Utils::unitTestStatusWrapper(func_to_test, err, func_name, false);
    Utils::unitTestOutputWrapper(func_to_test, err, func_name, "");
  }

  auto valid_values = {1, 5, 1000};
  for (auto value : valid_values)
  {
    testing::internal::CaptureStdout();
    auto status = func_to_test(value);
    testing::internal::GetCapturedStdout();
    EXPECT_TRUE(status) << Utils::formatError(func_name + "(" + std::to_string(value) + ") should return true");
  }

  auto values_to_test = {1, 2, 3, 4, 5};
  auto expected_outputs = {"1 \n", "1 4 \n", "1 4 9 \n", "1 4 9 16 \n", "1 4 9 16 25 \n"};

  for (auto ITs = std::make_pair(values_to_test.begin(), expected_outputs.begin());
       ITs.first != values_to_test.end() && ITs.second != expected_outputs.end();
       ++ITs.first, ++ITs.second)
  {
    Utils::unitTestOutputWrapper(func_to_test, (*ITs.first), func_name, (*ITs.second));
  }

  auto expected_upper_bound = std::string();
  for (int i = 1; i <= 1000; ++i)
  {
    expected_upper_bound += std::to_string(i * i) + " ";
  }
  expected_upper_bound += "\n";
  Utils::unitTestOutputWrapper(func_to_test, 1000, func_name, expected_upper_bound);
}
