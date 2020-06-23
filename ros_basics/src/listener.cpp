#include "ros/ros.h"
#include "std_msgs/String.h" /*Check "std_msgs" is available in 'find_package()' 
and CATKIN_DEPENDS of 'CMakeList.txt' --- and in 'package.xml' or not! */
                                
// Topic messages callback
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{    
    ROS_INFO("[Listener] I heard: [%s]\n", msg->data.c_str());
}

int main(int argc, char **argv)
{
    // Initiate a new ROS node named "listener"
	ros::init(argc, argv, "listener_node");
	//create a node handle: it is reference assigned to a new node
	ros::NodeHandle node; // this Node_Handle will be use to creat publisher & subscriber both...

    // Subscribe to a given topic, in this case "chatter".
	//chatterCallback: is the name of the callback function that will be executed each time a message is received.
    ros::Subscriber sub = node.subscribe("chatter", 1000, chatterCallback); //"chatter"->Common topic,1000-buffer_size

    // Enter a loop, pumping callbacks
    ros::spin();

    return 0;
}