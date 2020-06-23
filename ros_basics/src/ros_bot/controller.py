#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import Tkinter as tk

pub = rospy.Publisher('chatter', String, queue_size=10)

def leftKey(event):
    hello_str="Left"
    rospy.loginfo(hello_str)
    pub.publish(hello_str)

def rightKey(event):
    hello_str="Right"
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
def upkey(event):
    hello_str="Up"
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
def downkey(event):
    hello_str="Down"
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
def stopkey(event):
    hello_str="Stop"
    rospy.loginfo(hello_str)
    pub.publish(hello_str)

def talker():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('chatter', String, queue_size=10)
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node('talker', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1) # 1hz
    #keep publishing until a Ctrl-C is pressed
    i = 0
    
    while not rospy.is_shutdown():
        main = tk.Tk()
        frame = tk.Frame(main, width=100, height=100)
        main.bind('<Left>', leftKey)
        main.bind('<Right>', rightKey)
        main.bind('<Up>', upkey)
        main.bind('<Down>', downkey)
        main.bind("<space>", stopkey)
        rate.sleep()
        i=i+1
        frame.pack()
        main.mainloop()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
