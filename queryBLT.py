# -*- coding:utf-8 -*-
"""
Dec: 终于摆脱了线缆的束缚 :-)
Created on: 2018.09.09
Author: Iflier
"""
print(__doc__)

import os
import sys
import argparse

import serial


ap = argparse.ArgumentParser(description="读取通过远程蓝牙设备传送的传感器数据, 命令字符串不区分大小写.\tcommand -->:\ta: 获取高度\tt: 获取温度\tp: 获取气压")
ap.add_argument("-p", "--port", type=str, default="COM6", help="Specify a com port.")
ap.add_argument("-b", "--baudrate", type=int, default=9600, help="Specify a baud rate.")
args = vars(ap.parse_args())

# 最多等待15秒，然后返回
com = serial.Serial(port=args["port"], baudrate=args["baudrate"], timeout=15)

if com.is_open:
    while True:
        command = input("Command -->:")
        if command.lower() == "exit":
            break
        writtenBytesNum = com.write((command.upper() + ";").encode())
        print("Written {0:^5,d} bytes.".format(writtenBytesNum))
        result = com.readlines()
        print("Response -->:")
        for index, line in enumerate(result, 1):
            print("Line {0}: {1}".format(index, line.decode()))
com.close()
print("Done.")
