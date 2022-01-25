#!/usr/bin/env python
import rospy 
from std_msgs.msg import Float32

class Cars():

    def __init__(self, ini_pos, ini_velo,wall_len):
        self.pos = ini_pos
        self.velo = ini_velo
        self.tol = 0.05
        self.wall = wall_len
        self.pub = rospy.Publisher('car1_pos', Float32, queue_size=10, latch=True)
        self.rate = rospy.Rate(10)
        # pubulish its initial position
        self.pub.publish(self.pos)
        #rospy.loginfo(self.pos)

        rospy.Subscriber('car2_pos', Float32, self.callback)

    def callback(self,data):
        self.car2_p = float(data.data)
        message = self.pos
        self.pub.publish(message)
        #rospy.loginfo(self.pos)
        self.rate.sleep()
        
        #check car1 position
        #print(message)

        # check walls first
        if self.pos >= self.wall-self.tol or self.pos <= 0.0+self.tol:
            self.velo = -1.0 * self.velo

        # check collision with car 2 on the positive direction
        if self.pos >= self.car2_p - 2.0*self.tol:
            self.velo = -1.0 * self.velo
        
        self.pos = self.pos + (1.0/10.0) * self.velo


if __name__ == "__main__":
    initial_pos = 1.0
    initial_velocity = -0.1
    wall_len = 10.0
    rospy.init_node('car1', anonymous=True)
    car1 = Cars(initial_pos, initial_velocity,wall_len)
    rospy.spin()
    
