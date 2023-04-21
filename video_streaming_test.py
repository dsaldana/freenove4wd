#!/usr/bin/python 
# -*- coding: utf-8 -*-

import cv2


from robot.VideoStreaming import VideoStreaming

ROBOT_IP = "192.168.0.226"


def camera_listener(image):
    cv2.imshow('video', image)
    print('aa', image)


if __name__ == '__main__':
    client = VideoStreaming()

    client.streaming(ROBOT_IP, listener=camera_listener)

    # client.connect()
    # while True:
    #     time.sleep(1)
    #     print('a')
    client.StopTcpcClient()