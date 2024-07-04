import os
import yaml
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.substitutions import FindPackageShare
import xacro

#####################################
def generate_launch_description():

  # Robot description for the arm
  yumi_path = get_package_share_directory('yumi_description')
  urdf_model_path = os.path.join(yumi_path, 'urdf', 'yumi.urdf.xacro')
  doc = xacro.process_file(urdf_model_path, mappings={'xyz' : '1.0 0.0 1.5', 'rpy': '3.1416 0.0 0.0', 'arms_interface' : 'PositionJointInterface', 'grippers_interface' :'EffortJointInterface',  'yumi_setup' : 'default'}) 


  # Rviz visualization of arm
  rviz_config = os.path.join(get_package_share_directory("yumi_description"), "yumi.rviz")
  rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config]
  )


  rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='yumi_robot_state_publisher',
        output='screen',
        parameters=[
          {'robot_description': doc.toxml()}
        ],
      )
    
  # Send commands - Joint State publisher
  joint_publisher = Node(
      package='joint_state_publisher_gui',
      executable='joint_state_publisher_gui',
      name='joint_state_publisher_gui',
      parameters=[{"rate": 10}],
      #remappings={('joint_states', "joint_command")},
      output='screen')    
  
  return LaunchDescription(
      [
       rviz_node,
       rsp,
       joint_publisher
      ]
  )



