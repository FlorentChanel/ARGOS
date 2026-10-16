#include <iostream>
#include <sstream>
#include <string>

#include <gtest/gtest.h>

namespace Utils
{
  // Mute/unmute program output when stating status
  void muteStdout();
  void unmuteStdout();

  // Custom error output
  std::string asString(int array[], int nb_vals);
  std::string formatError(const std::string &msg);

  // Custom unit tests
  bool expectEQ(int arr1[], int arr2[], int nb_vals);

  bool unitTestStatusWrapper(bool (*func)(int), int arg, const std::string &func_name, bool expected_status);
  bool unitTestStatusWrapper(int (*func)(int[], int), int arr[], int arg, const std::string &func_name, int expected_result);
  bool unitTestStatusWrapper(bool (*func)(int[], int[], int), int arr1[], int arr2[], int arg3, const std::string &func_name, bool expected_result);
  bool unitTestStatusWrapper(int (*func)(int[], int[], int), int arr1[], int arr2[], int arg3, const std::string &func_name, int expected_result);

  bool unitTestOutputWrapper(bool (*func)(int), int arg, const std::string &func_name, const std::string &expected_output);
  bool unitTestOutputWrapper(void (*func)(int[], int), int array[], int arg, const std::string &func_name, const std::string &expected_output);

  bool unitTestResultWrapper(int (*func)(int), int arg, const std::string &func_name, int expected_result);
  bool unitTestResultWrapper(int (*func)(int, int), int arg1, int arg2, const std::string &func_name, int expected_result);
  bool unitTestResultWrapper(double (*func)(double), int arg, const std::string &func_name, double expected_result);
  bool unitTestResultWrapper(double (*func)(double), double arg, const std::string &func_name, double expected_result);
  bool unitTestResultWrapper(double (*func)(double, double, double), double arg1, double arg2, double arg3, const std::string &func_name, double expected_result);
  bool unitTestResultWrapper(double (*func)(double, double, int), double arg1, double arg2, int arg3, const std::string &func_name, double expected_result);
  bool unitTestResultWrapper(double (*func)(double, double, char), double arg1, double arg2, char arg3, const std::string &func_name, double expected_result);
  bool unitTestResultWrapper(int (*func)(int[], int), int array[], int arg, const std::string &func_name, int expected_result[]);
  bool unitTestResultWrapper(void (*func)(int[], int, int[], int), int array1[], int arg1, int array2[], int arg2, const std::string &func_name, int expected_result[], int arg3);
}
