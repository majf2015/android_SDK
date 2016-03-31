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
        self.apk_url = 'E:/windows-x86-SDK/sdk/platform-tools/9358mgr_v2.5.3.12_xiaomodo_201603181025.apk'
        self.apk_name_activity = "com.xmd.manager/com.xmd.manager.window.LoginActivity"
        self.tool = 'E:/windows-x86-SDK/sdk/tools'
        self.count = ['93', '123456']
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

    def case_login(self):
        self.device.startActivity( component=self.apk_name_activity )
        mr.sleep(3.0)
        #self.device.type('helloworld')
        self.easy_device.touch(By.id('id/username'),md.DOWN_AND_UP)
        text = self.easy_device.getText(By.id('id/username'))
        self.device.press('KEYCODE_MOVE_END', md.DOWN_AND_UP)
        for i in range(len(text)):
            self.device.press('KEYCODE_DEL', md.DOWN)
        self.device.type(self.count[0])
        self.easy_device.touch(By.id('id/password'),md.DOWN_AND_UP)
        self.device.type(self.count[1])
        self.easy_device.touch(By.id('id/login'),md.DOWN_AND_UP)
        print "case_login"

    def case_order_manage(self):
        mr.sleep(1.0)
        self.easy_device.touch(By.id("id/order_manage"),md.DOWN_AND_UP)
        self.easy_device.touch(By.id("id/toolbar_back"), md.DOWN_AND_UP)
        print "case_order_manage"

    def case_coupon_consume(self):
        mr.sleep(1.0)
        self.easy_device.touch(By.id("id/coupon_consume"), md.DOWN_AND_UP)
        self.easy_device.touch(By.id("id/toolbar_back"), md.DOWN_AND_UP)
        print "case_coupon_consume"

    def case_statistics(self):
        mr.sleep(1.0)
        self.easy_device.touch(By.id("id/statistics"), md.DOWN_AND_UP)
        mr.sleep(1.0)
        self.easy_device.touch(By.id("id/dialog_positive"), md.DOWN_AND_UP)
        print "case_statistics"

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
        self.case_login()
        self.case_order_manage()
        self.case_coupon_consume()
        self.case_statistics()
        #self.take_screem()

test = MyMonkeyrunner()
test.main()






