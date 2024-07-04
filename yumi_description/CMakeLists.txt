cmake_minimum_required(VERSION 3.5)
project(yumi_description)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

set(dependencies
xacro
)

find_package(ament_cmake REQUIRED)
#find_package(ament_cmake_python REQUIRED)
#find_package(rclpy REQUIRED)

#find_package(rclcpp REQUIRED)
find_package(xacro REQUIRED)


ament_export_dependencies(
#  rclcpp
  ${dependencies}
)


#install(TARGETS
#  ${PROJECT_NAME}_executable
#  DESTINATION lib/${PROJECT_NAME}
#)


# Install Python modules
#ament_python_install_package(${PROJECT_NAME})

# Install Python executables
#install(PROGRAMS
#  scripts/ground_twist_odom_convert.py
#  DESTINATION lib/${PROJECT_NAME}
#)

# Install folders
install(DIRECTORY
  urdf meshes 
  DESTINATION share/${PROJECT_NAME}/
)

install(FILES
  yumi.rviz
  DESTINATION share/${PROJECT_NAME}/
)
  

ament_package()
