#!/usr/bin/env python
import rospy 
import message_filters
from std_msgs.msg import Float32

class Cars():

    def __init__(self, ini_pos, ini_velo,wall_len):
        self.pos = ini_pos
        self.velo = ini_velo
        self.tol = 0.05
        self.wall = wall_len
        self.pub = rospy.Publisher('car4_pos', Float32, queue_size=10, latch=True)
        self.rate = rospy.Rate(10)
        # pubulish its initial position
        self.pub.publish(self.pos)
        #rospy.loginfo(self.pos)

        # subscribe to its nabors
        subscriber_left = message_filters.Subscriber('car3_pos', Float32)
        subscriber_right= message_filters.Subscriber('car5_pos', Float32)
        ts = message_filters.ApproximateTimeSynchronizer([subscriber_left, subscriber_right], queue_size=10, slop=0.5, allow_headerless=True)
        ts.registerCallback(self.callback)

    def callback(self,sub_left, sub_right):
        self.car3_p = float(sub_left.data)
        self.car5_p = float(sub_right.data)

        message = self.pos
        self.pub.publish(message)
        self.rate.sleep()
        
        #check car1 position
        #print(message)

        # check walls first
        if self.pos >= self.wall-self.tol or self.pos <= 0.0+self.tol:
            self.velo = -1.0 * self.velo

        # check collision with car3 in the positive direction
        if self.pos >= self.car5_p - 2.0*self.tol:
            self.velo = -1.0 * self.velo

        # check collision with car1 in the negative direction
        if self.pos <= self.car3_p + 2.0*self.tol:
            self.velo = -1.0* self.velo

        self.pos = self.pos + (1.0/10.0) * self.velo


if __name__ == "__main__":
    initial_pos = 7.0
    initial_velocity = -0.15
    wall_len = 10.0
    rospy.init_node('car4', anonymous=True)
    car4 = Cars(initial_pos, initial_velocity,wall_len)
    rospy.spin()
    
