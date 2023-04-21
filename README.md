# Remote control for Freenove 4WD robot
Simple interface for the Freenove 4 wheel drive robot

This library includes the following functionalities:
* Send linear and angular velocities to the robot. Try ``robot_control_test.py``
* Set the colors of the LEDs.
* Stream video from robot camera. Try ``video_streaming_test.py``
* Record video from the robot camera. Try ``record_video_test.py``

Make sure to run the server on the robot. Example:
 ```
$ sudo python ~/Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server/main.py -tn
 ```
Set the constat ``ROBOT_IP`` with the ip of your robot.



----
Note that there is a bug that requires restarting the server everytime there is video streaming.
