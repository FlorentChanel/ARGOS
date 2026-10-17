extern "C"
{
  #include "../../../Exercises/ex_0016_SumProductMean/ex_0016_SumProductMean.c"
}

#include <gtest/gtest.h>

#include <cstdio>

#include "Common/Utils.h"

TEST(ex_0016, SumProductMean)
{
  // Feed N and the values through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0016_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0016_SumProductMean();
  ex_0016_SumProductMean();
  ex_0016_SumProductMean();
  ex_0016_SumProductMean();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Number of values to read: "
                  "Number of values to read: "
                  "Number of values to read: "
                  "Number of values to read: 1. number: 1. number: 2. number: 2. number: 3. number: 3. number: Sum = 6\n"
                  "Product = 6\n"
                  "Mean = 2.0000\n"
                  "Number of values to read: "
                  "Number of values to read: 1. number: 2. number: Sum = 1\n"
                  "Product = -12\n"
                  "Mean = 0.5000\n"
                  "Number of values to read: 1. number: Sum = -4\n"
                  "Product = -4\n"
                  "Mean = -4.0000\n"
                  "Number of values to read: "
                  "1. number: 2. number: 3. number: 4. number: 5. number: "
                  "6. number: 7. number: 8. number: 9. number: 10. number: "
                  "11. number: 12. number: 13. number: 14. number: 15. number: Sum = 9\n"
                  "Product = 0\n"
                  "Mean = 0.6000\n";

  auto msg = std::string("CHECK ex_0016_SumProductMean() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
