extern "C"
{
  #include "../../../Exercises/ex_0035_ResetPointer/ex_0035_ResetPointer.c"
}

#include <gtest/gtest.h>

#include <string>

#include "Common/Utils.h"

TEST(ex_0035, ResetPointerToScalar)
{
  auto values_to_test = {42, -7, 0};

  for (auto initial : values_to_test)
  {
    int x = initial;
    int *p = &x;
    ex_0035_ResetPointer(&p);

    std::string call = "ex_0035_ResetPointer(&p) with p = &x and x = " + std::to_string(initial);
    EXPECT_EQ(p, nullptr) << Utils::formatError(call + " did not set p to NULL");
    EXPECT_EQ(x, initial) << Utils::formatError(call + " modified x");
  }
}

TEST(ex_0035, ResetPointerToArrayElement)
{
  for (int index = 0; index < 3; index++)
  {
    int values[3] = {1, 2, 3};
    int *q = &values[index];
    ex_0035_ResetPointer(&q);

    std::string call = "ex_0035_ResetPointer(&q) with q = &values[" + std::to_string(index) + "] and values = {1, 2, 3}";
    EXPECT_EQ(q, nullptr) << Utils::formatError(call + " did not set q to NULL");
    EXPECT_EQ(values[0], 1) << Utils::formatError(call + " modified values[0]");
    EXPECT_EQ(values[1], 2) << Utils::formatError(call + " modified values[1]");
    EXPECT_EQ(values[2], 3) << Utils::formatError(call + " modified values[2]");
  }
}

TEST(ex_0035, NullAndNonNullPointers)
{
  int *r = NULL;
  ex_0035_ResetPointer(&r);
  EXPECT_EQ(r, nullptr) << Utils::formatError("ex_0035_ResetPointer(&r) with r = NULL did not leave r NULL");

  int y = 5;
  int *s = &y;
  ex_0035_ResetPointer(&s);
  EXPECT_EQ(s, nullptr) << Utils::formatError("ex_0035_ResetPointer(&s) with s = &y and y = 5 did not set s to NULL");
  EXPECT_EQ(y, 5) << Utils::formatError("ex_0035_ResetPointer(&s) with s = &y and y = 5 modified y");
}
