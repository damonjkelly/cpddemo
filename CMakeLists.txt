cmake_minimum_required(VERSION 2.8)

find_package(Cpd REQUIRED)
add_executable(cpdexample
    src/main.cpp
    )
target_link_libraries(cpdexample
    PUBLIC
    Cpd::Library-C++
    )
