#!usr/bin/env python
# -*-coding:utf-8-*-

import wx,os,re

# 获取activity
def getactivity(event):
    p=os.popen('adb devices')
    #return p.read()
    #contents.SetValue('当前应用的devices是：\n')
    contents.WriteText('当前的devices是：\n'+p.read())

#print getactivity()

# 获取包名称
def getpackage(event):
    p=os.popen('adb shell dumpsys activity activities|findstr \/|findstr realActivity=')
    contents.WriteText('查看运行的包名：\n'+p.read())
    p2=os.popen('adb shell dumpsys window w |findstr \/ |findstr name=')
    contents.WriteText('当前运行的包名：\n'+p2.read())

    # p3=os.popen('adb shell dumpsys activity activities|findstr realActivity=')
    # p4=contents.WriteText('123'+p3.read())
    # print 'test'+contents.GetValue()

    # A.append(contents.WriteText('123'+p3.read()))

# 获取包名的数据
def getinformation():
    file = open('test.txt', 'w')
    file.write(contents.GetValue())
    file.close()
    A = []
    pattern = re.compile(r'name=(.*)(\/)')
    f = open('test.txt')
    for line in f:
        m = pattern.findall(line)
        if m is not None and m:
            A.append(m[0][0])
    if A:
        return A[0]
    else:
        return '请检查连接'

#　杀掉当前进程
def killapp(event):
    getpackage(event)
    s='adb shell am force-stop'+' '+getinformation()
    p = os.popen(s)
    contents.WriteText('停止运行app。。。。')

# 清除数据
def clearbum(event):
    getpackage(event)
    pi=getinformation()
    s='adb shell pm clear'+' '+pi
    p=os.popen(s)
    contents.WriteText('当前app的数据被清除：。。。'+p.read())
# 获取路径
def getpath(event):
    getpackage(event)
    pi=getinformation()
    s='adb shell pm path'+' '+pi
    p=os.popen(s)
    contents.WriteText('当前app存在目录：\n'+p.read())

# 重启手机
def restart(event):
    p=os.popen('adb reboot')
    contents.WriteText('手机重新启动中，请稍后')
# 卸载应用
def appuninstall(event):
    # getpackage(event)
    # pi = getinformation()
    # s = 'adb uninstall' + ' ' + pi
    # p=os.popen(s)
    contents.WriteText('卸载当前app：。。。')
# 获取手机版本
def getversion(event):
    p=os.popen('adb shell getprop ro.build.version.release')
    contents.WriteText('当前系统版本为：\n'+'android   '+p.read())


app=wx.App(False)
frame=wx.Frame(None,title='tools',size=(800,500))
bkg=wx.Panel(frame)

button1=wx.Button(bkg,label='获取当前devices')
button1.Bind(wx.EVT_BUTTON, getactivity)
button2=wx.Button(bkg,label='获取当前包名')
button2.Bind(wx.EVT_BUTTON,getpackage)
button3=wx.Button(bkg,label='重启当前设备')
button3.Bind(wx.EVT_BUTTON,restart)
button4=wx.Button(bkg,label='杀掉当前应用')
button4.Bind(wx.EVT_BUTTON,killapp)
button5=wx.Button(bkg,label='清除当前应用数据')
button5.Bind(wx.EVT_BUTTON,clearbum)
button6=wx.Button(bkg,label='卸载当前应用')
button6.Bind(wx.EVT_BUTTON,appuninstall)
button7=wx.Button(bkg,label='查看系统版本')
button7.Bind(wx.EVT_BUTTON,getversion)
button8=wx.Button(bkg,label='查看应用安装路径')
button8.Bind(wx.EVT_BUTTON,getpath)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)


hbox=wx.BoxSizer()
hbox.Add(button1,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(button2,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(button3,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(button4,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(button5,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(button7,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(button8,proportion=0,flag=wx.LEFT,border=5)



vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(button6,proportion=0,flag=wx.LEFT, border=5)
#vbox.Add(button8,proportion=0, flag=wx.LEFT, border=5)
vbox.Add(contents,proportion=1,flag=wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND,border=5)


bkg.SetSizer(vbox)
frame.Show()
app.MainLoop()