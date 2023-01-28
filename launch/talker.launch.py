from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return launchDescription{[
		Node(
			package='demo_nodes_cpp',
			executable='talker'
		)
	]}
