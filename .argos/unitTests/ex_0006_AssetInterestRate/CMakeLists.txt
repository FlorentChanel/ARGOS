add_executable(ex_0006_TEST ex_0006_TEST.cpp)

target_link_libraries(ex_0006_TEST argos_common GTest::gtest_main)

include(GoogleTest)

gtest_discover_tests(ex_0006_TEST EXTRA_ARGS --gtest_color=1)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0006_AssetInterestRate/main.c)
  # With a header the exercise uses separate compilation; without it, main.c includes the .c
  if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../../../Exercises/ex_0006_AssetInterestRate/ex_0006_AssetInterestRate.h)
    add_executable(ex_0006 ../../../Exercises/ex_0006_AssetInterestRate/main.c ../../../Exercises/ex_0006_AssetInterestRate/ex_0006_AssetInterestRate.c)
  else()
    add_executable(ex_0006 ../../../Exercises/ex_0006_AssetInterestRate/main.c)
  endif()
endif()
