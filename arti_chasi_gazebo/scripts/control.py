#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64

front_left_wheel_joint_controller_pub = rospy.Publisher('/chasi/front_left_wheel_joint_controller/command', Float64, queue_size=10)
front_right_wheel_joint_controller_pub = rospy.Publisher('/chasi/front_right_wheel_joint_controller/command', Float64, queue_size=10)
rear_left_wheel_joint_controller_pub = rospy.Publisher('/chasi/rear_left_wheel_joint_controller/command', Float64, queue_size=10)
rear_right_wheel_joint_controller_pub = rospy.Publisher('/chasi/rear_right_wheel_joint_controller/command', Float64, queue_size=10)
front_left_hinge_joint_controller_pub = rospy.Publisher('/chasi/front_left_hinge_joint_controller/command', Float64, queue_size=10)
front_right_hinge_joint_controller_pub = rospy.Publisher('/chasi/front_right_hinge_joint_controller/command', Float64, queue_size=10)
rear_left_hinge_joint_controller_pub = rospy.Publisher('/chasi/rear_left_hinge_joint_controller/command', Float64, queue_size=10)
rear_right_hinge_joint_controller_pub = rospy.Publisher('/chasi/rear_right_hinge_joint_controller/command', Float64, queue_size=10)
topic_mapping = {'front_left_hinge_joint': 0,\
'front_left_wheel_joint': 1,\
'front_right_hinge_joint': 2,\
'front_right_wheel_joint': 3,\
'front_steering_joint': 4,\
'rear_left_hinge_joint': 5,\
'rear_left_wheel_joint': 6,\
'rear_right_hinge_joint': 7,\
'rear_right_wheel_joint': 8}


def control():

    rospy.init_node('gazebo_control_manager', anonymous=True)
    rospy.Subscriber("joint_states", JointState, callback)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        rate.sleep()


def callback(data):
    """

    :param data:
    :type data: JointState
    :return:
    """

    num_pos = len(data.position)
    #rospy.loginfo("Number of positions: %d", num_pos)
    front_left_wheel_joint_controller_pub.publish(data.velocity[topic_mapping['front_left_wheel_joint']])
    front_right_wheel_joint_controller_pub.publish(data.velocity[topic_mapping['front_right_wheel_joint']])
    rear_left_wheel_joint_controller_pub.publish(data.velocity[topic_mapping['rear_left_wheel_joint']])
    rear_right_wheel_joint_controller_pub.publish(data.velocity[topic_mapping['rear_right_wheel_joint']])
    front_left_hinge_joint_controller_pub.publish(data.position[topic_mapping['front_left_hinge_joint']])
    front_right_hinge_joint_controller_pub.publish(data.position[topic_mapping['front_right_hinge_joint']])
    rear_left_hinge_joint_controller_pub.publish(data.position[topic_mapping['rear_left_hinge_joint']])
    rear_right_hinge_joint_controller_pub.publish(data.position[topic_mapping['rear_right_hinge_joint']])


if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass