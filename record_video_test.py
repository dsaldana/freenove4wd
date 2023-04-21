#!/usr/bin/python 
# -*- coding: utf-8 -*-

import cv2

from robot.RobotCommand import RobotCommand
from robot.VideoStreaming import VideoStreaming

ROBOT_IP = "192.168.0.226"
NUM_FRAMES = 50



def save_video(frames):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    width = len(frames[0][0])
    height = len(frames[0])

    fps = 10
    out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))
    for frame in frames:
        out.write(frame)
    out.release()


if __name__ == '__main__':
    client = VideoStreaming()
    frames = []

    # Robot interface
    cmd = RobotCommand()
    cmd.connect(ROBOT_IP)
    cmd.send_wheel_command(900, 1000)

    def camera_listener(image):
        # cv2.imshow('video', image)
        print('aa', image)
        frames.append(image)

        if len(frames) >= NUM_FRAMES:
            client.running = False
    try:
        client.streaming(ROBOT_IP, listener=camera_listener)
    except KeyboardInterrupt:
        cmd.send_wheel_command(0, 0)
    cmd.disconnect()
    save_video(frames)      # Save video
    client.StopTcpcClient()     # Stop connection

