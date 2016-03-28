#coding=utf-8
import sys
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md

from com.android.monkeyrunner.easy import EasyMonkeyDevice as emd
from com.android.monkeyrunner.easy import By
#from com.android.monkeyrunner import MonkeyImage as  mi
import os

class MyMonkeyrunner:
    def __init__(self):
        self.device = None
        self.easy_device = None
        self.apk_url = 'E:/windows-x86-SDK/sdk/platform-tools/9358mgr_v2.5.1.12_xiaomodo_201602021454.apk'
        self.apk_name_activity = "com.xmd.manager/com.xmd.manager.window.LoginActivity"
        self.tool = 'E:/windows-x86-SDK/sdk/tools'
        self.shot = 0


    def connect_device(self):
        self.device = mr.waitForConnection(2.0)
        self.easy_device = emd(self.device)
        if not self.device:
            print "connect error"
        else:
            print "connect success"

    def install_apk(self):
        self.device.installPackage(self.apk_url)

    def start_activity(self):
        self.device.startActivity( component=self.apk_name_activity )
        print "start_activity"
        mr.sleep(1.0)

    def do_something(self):
        #self.device.type('helloworld')
        self.easy_device.touch(By.id('id/username'),md.DOWN_AND_UP)
        text = self.easy_device.getText(By.id('id/username'))
        self.device.press('KEYCODE_MOVE_END', md.DOWN_AND_UP)
        for i in range(len(text)):
            self.device.press('KEYCODE_DEL', md.DOWN)
        self.device.type('93')
        self.easy_device.touch(By.id('id/password'),md.DOWN_AND_UP)
        self.device.type('123456')
        self.easy_device.touch(By.id('id/login'),md.DOWN_AND_UP)
        print "do_something"

    def take_screem(self):
        os.chdir(self.tool)
        mr.sleep(1.0)
        result = self.device.takeSnapshot()
        result.writeToFile('./shot%d.png'% self.shot,'png')
        self.shot += 1

    def main(self):
        self.connect_device()
        #self.take_screem()
        #self.install_apk()
        #self.take_screem()
        self.start_activity()
        #self.take_screem()
        self.do_something()
        #self.take_screem()

test = MyMonkeyrunner()
test.main()






