#!/usr/bin/env python
import rospy 
import message_filters
from std_msgs.msg import Float32
import matplotlib.animation as animation
import matplotlib.pyplot as plt

class listener():
    
    def __init__(self):
        sub_car1 = message_filters.Subscriber('car1_pos', Float32)
        sub_car2 = message_filters.Subscriber('car2_pos', Float32)
        sub_car3 = message_filters.Subscriber('car3_pos', Float32)
        sub_car4 = message_filters.Subscriber('car4_pos', Float32)
        sub_car5 = message_filters.Subscriber('car5_pos', Float32)

        sync = message_filters.ApproximateTimeSynchronizer([sub_car1, sub_car2, sub_car3, sub_car4, sub_car5], queue_size=10, slop=0.5, allow_headerless=True)
        sync.registerCallback(self.callbacks)

    def callbacks(self,car1, car2, car3, car4, car5):
        self.c1p = float(car1.data)
        self.c2p = float(car2.data)
        self.c3p = float(car3.data)
        self.c4p = float(car4.data)
        self.c5p = float(car5.data)

def animate(i):
    ax.clear()
    ax.scatter(listen.c1p,0, c='red')
    ax.scatter(listen.c2p,0, c='blue')
    ax.scatter(listen.c3p,0, c='yellow')
    ax.scatter(listen.c4p,0, c='green')
    ax.scatter(listen.c5p,0 ,c='black')

if __name__ == "__main__":
    rospy.init_node('animation', anonymous=True)
    listen = listener()
    # animate data with matplotlib
    # setup figure
    fig, ax = plt.subplots(figsize=(10,5))
    anim = animation.FuncAnimation(fig, animate ,interval=100)
    plt.show()

    rospy.spin()