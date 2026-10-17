extern "C"
{
  #include "../../../Exercises/ex_0019_MultiplicationTable/ex_0019_MultiplicationTable.c"
}

#include <gtest/gtest.h>

#include <cstdio>

#include "Common/Utils.h"

TEST(ex_0019, Read)
{
  // Feed the numbers through stdin (fixture shipped next to the binary).
  ASSERT_NE(freopen("ex_0019_inputs.txt", "r", stdin), nullptr);

  testing::internal::CaptureStdout();
  auto number = ex_0019_Read(1, 12);

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "Please enter the multiplication table (in [1..12]): "
                  "Please enter the multiplication table (in [1..12]): "
                  "Please enter the multiplication table (in [1..12]): "
                  "Please enter the multiplication table (in [1..12]): ";

  auto msg = std::string("CHECK ex_0019_Read() output!");
  EXPECT_EQ(expected, actual) << Utils::formatError(msg);

  auto msg_result = std::string("ex_0019_Read(1, 12) should return 5");
  EXPECT_EQ(5, number) << Utils::formatError(msg_result);

  testing::internal::CaptureStdout();
  number = ex_0019_Read(3, 8);

  actual = testing::internal::GetCapturedStdout();
  expected = "Please enter the multiplication table (in [3..8]): "
             "Please enter the multiplication table (in [3..8]): "
             "Please enter the multiplication table (in [3..8]): ";

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);

  msg_result = std::string("ex_0019_Read(3, 8) should return 8");
  EXPECT_EQ(8, number) << Utils::formatError(msg_result);

  testing::internal::CaptureStdout();
  number = ex_0019_Read(3, 8);

  actual = testing::internal::GetCapturedStdout();
  expected = "Please enter the multiplication table (in [3..8]): ";

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);

  msg_result = std::string("ex_0019_Read(3, 8) should return 3");
  EXPECT_EQ(3, number) << Utils::formatError(msg_result);
}

TEST(ex_0019, MultiplicationTable)
{
  testing::internal::CaptureStdout();
  ex_0019_MultiplicationTable(5);

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "\nMULTIPLICATION TABLE FOR 5\n"
                  "5 X 1 = 5\n"
                  "5 X 2 = 10\n"
                  "5 X 3 = 15\n"
                  "5 X 4 = 20\n"
                  "5 X 5 = 25\n"
                  "5 X 6 = 30\n"
                  "5 X 7 = 35\n"
                  "5 X 8 = 40\n"
                  "5 X 9 = 45\n"
                  "5 X 10 = 50\n";

  auto msg = std::string("CHECK ex_0019_MultiplicationTable() output!");
  EXPECT_EQ(expected, actual) << Utils::formatError(msg);

  testing::internal::CaptureStdout();
  ex_0019_MultiplicationTable(1);

  actual = testing::internal::GetCapturedStdout();
  expected = "\nMULTIPLICATION TABLE FOR 1\n"
             "1 X 1 = 1\n"
             "1 X 2 = 2\n"
             "1 X 3 = 3\n"
             "1 X 4 = 4\n"
             "1 X 5 = 5\n"
             "1 X 6 = 6\n"
             "1 X 7 = 7\n"
             "1 X 8 = 8\n"
             "1 X 9 = 9\n"
             "1 X 10 = 10\n";

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);

  testing::internal::CaptureStdout();
  ex_0019_MultiplicationTable(12);

  actual = testing::internal::GetCapturedStdout();
  expected = "\nMULTIPLICATION TABLE FOR 12\n"
             "12 X 1 = 12\n"
             "12 X 2 = 24\n"
             "12 X 3 = 36\n"
             "12 X 4 = 48\n"
             "12 X 5 = 60\n"
             "12 X 6 = 72\n"
             "12 X 7 = 84\n"
             "12 X 8 = 96\n"
             "12 X 9 = 108\n"
             "12 X 10 = 120\n";

  EXPECT_EQ(expected, actual) << Utils::formatError(msg);
}
