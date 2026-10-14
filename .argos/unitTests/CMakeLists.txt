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
include(GoogleTest)

add_subdirectory(Common)

# Every exercise follows the same frozen structure (enforced by
# 'argos admin check-structure'), so all targets are generated here:
# no per-exercise CMakeLists.
set(EXERCISES_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../Exercises)

file(GLOB exercise_dirs RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/ex_*)
foreach(dir ${exercise_dirs})
  if(NOT IS_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${dir})
    continue()
  endif()

  string(SUBSTRING ${dir} 0 7 exercise_id) # ex_NNNN
  set(test_target ${exercise_id}_TEST)

  add_executable(${test_target} ${dir}/${test_target}.cpp)
  target_link_libraries(${test_target} argos_common m GTest::gtest_main)
  # Same binary layout as the former per-exercise CMakeLists (the CLI test
  # runner looks the binaries up under BUILD/<exercise-fullname>/).
  set_target_properties(${test_target} PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/${dir})
  # Tests run from the exercise build folder, wherever they are launched
  # from (CLI runner, ctest, IDE): stdin fixtures resolve by name there.
  gtest_discover_tests(${test_target} EXTRA_ARGS --gtest_color=1
      WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/${dir})

  # Stdin fixtures: shipped next to the binary, where the CLI runs the tests.
  file(GLOB input_files ${CMAKE_CURRENT_SOURCE_DIR}/${dir}/*_inputs.txt)
  foreach(input_file ${input_files})
    get_filename_component(input_name ${input_file} NAME)
    add_custom_command(TARGET ${test_target} POST_BUILD
      COMMAND ${CMAKE_COMMAND} -E copy_if_different ${input_file} ${CMAKE_BINARY_DIR}/${dir}/${input_name})
  endforeach()

  # Sandbox target, only when the student working copy exists.
  set(sandbox_dir ${EXERCISES_DIR}/${dir})
  if(EXISTS ${sandbox_dir}/main.c)
    # With a header the exercise uses separate compilation; without it, main.c includes the .c
    if(EXISTS ${sandbox_dir}/${dir}.h)
      add_executable(${exercise_id} ${sandbox_dir}/main.c ${sandbox_dir}/${dir}.c)
    else()
      add_executable(${exercise_id} ${sandbox_dir}/main.c)
    endif()
    target_link_libraries(${exercise_id} m)
    set_target_properties(${exercise_id} PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/${dir})
  endif()
endforeach()
