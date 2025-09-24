import rospy
from sensor_msgs.msg import JointState
import math
import time

rospy.init_node('joint_mover', anonymous=True)
pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
rate = rospy.Rate(10)

# Список шарниров
joint_names = ['joint1', 'joint2', 'joint3']
t = 0

while not rospy.is_shutdown():
    js = JointState()
    js.header.stamp = rospy.Time.now()
    js.name = joint_names
    
    # Движение по синусоиде
    js.position = [
        0.5 * math.sin(t),
        0.3 * math.sin(t + 0.5),
        0.2 * math.sin(t + 1.0)
    ]
    
    pub.publish(js)
    t += 0.1
    rate.sleep()