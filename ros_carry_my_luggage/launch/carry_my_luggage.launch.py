from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package="turtlebot_bringup",
            node_executable="turtlebot2",
            output="screen"
        ),

        launch_ros.actions.Node(
            package="ydlidar",
            node_executable="ydlidar_node",
            output="screen"
        ),

        launch_ros.actions.Node(
            package="follow_me",
            node_executable="follow_me",
            output="screen"

        ),

        launch_ros.actions.Node(
            package="sound_system",
            node_executable="turtlebot_button0",
            output="screen"
        ),

        launch_ros.actions.Node(
            package="sound_system",
            node_executable="sound_speak1",
            output="screen"
        ),

        launch_ros.actions.Node(
            package="sound_system",
            node_executable="sound_stop",
            output="screen"

        ),

        launch_ros.actions.Node(
            package="location_register",
            node_executable="location_register_node",
            output="screen"

        ),

        launch_ros.actions.Node(
            package="slam_gmapping",
            node_executable="slam_gmapping",
            output="screen"

        ),
    ])
