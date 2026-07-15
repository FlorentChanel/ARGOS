add_executable(ex_0005_TEST ex_0005_TEST.cpp)

target_link_libraries(ex_0005_TEST argos_common GTest::gtest_main)

include(GoogleTest)

gtest_discover_tests(ex_0005_TEST EXTRA_ARGS --gtest_color=1)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0005_CelsiusToFahrenheit/main.c)
  # With a header the exercise uses separate compilation; without it, main.c includes the .c
  if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0005_CelsiusToFahrenheit/ex_0005_CelsiusToFahrenheit.h)
    add_executable(ex_0005 ../../../Exercises/ex_0005_CelsiusToFahrenheit/main.c ../../../Exercises/ex_0005_CelsiusToFahrenheit/ex_0005_CelsiusToFahrenheit.c)
  else()
    add_executable(ex_0005 ../../../Exercises/ex_0005_CelsiusToFahrenheit/main.c)
  endif()
endif()
