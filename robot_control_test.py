#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from robot.RobotCommand import RobotCommand

ROBOT_IP = "192.168.0.226"


if __name__ == "__main__":
    cmd = RobotCommand()    # Robot commander
    cmd.connect(ROBOT_IP)   # Connect to the robot

    # LEDs
    cmd.send_all_led_command((2, 2, 2))  # RGB channels from 0 to 255
    cmd.send_led_command(1, (0, 10, 0))


    try:
        while True:
            v = 0  # Linear velocity
            omega = 15000  # Angular velocity

            # send command to robot
            cmd.send_wheel_command(v, omega)


            # Wait for .1 second
            time.sleep(.1)

    except KeyboardInterrupt:
        # STOP
        cmd.disconnect()
        print('Disconnected')
