extern "C"
{
  #include "../../../Exercises/ex_0003_SomeCalculus/ex_0003_SomeCalculus.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0003, SomeCalculus)
{
  testing::internal::CaptureStdout();
  ex_0003_SomeCalculus(4, 7);

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "\n a) 4.000000 power 7.000000 = 16384 \n\n"
                  " b) The hypotenuse of the right triangle is 8.062258 \n\n"
                  " c) The tangent of A is 0.069927 \n\n"
                  " d) The rounded down value of A/B is 0.000000 \n\n"
                  " e) The rounded down value of A/B with 3 decimals is 0.571000 \n\n";

  auto msg = std::string("CHECK ex_0003_SomeCalculus() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);

  testing::internal::CaptureStdout();
  ex_0003_SomeCalculus(-7, 3);

  actual = testing::internal::GetCapturedStdout();
  expected = "\n a) -7.000000 power 3.000000 = -343 \n\n"
             " b) The hypotenuse of the right triangle is 7.615773 \n\n"
             " c) The tangent of A is -0.122785 \n\n"
             " d) The rounded down value of A/B is -3.000000 \n\n"
             " e) The rounded down value of A/B with 3 decimals is -2.334000 \n\n";

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
