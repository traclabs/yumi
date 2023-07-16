cmake_minimum_required(VERSION 3.16.0)
project(yumi_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY meshes urdf
  DESTINATION share/${PROJECT_NAME}/
)

set(DEPS
  xacro
)

foreach(dependency ${DEPS})
  find_package(${dependency} REQUIRED)
endforeach()

ament_export_dependencies(${DEPS})

ament_package()


