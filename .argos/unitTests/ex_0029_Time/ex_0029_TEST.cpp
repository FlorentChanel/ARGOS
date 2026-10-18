extern "C"
{
  #include "../../../Exercises/ex_0029_Time/ex_0029_Time.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

static void checkInitTime(int h, int m, int s)
{
  Time t = ex_0029_InitTime(h, m, s);

  EXPECT_EQ(h, (int)t.hh) << Utils::formatError("CHECK ex_0029_InitTime(" + std::to_string(h) + ", " + std::to_string(m) + ", " + std::to_string(s) + ").hh!");
  EXPECT_EQ(m, (int)t.mm) << Utils::formatError("CHECK ex_0029_InitTime(" + std::to_string(h) + ", " + std::to_string(m) + ", " + std::to_string(s) + ").mm!");
  EXPECT_EQ(s, (int)t.ss) << Utils::formatError("CHECK ex_0029_InitTime(" + std::to_string(h) + ", " + std::to_string(m) + ", " + std::to_string(s) + ").ss!");
}

static void checkPrintTime(int h, int m, int s, const std::string& expected)
{
  Time t;
  t.hh = h;
  t.mm = m;
  t.ss = s;

  testing::internal::CaptureStdout();
  ex_0029_PrintTime(t);
  auto actual = testing::internal::GetCapturedStdout();

  EXPECT_EQ(expected, actual) << Utils::formatError("CHECK ex_0029_PrintTime() output for " + expected.substr(0, expected.size() - 1) + "!");
}

TEST(ex_0029, InitTime)
{
  checkInitTime(5, 3, 17);
  checkInitTime(0, 0, 0);
  checkInitTime(99, 59, 59);
  checkInitTime(12, 34, 56);
}

TEST(ex_0029, PrintTime)
{
  checkPrintTime(5, 3, 17, "05:03:17\n");
  checkPrintTime(0, 0, 0, "00:00:00\n");
  checkPrintTime(99, 59, 59, "99:59:59\n");
  checkPrintTime(10, 20, 30, "10:20:30\n");
}

TEST(ex_0029, Time)
{
  testing::internal::CaptureStdout();
  ex_0029_Time();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "05:03:17\n";

  EXPECT_EQ(expected, actual) << Utils::formatError("CHECK ex_0029_Time() output!");
}
