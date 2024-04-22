import rclpy
from sensor_msgs.msg import PointCloud2
import numpy as np
import os
from datetime import datetime
from builtin_interfaces.msg import Time

def callback(msg):
    # Extract x and y coordinates from the point cloud
    points = []
    fields = [f.name for f in msg.fields]
    data = np.frombuffer(msg.data, dtype=np.float32)
    point_size = len(fields)
    point_count2 = len(data)# // point_size
    point_count = len(data)/ 12

    k=0
    print(data[:15])
    for i in range(0, point_count2, 12): #, point_size):
        #if data[i + fields.index('x')]<40 and data[i + fields.index('y')]<40:
        x = data[i + fields.index('x')]
        y = data[i + fields.index('y')]
        #print(fields)
        #print(data[i:i+12])
        intensity = data[i+4]
        #intense = data[i + fields.index('intensity')]

        if abs(x)>0.1 and abs(y)>0.1: # 2.1>y and y>-2.1:
            points.append((x, y, intensity)) #,intense))
            print(len(data))
            print(i,k)
            k+=1


    timestamp = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9

    msg_timestamp = msg.header.stamp
    offset = 177579.9448

    # Convert to ROS time object
    ros_time = Time()
    ros_time.sec = msg_timestamp.sec
    ros_time.nanosec = msg_timestamp.nanosec


    directory = "trial_3.1"
    if not os.path.exists(directory):
        os.makedirs(directory)


    # Save points to a new file with the timestamp as the filename
    filename = f"{directory}/{timestamp+offset}.txt"

    with open(filename, 'a') as file:
        file.write(f'Timestamp fo ptCloud: {timestamp+offset}\n')
        file.write('x:                         y:\n')
        for point in points:
            file.write(f"{point[0]}, {point[1]}, {point[2]}\n")

def main(args=None):
    rclpy.init(args=args)

    # Create a node
    node = rclpy.create_node('pointcloud_subscriber')

    # Create a subscriber for the point cloud topic
    subscriber = node.create_subscription(
        PointCloud2,
        '/detection/groundplane_segmented',
        callback,
        qos_profile=rclpy.qos.qos_profile_sensor_data
    )

    # Spin the node
    rclpy.spin(node)

    # Shutdown
    rclpy.shutdown()

if __name__ == '__main__':
    main()
