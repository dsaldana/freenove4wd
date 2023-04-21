#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from threading import Thread

import numpy as np
import cv2
import socket
import io
import struct
from PIL import Image


class VideoStreaming:

    def __init__(self):
        self.image = None
        self.running = False

    def StopTcpcClient(self):
        try:
            self.client_socket.shutdown(2)
            self.client_socket.close()

            # os.remove("video.jpg")
            # os._exit(0)
        except Exception as e:
            raise e

    def isValidImage4Bytes(self, buf):
        bValid = True
        if buf[6:10] in (b'JFIF', b'Exif'):
            if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):
                bValid = False
        else:
            try:
                Image.open(io.BytesIO(buf)).verify()
            except:
                bValid = False
        return bValid


    def connect(self, ip):
        try:
            streaming = Thread(target=self.streaming, args=(ip,))
            streaming.start()
        except Exception as e:
            raise e


    def streaming(self, ip, listener=None):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.client_socket.connect((ip, 8000))
            self.connection = self.client_socket.makefile('rb')
        except Exception as e:
            # print "command port connect failed"
            raise e

        self.running = True
        while self.running:
            try:
                stream_bytes = self.connection.read(4)
                leng = struct.unpack('<L', stream_bytes[:4])
                jpg = self.connection.read(leng[0])
                if self.isValidImage4Bytes(jpg):
                    image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    self.image = image

                    if not listener is None:
                        listener(image)

            except Exception as e:
                raise e
