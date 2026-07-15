add_library(argos_common STATIC Utils.cpp)

target_include_directories(argos_common PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/..)

target_link_libraries(argos_common PUBLIC GTest::gtest)
