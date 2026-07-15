#include "Common/Utils.h"

// Mute/unmute program output when stating status
void Utils::muteStdout()
{
  std::cout.setstate(std::ios_base::failbit);
  // On Unix and Unix-like systems:
  freopen("/dev/null", "w", stdout);
  // On Windows:
  freopen("NUL", "w", stdout);
}

void Utils::unmuteStdout()
{
  std::cout.clear();
  // On Unix and Unix-like systems:
  freopen("/dev/tty", "w", stdout);
  // On Windows:
  freopen("CON", "w", stdout);
}

std::string Utils::asString(int array[], int nb_vals)
{
  // Array is empty
  if (nb_vals <= 0)
  {
    return "{}";
  }

  std::ostringstream oss;
  oss << "{";
  // Handle special case for last element
  for (int i = 0; i < nb_vals-1; ++i)
  {
    oss << array[i] << ", ";
  }
  oss << array[nb_vals-1] << "}";
  return oss.str();
}

// Custom error output
std::string Utils::formatError(const std::string &msg)
{
  // ANSI Colors are in the form "\033[color1;color2;...m"
  // where \033 is the escape character, m is the end of the command
  const auto colorCode = std::string("\033[1;37;41m");
  const auto resetColorCode = std::string("\033[0m");
  const auto msgHeader = std::string("\n\t");
  const auto msgTail = std::string("\n");
  return msgHeader + colorCode + msg + resetColorCode + msgTail;
}

bool Utils::expectEQ(int expected_array[], int actual_array[], int nb_vals)
{
  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss <<  asString(actual_array, nb_vals) << " should be " << asString(expected_array, nb_vals);
    msg = oss.str();
  }

  auto std_actual = std::vector<int>(actual_array, actual_array + nb_vals);
  auto std_expected = std::vector<int>(expected_array, expected_array + nb_vals);
  auto equal = std::equal(std_actual.begin(), std_actual.end(), std_expected.begin());

  EXPECT_TRUE(equal) << formatError(msg);

  return equal;
}

// Simple decorator for custom unit testing
bool Utils::unitTestStatusWrapper(bool (*func)(int), int arg, const std::string &func_name, bool expected_status)
{
  auto actual_status = func(arg);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arg << ") should return " << std::boolalpha << expected_status;
    msg = oss.str();
  }

  EXPECT_EQ(expected_status, actual_status) << formatError(msg);

  return expected_status == actual_status; // Just in case
}

bool Utils::unitTestStatusWrapper(int (*func)(int[], int), int arr[], int arg, const std::string &func_name, int expected_result)
{
  auto actual_result = func(arr, arg);

  auto arrStr = asString(arr, arg);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arrStr << ", " << arg << ") should return " << expected_result;
    msg = oss.str();
  }

  EXPECT_EQ(expected_result, actual_result) << formatError(msg);

  return expected_result == actual_result; // Just in case
}

bool Utils::unitTestStatusWrapper(bool (*func)(int[], int[], int), int arr1[], int arr2[], int arg3, const std::string &func_name, bool expected_result)
{
  auto actual_status = func(arr1, arr2, arg3);

  auto arrStr1 = asString(arr1, arg3);
  auto arrStr2 = asString(arr2, arg3);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arrStr1 << ", " << arrStr2 << ", " << arg3 << ") should return " << std::boolalpha << expected_result;
    msg = oss.str();
  }

  EXPECT_EQ(expected_result, actual_status) << formatError(msg);

  return expected_result == actual_status; // Just in case
}

bool Utils::unitTestStatusWrapper(int (*func)(int[], int[], int), int arr1[], int arr2[], int arg3, const std::string &func_name, int expected_result)
{
  auto actual_status = func(arr1, arr2, arg3);

  auto arrStr1 = asString(arr1, arg3);
  auto arrStr2 = asString(arr2, arg3);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arrStr1 << ", " << arrStr2 << ", " << arg3 << ") should return " << expected_result;
    msg = oss.str();
  }

  EXPECT_EQ(expected_result, actual_status) << formatError(msg);

  return expected_result == actual_status; // Just in case
}

bool Utils::unitTestOutputWrapper(bool (*func)(int), int arg, const std::string &func_name, const std::string &expected_output)
{
  testing::internal::CaptureStdout();

  func(arg);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arg << ") should output " << expected_output;
    msg = oss.str();
  }

  auto actual_output = testing::internal::GetCapturedStdout();
  EXPECT_EQ(expected_output, actual_output) << formatError(msg);

  return expected_output == actual_output; // Just in case
}

bool Utils::unitTestOutputWrapper(void (*func)(int[], int), int array[], int arg, const std::string &func_name, const std::string &expected_output)
{
  testing::internal::CaptureStdout();

  func(array, arg);

  auto arrayStr = asString(array, arg);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arrayStr << ", " << arg << ") should output " << expected_output;
    msg = oss.str();
  }

  auto actual_output = testing::internal::GetCapturedStdout();
  EXPECT_EQ(expected_output, actual_output) << formatError(msg);

  return expected_output == actual_output; // Just in case
}

bool Utils::unitTestResultWrapper(int (*func)(int), int arg, const std::string &func_name, int expected_result)
{
  auto actual_result = func(arg);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arg << ") should return " << expected_result;
    msg = oss.str();
  }

  EXPECT_EQ(expected_result, actual_result) << formatError(msg);

  return expected_result == actual_result; // Just in case
}

bool Utils::unitTestResultWrapper(int (*func)(int, int), int arg1, int arg2, const std::string &func_name, int expected_result)
{
  auto actual_result = func(arg1, arg2);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arg1 << ", " << arg2 << ") should return " << expected_result;
    msg = oss.str();
  }

  EXPECT_EQ(expected_result, actual_result) << formatError(msg);

  return expected_result == actual_result; // Just in case
}

bool Utils::unitTestResultWrapper(double (*func)(double), int arg, const std::string &func_name, double expected_result)
{
  auto actual_result = func(arg);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arg << ") should return " << expected_result;
    msg = oss.str();
  }

  double epsilon = 0.0000001;
  EXPECT_NEAR(expected_result, actual_result, epsilon) << formatError(msg);

  return expected_result == actual_result; // Just in case
}

bool Utils::unitTestResultWrapper(double (*func)(double), double arg, const std::string &func_name, double expected_result)
{
  auto actual_result = func(arg);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arg << ") should return " << expected_result;
    msg = oss.str();
  }

  double epsilon = 0.0000001;
  EXPECT_NEAR(expected_result, actual_result, epsilon) << formatError(msg);

  return expected_result == actual_result; // Just in case
}

bool Utils::unitTestResultWrapper(double (*func)(double, double, double), double arg1, double arg2, double arg3, const std::string &func_name, double expected_result)
{
  auto actual_result = func(arg1, arg2, arg3);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arg1 << ", " << arg2 << ", " << arg3 << ") should return " << expected_result;
    msg = oss.str();
  }

  double epsilon = 0.0000001;
  EXPECT_NEAR(expected_result, actual_result, epsilon) << formatError(msg);

  return expected_result == actual_result; // Just in case
}

bool Utils::unitTestResultWrapper(double (*func)(double, double, char), double arg1, double arg2, char arg3, const std::string &func_name, double expected_result)
{
  auto actual_result = func(arg1, arg2, arg3);

  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(" << arg1 << ", " << arg2 << ", " << arg3 << ") should return " << expected_result;
    msg = oss.str();
  }

  double epsilon = 0.0000001;
  EXPECT_NEAR(expected_result, actual_result, epsilon) << formatError(msg);

  return expected_result == actual_result; // Just in case
}

bool Utils::unitTestResultWrapper(int (*func)(int[], int), int array[], int arg, const std::string &func_name, int expected_result[])
{
  func(array, arg);

  // Now we need to test all the elements of the array separately
  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(array, " << arg << ") should set array to " << asString(expected_result, arg) << " but it is " << asString(array, arg);
    msg = oss.str();
  }

  auto std_array = std::vector<int>(array, array + arg);
  auto std_expected_result = std::vector<int>(expected_result, expected_result + arg);
  auto equal = std::equal(std_array.begin(), std_array.end(), std_expected_result.begin());

  EXPECT_TRUE(equal) << formatError(msg);

  return equal;
}

bool Utils::unitTestResultWrapper(void (*func)(int[], int, int[], int), int array1[], int arg1, int array2[], int arg2, const std::string &func_name, int expected_result[], int arg3)
{
  func(array1, arg1, array2, arg2);

  // Now we need to test all the elements of the array separately
  auto msg = std::string();
  {
    auto oss = std::ostringstream();
    oss << func_name << "(array1, " << arg1 << ", array2, " << arg2 << ") should set array to " << asString(expected_result, arg3) << " but it is " << asString(array1, arg3);
    msg = oss.str();
  }

  auto std_array = std::vector<int>(array1, array1 + arg3);
  auto std_expected_result = std::vector<int>(expected_result, expected_result + arg3);
  auto equal = std::equal(std_array.begin(), std_array.end(), std_expected_result.begin());

  EXPECT_TRUE(equal) << formatError(msg);

  return equal;
}
