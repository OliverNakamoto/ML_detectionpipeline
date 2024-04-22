#include <iostream>
#include <vector>
#include <chrono>
#include <pcl/point_cloud.h>
#include <sensor_msgs/msg/point_cloud2.hpp>
#include <pcl/common/transforms.h>
#include <tf2/LinearMath/Transform.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.hpp>

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
    clearPointClouds();
  
    auto t_start = high_resolution_clock::now();

    tf2::Transform tf;
    tf2::fromMsg(params_.lidar.input_to_rotated_lidar_frame, tf);
    pcl_ros::transformPointCloud(*input_cloud, *input_cloud, tf);
    input_cloud->header.frame_id = "rotated_lidar_0";

    CloudPtr<T> test_cloud(new pcl::PointCloud<T>);
    pcl::copyPointCloud(*input_cloud, *test_cloud);

    // Vector to store x and y coordinates
    std::vector<std::pair<float, float>> points_xy;

    // Iterate through your point cloud and extract x and y coordinates
    for (int i = 0; i < test_cloud->size(); ++i) {
        T point = test_cloud->points[i];
        points_xy.emplace_back(point.x, point.y);
    }

    // Get current time to use as the filename
    auto t_now = high_resolution_clock::now();
    MillisecondsDouble duration = duration_cast<MillisecondsDouble>(t_now - t_start);
    double timestamp = duration.count();

    std::string filename = "pointList_" + std::to_string(timestamp) + ".txt";

    // Save the points_xy into a file
    std::ofstream outputFile(filename);
    if (outputFile.is_open()) {
        for (const auto& point : points_xy) {
            outputFile << point.first << " " << point.second << std::endl;
        }
        outputFile.close();
        std::cout << "Point list saved to " << filename << std::endl;
    } else {
        std::cerr << "Unable to open file for writing!" << std::endl;
        return 1; // indicate error
    }

    return 0; // indicate success
}
