import rclpy
from sensor_msgs.msg import PointCloud2
import numpy as np

def callback(msg, points_list):
    # Extract x and y coordinates from the point cloud
    points = []
    fields = [f.name for f in msg.fields]
    data = np.frombuffer(msg.data, dtype=np.float32)
    point_size = len(fields)
    for i in range(0, 300, point_size):
        x_coord = data[i + fields.index('x')]
        y_coord = data[i + fields.index('y')]
        points.append((x_coord, y_coord, len(points_list)))
        print(i)

    # Store the points in the provided list
    points_list.extend(points)

def main(args=None):
    rclpy.init(args=args)

    # Create a node
    node = rclpy.create_node('pointcloud_subscriber')

    # Create a list to store the points
    points_list = []

    # Create a subscriber for the point cloud topic
    subscriber = node.create_subscription(
        PointCloud2,
        '/detection/groundplane_segmented',
        lambda msg: callback(msg, points_list),
        qos_profile=rclpy.qos.qos_profile_sensor_data
    )

    # Create a timer to stop the node after 5 seconds of inactivity
    stop_timer = node.create_timer(5.0, lambda: shutdown_node(node))

    # Spin the node
    rclpy.spin(node)

    directory = "ptClouds"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save points to a new file with the timestamp as the filename
    filename = f"{'timestampsssss'}.txt"

    # Save the points to a text file
    with open(filename, 'a') as file:
        file.write('x:         y:')
        for point in points_list[:100]:
            file.write(f"{point[0]}, {point[1]}\n")
    print("Points saved to points.txt")


def shutdown_node(node):
    node.get_logger().info('Shutting down node due to inactivity')
    node.destroy_node()
    rclpy.shutdown()
    exit()  # Exit the script after shutting down the node and ROS 2 system


if __name__ == '__main__':
    main()
