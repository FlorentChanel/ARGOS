extern "C"
{
  #include "../../../Exercises/ex_0031_Person/ex_0031_Person.c"
}

#include <gtest/gtest.h>

#include "Common/Utils.h"

TEST(ex_0031, Person)
{
  testing::internal::CaptureStdout();
  ex_0031_Person();

  auto actual = testing::internal::GetCapturedStdout();
  auto expected = "7 Persons\n"
                  "Persons less than 80 years old:\n"
                  "Brian Kernighan 78 years\n"
                  "Dennis Ritchie 79 years\n"
                  "Ken Thompson 77 years\n"
                  "Bjarne Stroustrup 70 years\n\n"
                  "Alphabetic order:\n"
                  "The first is: Dijkstra\n"
                  "The last is: Thompson\n";

  EXPECT_EQ(expected, actual) << Utils::formatError("CHECK ex_0031_Person() output!");
}
