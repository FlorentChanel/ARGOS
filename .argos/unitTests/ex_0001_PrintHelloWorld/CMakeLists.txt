add_executable(ex_0001_TEST ex_0001_TEST.cpp)

target_link_libraries(ex_0001_TEST argos_common GTest::gtest_main)

include(GoogleTest)

gtest_discover_tests(ex_0001_TEST EXTRA_ARGS --gtest_color=1)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0001_PrintHelloWorld/main.c)
  # With a header the exercise uses separate compilation; without it, main.c includes the .c
  if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0001_PrintHelloWorld/ex_0001_PrintHelloWorld.h)
    add_executable(ex_0001 ../../../Exercises/ex_0001_PrintHelloWorld/main.c ../../../Exercises/ex_0001_PrintHelloWorld/ex_0001_PrintHelloWorld.c)
  else()
    add_executable(ex_0001 ../../../Exercises/ex_0001_PrintHelloWorld/main.c)
  endif()
endif()
