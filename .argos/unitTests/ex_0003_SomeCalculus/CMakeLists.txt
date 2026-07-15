add_executable(ex_0003_TEST ex_0003_TEST.cpp)

target_link_libraries(ex_0003_TEST argos_common GTest::gtest_main)

include(GoogleTest)

gtest_discover_tests(ex_0003_TEST EXTRA_ARGS --gtest_color=1)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0003_SomeCalculus/main.c)
  # With a header the exercise uses separate compilation; without it, main.c includes the .c
  if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0003_SomeCalculus/ex_0003_SomeCalculus.h)
    add_executable(ex_0003 ../../../Exercises/ex_0003_SomeCalculus/main.c ../../../Exercises/ex_0003_SomeCalculus/ex_0003_SomeCalculus.c)
  else()
    add_executable(ex_0003 ../../../Exercises/ex_0003_SomeCalculus/main.c)
  endif()
endif()
