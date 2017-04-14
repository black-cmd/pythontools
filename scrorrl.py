#!usr/bin/env python
#-*-coding:utf-8 -*-
#运行monkeyrunner（脚本置于androidsdk tools下    运行monkeyrunner XXX.py）
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.easy import EasyMonkeyDevice,By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
#from com.android.hierarchyviewerlib.device import ViewNode
import time
import sys
#等待30s,设备名称
device = mr.waitForConnection(30, '4faf528e')
if not device:
    print>>sys.stderr, "设备连接失败"
    sys.exit(1)
else:
    print '1.设备连接成功'

# 安装apk包

# mr.sleep(1)device.installPackage('./maimeng3.5.apk')
# print '2.程序安装成功'

# 启动程序
device.startActivity(component='com.cn.maimeng/.activity.SplashActivity')
mr.sleep(5)
print '3.程序启动成功'

#easy_device=EasyMonkeyDevice(device)
#easy_device.touch(By.xpath("//android.widget.TextView[contains(@text,'美图')]"), MonkeyDevice.DOWN_AND_UP)

device.touch(910,2448,"DOWN_AND_UP")

#向上滑动屏幕
def scrollingUp():
    device.touch(100,500,MonkeyDevice.DOWN)
    device.touch(100,100,MonkeyDevice.MOVE)
    device.touch(100,100,MonkeyDevice.UP)

#向下滑动屏幕
def scrolldownDown():
    device.touch(100,500,MonkeyDevice.DOWN)
    device.touch(100,800,MonkeyDevice.MOVE)
    device.touch(100,800,MonkeyDevice.UP)


# 向下互动屏幕循环次数
for i in range(1, 30050):
    scrollingUp()
    #time.sleep(0)
    i=i+1
    print i

