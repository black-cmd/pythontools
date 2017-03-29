#!/usr/bin/python
# -*-coding:utf-8-*-
__author__ = 'zxd'
'''date:2017-03-14'''

import wx
import requests
import json

def load(event):
    # file = open(filename.GetValue())
    # contents.SetValue(file.read())
    # file.close()
    v= choice(event)
    if v == 0:
        url = str(filename.GetValue())
        r = requests.post(url, headers={'clientversion': '1.0',
                   'clientid':'apitest',
                   'devicetype':'4',
                   'deviceinfo':'iPhone',
                   'devicetoken':'57e102a1121b9ed3040cc3e15f5f82a463a6d457',
                   'userid':'4',
                   'logintime':'1490342538',
                   'requesttime':'1490342538'}, data={'r':'user/add'})
        print r.text
        va = contents.SetValue(r.text)
    elif v == 1:
        #print 'hello'
        url=str(filename.GetValue())
        ployed={"r":"user/list","page":"1","size":"10"}
        r=requests.get(url, params=ployed)
        print r.text
        va = contents.SetValue(r.text)


def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(contents.GetValue())
    file.close()


def choice(event):
    v=remethod.CurrentSelection
    return v



app = wx.App()
win = wx.Frame(None, title='网络接口测试', size=(410, 335))
bkg = wx.Panel(win)

loadbutton = wx.Button(bkg, label='发送')
loadbutton.Bind(wx.EVT_BUTTON, load)
saveButton = wx.Button(bkg, label='保存')
saveButton.Bind(wx.EVT_BUTTON, save)
remethod=wx.Choice(bkg, choices=['post','get', 'put', 'delete'])
remethod.Bind(wx.EVT_CHOICE,choice)
#remethod.Bind(wx.Choice)
filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbix = wx.BoxSizer()
hbix.Add(remethod, proportion=0.5, flag=wx.EXPAND)
hbix.Add(filename, proportion=1, flag=wx.EXPAND)
hbix.Add(loadbutton, proportion=0, flag=wx.LEFT, border=5)
hbix.Add(saveButton, proportion=0, flag=wx.RIGHT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbix, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()