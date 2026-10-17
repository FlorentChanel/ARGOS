extern "C"
{
  #include "../../../Exercises/ex_0015_DaysInMonth/ex_0015_DaysInMonth.c"
}

#include <gtest/gtest.h>

#include <cstdio>
#include <string>

#include "Common/Utils.h"

TEST(ex_0015, DaysInMonth)
{
  // Feed the month numbers through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0015_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  ex_0015_DaysInMonth();
  ex_0015_DaysInMonth();
  ex_0015_DaysInMonth();
  ex_0015_DaysInMonth();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Please enter the number of the month (january=1, ... , december=12): Month 1 has 31 days.\n"
                  "Please enter the number of the month (january=1, ... , december=12): Month 12 has 31 days.\n"
                  "Please enter the number of the month (january=1, ... , december=12): "
                  "Please enter the number of the month (january=1, ... , december=12): "
                  "Month 7 has 31 days.\n"
                  "Please enter the number of the month (january=1, ... , december=12): "
                  "Please enter the number of the month (january=1, ... , december=12): "
                  "Please enter the number of the month (january=1, ... , december=12): "
                  "Please enter the number of the month (january=1, ... , december=12): Month 8 has 31 days.\n";

  auto msg = std::string("CHECK ex_0015_DaysInMonth() output!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}

TEST(ex_0015, AllMonths)
{
  ASSERT_NE(freopen("ex_0015_all_months_inputs.txt", "r", stdin), nullptr);

  const int expected_days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  std::string expected;
  testing::internal::CaptureStdout();
  for (int month = 1; month <= 12; ++month)
  {
    ex_0015_DaysInMonth();
    expected += "Please enter the number of the month (january=1, ... , december=12): Month " + std::to_string(month) +
                " has " + std::to_string(expected_days[month - 1]) + " days.\n";
  }

  auto actual = testing::internal::GetCapturedStdout();

  auto msg = std::string("CHECK ex_0015_DaysInMonth() output for months 1 to 12!");

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
