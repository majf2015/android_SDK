#coding=utf-8
#emulator -avd test431
#E:\windows-x86-SDK\sdk\tools
#monkeyrunner test.py



import sys
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as  mi

class MyMonkeyrunner:
    def __init__(self):
        self.device = None
        self.apk_url = 'E:/windows-x86-SDK/sdk/platform-tools/9358mgr_v2.5.1.12_xiaomodo_201602021454.apk'
        self.apk_name_activity = "com.xmd.manager/com.xmd.manager.window.LoginActivity"
        self.shot = 5


    def connect_device(self):
        self.device = mr.waitForConnection(2.0)
        if not self.device:
            print "connect error"
        else:
            print "connect success"

    def install_apk(self):
        self.device.installPackage(self.apk_url)

    def start_activity(self):
        self.device.startActivity( component=self.apk_name_activity )
        print "start_activity"
        mr.sleep(10.0)

    def do_something(self):
        #self.device.type('helloworld')
        self.device.press('KEYCODE_HOME', md.DOWN_AND_UP)
        print "do_something"
        mr.sleep(3.0)

    def take_screem(self):
        mr.sleep(3.0)
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






