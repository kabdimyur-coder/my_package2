#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped
import math

def quaternion_from_yaw(yaw):
    """Простой конвертер yaw в кватернион (упрощённо, без tf)."""
    from tf.transformations import quaternion_from_euler
    return quaternion_from_euler(0, 0, yaw)

def send_goal(client, x, y, yaw):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"  # или "odom", зависит от твоей настройки
    goal.target_pose.header.stamp = rospy.Time.now()
    
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    qx, qy, qz, qw = quaternion_from_yaw(yaw)
    goal.target_pose.pose.orientation.x = qx
    goal.target_pose.pose.orientation.y = qy
    goal.target_pose.pose.orientation.z = qz
    goal.target_pose.pose.orientation.w = qw
    
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        return False
    state = client.get_state()
    if state == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo(f"Достигнута точка ({x:.2f}, {y:.2f})")
        return True
    else:
        rospy.logwarn(f"Не удалось достичь точки ({x:.2f}, {y:.2f}), состояние: {state}")
        return False

if __name__ == '__main__':
    rospy.init_node('turtlebot_waypoints')
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    rospy.loginfo("Ожидание сервера move_base...")
    client.wait_for_server()
    rospy.loginfo("Сервер move_base доступен.")

    # Твой маршрут
    waypoints = [
        [1.5,  1.5],
        [1.5, -1.5],
        [0.5, -1.5],
        [0.5,  1.5],
        [-0.5, 1.5],
        [-0.5,-1.5],
        [-1.5,-1.5],
        [-1.5, 1.5],
        [ 1.5, 1.5],
    ]

    for i in range(len(waypoints)):
        x, y = waypoints[i]
        
        # Вычисляем угол к следующей точке (или к текущей, если это первая)
        if i == 0:
            # Для первой точки можно задать, например, 0 радиан
            yaw = 0.0
        else:
            prev_x, prev_y = waypoints[i-1]
            yaw = math.atan2(y - prev_y, x - prev_x)
        
        success = send_goal(client, x, y, yaw)
        if not success:
            rospy.logerr("Прерывание маршрута из-за ошибки.")
            break

    rospy.loginfo("Маршрут завершён.")
