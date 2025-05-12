#! /usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch import LaunchService
def generate_launch_description():
    ld = LaunchDescription()

    yolo_obb_node = Node(
        package="run_test",
        executable="sample",
        output="screen",
        name="yolo_obb_node",
        namespace="v4l2_camera"
    )

    v4l2_camera_node = Node(
        package="v4l2_camera",
        executable="v4l2_camera_node",
        output="screen",
        name="v4l2_camera_node",
        namespace="v4l2_camera",
        parameters=[
            {"video_device":"/dev/video2"}
        ]
    )

    ld.add_action(yolo_obb_node)
    ld.add_action(v4l2_camera_node)
    return ld

# if __name__ == "__main__":
#     ls = LaunchService()
#     ls.include_launch_description(generate_launch_description)
#     ls.run()