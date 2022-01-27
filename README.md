# interprocess-communication-via-ROS
The output of this project should look like the following screenshot:
<img width="500" alt="car_comms" src="https://user-images.githubusercontent.com/68209991/151266243-33777427-9377-43c8-9f81-4131f8c19cf9.PNG">
  
Five "cars" with different colors run on their on process and communicate to each other via ROS channels. Each car will turn around before crash into its neghbors. There is two virtual walls, one locates at x=0 the other locates at x=10. Cars will turn around before hitting the walls.  

This project is created based on ROS melodic  
To run this project:  
step1: navigate to your catkin workspace: cd ~/catkin_ws/src  
step2: clone the github repository: git clone https://github.com/zzheding/interprocess-comms-ROS.git  
step3: navigate to scripts file and make all python files executable by using "chmod" commmend  
step4: navigate to catkin workspace and do catkin_make  
step5: run: source devel/setup.bash  
step6: run: roslaunch cars_comms comms.launch  
