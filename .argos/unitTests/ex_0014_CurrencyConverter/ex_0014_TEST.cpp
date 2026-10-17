extern "C"
{
  #include "../../../Exercises/ex_0014_CurrencyConverter/ex_0014_CurrencyConverter.c"
}

#include <gtest/gtest.h>

#include <cstdio>

#include "Common/Utils.h"

TEST(ex_0014, CurrencyConverter)
{
  // Feed the amounts through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0014_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0014_CurrencyConverter();
  ex_0014_CurrencyConverter();
  ex_0014_CurrencyConverter();
  ex_0014_CurrencyConverter();
  ex_0014_CurrencyConverter();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Swiss francs: 0.086\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Swiss francs: 121.770\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: The input amount is negative!!\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Swiss francs: 0.824\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Unsupported currency!!\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Swiss francs: 138.990\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: The input format is not correct!!\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Swiss francs: 0.085\n";

  auto msg = std::string("CHECK ex_0014_CurrencyConverter() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}

TEST(ex_0014, EdgeCases)
{
  ASSERT_NE(freopen("ex_0014_edge_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0014_CurrencyConverter();
  ex_0014_CurrencyConverter();
  ex_0014_CurrencyConverter();
  ex_0014_CurrencyConverter();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Unsupported currency!!\n"
                  "The input amount is negative!!\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Swiss francs: 0.007\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Unsupported currency!!\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Swiss francs: 0.670\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Unsupported currency!!\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Swiss francs: 113.000\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Unsupported currency!!\n"
                  "USAGE: non-negative value [W | $ | Y | P]\n"
                  "Won = W  Dollar = $  Yen = Y  Pound = P\n"
                  "Please enter the amount to convert: Swiss francs: 0.000\n";

  auto msg = std::string("CHECK ex_0014_CurrencyConverter() edge cases output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
