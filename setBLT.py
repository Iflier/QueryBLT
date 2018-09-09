# -*- coding:utf-8 -*-
"""
Dec: 通过串口设置BLE的参数.HC-05
Createdon： 2018.09.09
Author: Iflier
"""
print(__doc__)

import os
import sys
import serial

PORT = "COM6"
BAUDRATE = 9600

com = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=10)
if com.is_open:
    print("Port is opened.")
    while True:
        command = input("Command -->:")
        if command.lower() == "exit":
            break
        print("Command: {0}".format(command))
        # writtenBytesNum = com.write(command.encode(encoding='utf-8'))
        writtenBytesNum = com.write((command + os.linesep).encode(encoding='utf-8'))
        print("已写入 {0:^5,d} 个字节.".format(writtenBytesNum))
        result = com.readline()
        print("Response -->: {0}".format(result.decode()))
com.close()
print("Done.")