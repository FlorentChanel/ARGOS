add_executable(ex_0004_TEST ex_0004_TEST.cpp)

target_link_libraries(ex_0004_TEST argos_common GTest::gtest_main)

include(GoogleTest)

gtest_discover_tests(ex_0004_TEST EXTRA_ARGS --gtest_color=1)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0004_Swap/main.c)
  # With a header the exercise uses separate compilation; without it, main.c includes the .c
  if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0004_Swap/ex_0004_Swap.h)
    add_executable(ex_0004 ../../../Exercises/ex_0004_Swap/main.c ../../../Exercises/ex_0004_Swap/ex_0004_Swap.c)
  else()
    add_executable(ex_0004 ../../../Exercises/ex_0004_Swap/main.c)
  endif()
endif()
