extern "C"
{
  #include "../../../Exercises/ex_0184_DerefModify/ex_0184_DerefModify.c"
}

#include <gtest/gtest.h>

#include <string>
#include <tuple>

#include "Common/Utils.h"

TEST(ex_0184, AddDelta)
{
  auto values_to_test = {std::make_tuple(10, 5, 15), std::make_tuple(3, -8, -5), std::make_tuple(-4, 0, -4), std::make_tuple(0, 7, 7), std::make_tuple(-20, 12, -8), std::make_tuple(100, -100, 0)};

  for (auto val : values_to_test)
  {
    auto initial = std::get<0>(val);
    auto delta = std::get<1>(val);
    auto expected = std::get<2>(val);

    int value = initial;
    ex_0184_DerefModify(&value, delta);

    std::string call = "ex_0184_DerefModify(&value, " + std::to_string(delta) + ") with value = " + std::to_string(initial);
    EXPECT_EQ(value, expected) << Utils::formatError(call + ": value is " + std::to_string(value) + ", expected " + std::to_string(expected));
  }
}

TEST(ex_0184, RepeatedCalls)
{
  auto values_to_test = {std::make_tuple(1, 2, 2, 5), std::make_tuple(4, 3, -3, 4), std::make_tuple(-6, -1, -1, -8)};

  for (auto val : values_to_test)
  {
    auto initial = std::get<0>(val);
    auto first_delta = std::get<1>(val);
    auto second_delta = std::get<2>(val);
    auto expected = std::get<3>(val);

    int value = initial;
    ex_0184_DerefModify(&value, first_delta);
    ex_0184_DerefModify(&value, second_delta);

    std::string call = "ex_0184_DerefModify(&value, " + std::to_string(first_delta) + ") then ex_0184_DerefModify(&value, " + std::to_string(second_delta) + ") with value = " + std::to_string(initial);
    EXPECT_EQ(value, expected) << Utils::formatError(call + ": value is " + std::to_string(value) + ", expected " + std::to_string(expected));
  }
}
