from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os 
def generate_launch_description():
    
    ld = LaunchDescription()
    config = os.path.join(
        get_package_share_directory('vision'),
        'config',
        'params.yaml'
        )
    vision_node = Node(
        package='vision',
        executable='vision_node',
        name='vision_node',
        parameters=[config]
    )

    ld.add_action(vision_node)

    return ld