#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan, Imu, JointState
from nav_msgs.msg import Odometry

def scan_callback(msg):
    rospy.loginfo("Получено %d лучей из /scan", len(msg.ranges))

def imu_callback(msg):
    rospy.loginfo("Угловая скорость (x,y,z): %.3f, %.3f, %.3f рад/с",
                  msg.angular_velocity.x,
                  msg.angular_velocity.y,
                  msg.angular_velocity.z)

def odom_callback(msg):
    rospy.loginfo("Скорость робота: %.3f м/с, %.3f рад/с",
                  msg.twist.twist.linear.x,
                  msg.twist.twist.angular.z)

def joint_callback(msg):
    for name, pos, vel, effort in zip(msg.name, msg.position, msg.velocity, msg.effort):
        rospy.loginfo("%s: pos=%.3f rad, vel=%.3f rad/s, effort=%.3f Nm",
                      name, pos, vel, effort)

rospy.init_node('turtlebot3_sensors_subscriber')

rospy.Subscriber('/scan', LaserScan, scan_callback)
rospy.Subscriber('/imu', Imu, imu_callback)          # или /imu/data
rospy.Subscriber('/odom', Odometry, odom_callback)
rospy.Subscriber('/joint_states', JointState, joint_callback)

rospy.spin()
