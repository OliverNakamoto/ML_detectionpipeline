import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    cv_image = CvBridge().imgmsg_to_cv2(msg, desired_encoding="bgr8")
    cv2.imshow("Raw Image", cv_image)
    print('hit')
    cv2.waitKey(1)

def main():
    rclpy.init()
    node = rclpy.create_node("image_viewer")
    subscription = node.create_subscription(Image, "/flir_camera/image_raw", image_callback, 1)
    rclpy.spin(node)

if __name__ == "__main__":
    main()
