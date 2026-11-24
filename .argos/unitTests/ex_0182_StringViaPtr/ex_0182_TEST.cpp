extern "C"
{
  #include "../../../Exercises/ex_0182_StringViaPtr/ex_0182_StringViaPtr.c"
}

#include <gtest/gtest.h>

#include <string>
#include <tuple>

#include "Common/Utils.h"

TEST(ex_0182, ReadmeExamples)
{
  auto values_to_test = {std::make_tuple("hello", "\"hello\"", 5), std::make_tuple("", "\"\"", 0), std::make_tuple("a b c", "\"a b c\"", 5), std::make_tuple("C\n", "\"C\\n\"", 2)};

  for (auto val : values_to_test)
  {
    auto text = std::get<0>(val);
    std::string shown = std::get<1>(val);
    auto expected = std::get<2>(val);

    int result = ex_0182_StringViaPtr(text);

    EXPECT_EQ(result, expected) << Utils::formatError("ex_0182_StringViaPtr(" + shown + ") returned " + std::to_string(result) + ", expected " + std::to_string(expected));
  }
}

TEST(ex_0182, OtherStrings)
{
  auto values_to_test = {std::make_tuple("x", "\"x\"", 1), std::make_tuple("Pointers walk strings", "\"Pointers walk strings\"", 21), std::make_tuple("123-456!", "\"123-456!\"", 8), std::make_tuple("\t \t", "\"\\t \\t\"", 3), std::make_tuple("abcdefghijklmnopqrstuvwxyz0123456789", "\"abcdefghijklmnopqrstuvwxyz0123456789\"", 36)};

  for (auto val : values_to_test)
  {
    auto text = std::get<0>(val);
    std::string shown = std::get<1>(val);
    auto expected = std::get<2>(val);

    int result = ex_0182_StringViaPtr(text);

    EXPECT_EQ(result, expected) << Utils::formatError("ex_0182_StringViaPtr(" + shown + ") returned " + std::to_string(result) + ", expected " + std::to_string(expected));
  }
}

TEST(ex_0182, PointerInsideString)
{
  const char sentence[] = "walking pointer";

  auto values_to_test = {std::make_tuple(0, 15), std::make_tuple(8, 7), std::make_tuple(14, 1), std::make_tuple(15, 0)};

  for (auto val : values_to_test)
  {
    auto offset = std::get<0>(val);
    auto expected = std::get<1>(val);

    int result = ex_0182_StringViaPtr(sentence + offset);

    EXPECT_EQ(result, expected) << Utils::formatError("ex_0182_StringViaPtr(sentence + " + std::to_string(offset) + ") with sentence = \"walking pointer\" returned " + std::to_string(result) + ", expected " + std::to_string(expected));
  }
}
