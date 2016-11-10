cmake_minimum_required(VERSION 3.3)
project(L11)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(L11 ${SOURCE_FILES})