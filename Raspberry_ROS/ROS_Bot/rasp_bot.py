#!/usr/bin/env python
import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time # Import the sleep function from the time module

#GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(7, GPIO.OUT) # Set pin 7 to be an output pin and set initial value to low (off)
GPIO.setup(11, GPIO.OUT) # Set pin 7 to be an output pin and set initial value to low (off)
GPIO.setup(13, GPIO.OUT) # Set pin 7 to be an output pin and set initial value to low (off)
temp=""

def move_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    rospy.loginfo(rospy.get_caller_id() + "Direction %s", message.data)
    temp=message.data
    print(temp)
    if(temp=="Up"):
        print("ok")
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
	GPIO.output(11, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
    if(temp=="Left"):
        GPIO.output(8, GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
	GPIO.output(11, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
    if(temp=="Right"):
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)
	GPIO.output(11, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
    if(temp=="Down"):
        GPIO.output(8, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
	GPIO.output(11, GPIO.HIGH)	
	GPIO.output(13, GPIO.HIGH)
    if(temp=="Stop"):
        GPIO.output(8, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
	GPIO.output(11, GPIO.LOW)	
	GPIO.output(13, GPIO.LOW)

    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, move_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
