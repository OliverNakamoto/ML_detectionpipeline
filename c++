#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include <nlohmann/json.hpp>
#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/point_cloud2.hpp>
#include <pcl/point_cloud.h>
#include <pcl/common/transforms.h>
#include <tf2/LinearMath/Transform.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>

using json = nlohmann::json;
using namespace std::chrono;

// Define your point type T here
struct Point {
    float x, y, z;
    // Constructor
    Point(float x_, float y_, float z_) : x(x_), y(y_), z(z_) {}
};

// Define your point cloud type T here
template<typename T>
using CloudPtr = typename pcl::PointCloud<T>::Ptr;

class LidarDetectionNode : public rclcpp::Node {
public:
    LidarDetectionNode() : Node("lidar_detection_node") {
        point_cloud_sub_ = this->create_subscription<sensor_msgs::msg::PointCloud2>(
            "/detection/groundplane_segmented",
            rclcpp::SensorDataQoS(),
            [this](const sensor_msgs::msg::PointCloud2::SharedPtr msg) {
                this->pointCloudCb(msg);
            }
        );
    }

    void pointCloudCb(const sensor_msgs::msg::PointCloud2::SharedPtr msg) {
        // Convert ROS PointCloud2 to PCL point cloud
        CloudPtr<T> input_cloud(new pcl::PointCloud<T>);
        pcl::fromROSMsg(*msg, *input_cloud);

        // Your existing code to process the point cloud goes here...
        // For example:
        clearPointClouds();
        auto t_start = std::chrono::high_resolution_clock::now();
        // rest of your code...
    }

private:
    rclcpp::Subscription<sensor_msgs::msg::PointCloud2>::SharedPtr point_cloud_sub_;
};

int main() {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<LidarDetectionNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
