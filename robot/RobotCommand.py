#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import numpy as np


class RobotCommand:
    def __init__(self):
        self.s = None

    def connect(self, ip, port=5000):
        # Connect to the robot
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        print('Connected')

    def send_wheel_command(self, linear_vel, angular_vel, max_motor=2000):
        v, omega = linear_vel, angular_vel
        u = np.array([v - omega, v + omega])
        u[u > max_motor] = max_motor
        u[u < -max_motor] = -max_motor
        # Send control input to the motors. Each motor receives a value between 0 and 4096
        command = 'CMD_MOTOR#%d#%d#%d#%d\n' % (u[0], u[0], u[1], u[1])
        self.s.send(command.encode('utf-8'))


    def send_led_command(self, led_id, rgb):
        command = 'CMD_LED#%d#%d#%d#%d\n' % (led_id, rgb[0], rgb[1], rgb[2])
        self.s.send(command.encode('utf-8'))

    def send_all_led_command(self, rgb):
        for i in [1,2,4,8,16,32,64,128]:
            self.send_led_command(i, rgb)

    def disconnect(self):
        command = 'CMD_MOTOR#00#00#00#00\n'
        self.s.send(command.encode('utf-8'))

        # Close the connection
        self.s.shutdown(2)
        self.s.close()
