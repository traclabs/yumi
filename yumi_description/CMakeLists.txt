cmake_minimum_required(VERSION 3.5)
project(yumi_description)

add_compile_options(-std=c++14)

set(DEPS
  xacro
)

find_package(ament_cmake REQUIRED)


foreach(dependency ${DEPS})
  find_package(${dependency} REQUIRED)
endforeach()


install( DIRECTORY urdf meshes
         DESTINATION share/${PROJECT_NAME} 
)

ament_export_dependencies(${DEPS})
ament_package()
