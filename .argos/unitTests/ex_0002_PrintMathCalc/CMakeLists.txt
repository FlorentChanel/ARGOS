add_executable(ex_0002_TEST ex_0002_TEST.cpp)

target_link_libraries(ex_0002_TEST argos_common GTest::gtest_main)

include(GoogleTest)

gtest_discover_tests(ex_0002_TEST EXTRA_ARGS --gtest_color=1)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0002_PrintMathCalc/main.c)
  # With a header the exercise uses separate compilation; without it, main.c includes the .c
  if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0002_PrintMathCalc/ex_0002_PrintMathCalc.h)
    add_executable(ex_0002 ../../../Exercises/ex_0002_PrintMathCalc/main.c ../../../Exercises/ex_0002_PrintMathCalc/ex_0002_PrintMathCalc.c)
  else()
    add_executable(ex_0002 ../../../Exercises/ex_0002_PrintMathCalc/main.c)
  endif()
endif()
