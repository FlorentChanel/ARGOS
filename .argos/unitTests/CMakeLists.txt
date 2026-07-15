cmake_minimum_required(VERSION 3.25)

project(ARGOS_Bank_Evaluation VERSION 0.1 LANGUAGES C CXX
    DESCRIPTION "ARGOS: Evaluation of exercises")


set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# Generate compile_commands.json to improve IDE support.
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Force colored outputs
set(CMAKE_COLOR_DIAGNOSTICS ON)

# Add warning for gcc/clang
add_compile_options(-Wall -Wextra -Wpedantic)

####################
#    GoogleTests   #
####################
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

##################
#     Sources    #
##################
set(BUILD_SHARED_LIBS OFF)

enable_testing()

file(GLOB exercise_dirs RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/*)
foreach(dir ${exercise_dirs})
  if(IS_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${dir})
    add_subdirectory(${dir})
  endif()
endforeach()
