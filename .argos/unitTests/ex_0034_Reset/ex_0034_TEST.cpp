extern "C"
{
  #include "../../../Exercises/ex_0034_Reset/ex_0034_Reset.c"
}

#include <gtest/gtest.h>

#include <string>

#include "Common/Utils.h"

TEST(ex_0034, Reset)
{
  auto values_to_test = {42, -7, 0, 1, -1, 2147483647, -2147483647 - 1};

  for (auto initial : values_to_test)
  {
    int value = initial;
    ex_0034_Reset(&value);

    std::string call = "ex_0034_Reset(&value) with value = " + std::to_string(initial);
    EXPECT_EQ(value, 0) << Utils::formatError(call + " did not set value to 0");
  }
}
