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
        self.data = ['93', '123456', ]
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
        print "install apk success"

    def case_login(self):
        self.device.startActivity( component=self.apk_name_activity )
        mr.sleep(3.0)
        self.easy_device.touch(By.id('id/username'),md.DOWN_AND_UP)
        text = self.easy_device.getText(By.id('id/username'))
        self.device.press('KEYCODE_MOVE_END', md.DOWN_AND_UP)
        for i in range(len(text)):
            self.device.press('KEYCODE_DEL', md.DOWN)
        self.device.type(self.data[0])
        self.easy_device.touch(By.id('id/password'),md.DOWN_AND_UP)
        self.device.type(self.data[1])
        self.easy_device.touch(By.id('id/login'),md.DOWN_AND_UP)
        print "case_login"

    def case_order_drag(self):
        mr.sleep(2.0)
        self.easy_device.touch(By.id("id/order_manage"),md.DOWN_AND_UP)
        for i in range(3):
            self.device.drag((190, 770), (190, 130),0.1,  5)
            mr.sleep(1.0)
        for i in range(5):
            self.device.drag((190, 130), (190, 770),0.1,  5)
        print "case_order_drag"

    def case_order_accept(self):
        mr.sleep(1.0)
        self.easy_device.touch(By.id("id/accept"),md.DOWN_AND_UP)
        #self.easy_device.touch(By.id("id/toolbar_back"), md.DOWN_AND_UP)
        print "case_order_accept"

    def case_order_complete(self):
        mr.sleep(1.0)
        self.easy_device.touch(By.id("id/complete"),md.DOWN_AND_UP)
        print "case_order_complete"

    def case_order_failure(self):
        mr.sleep(1.0)
        self.easy_device.touch(By.id("id/failure"),md.DOWN_AND_UP)
        mr.sleep(1.0)
        self.device.touch(400,222,md.DOWN_AND_UP)
        print "case_order_failure"

    def case_order_reject(self):
        mr.sleep(1.0)
        self.easy_device.touch(By.id("id/reject"),md.DOWN_AND_UP)
        mr.sleep(1.0)
        self.device.touch(357,494,md.DOWN_AND_UP)
        print "case_order_reject"

    def case_order_select(self, s):
        mr.sleep(1.0)
        self.easy_device.touch(By.id("id/toolbar_right"),md.DOWN_AND_UP)
        mr.sleep(1.0)
        if s == "order":
            self.device.touch(400,222,md.DOWN_AND_UP)
        elif s == "accepted":
            self.device.touch(400,293,md.DOWN_AND_UP)
        print "case_order_select"

    def case_coupon_consume(self):
        mr.sleep(1.0)
        self.easy_device.touch(By.id("id/coupon_consume"), md.DOWN_AND_UP)
        self.easy_device.touch(By.id("id/rl_manually_consume"), md.DOWN_AND_UP)
        self.easy_device.touch(By.id("id/coupon_consume_phone"), md.DOWN_AND_UP)
        self.device.type(self.data[2])
        self.easy_device.touch(By.id("id/btn_manually_consume"), md.DOWN_AND_UP)
        self.easy_device.touch(By.id("id/coupon_name"), md.DOWN_AND_UP)
        self.easy_device.touch(By.id("id/coupon_use"), md.DOWN_AND_UP)
        self.easy_device.touch(By.id("id/dialog_positive"),md.DOWN_AND_UP)
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

        #self.case_login()
        #self.case_order_drag()
        #self.case_order_select("order")
        #self.case_order_accept()
        #self.case_order_accept()
        #self.case_order_select("accepted")
        #self.case_order_complete()
        #self.case_order_failure()
        #self.case_order_select("order")
        #self.case_order_reject()

        self.case_coupon_consume()
        #self.case_statistics()
        #self.take_screem()

test = MyMonkeyrunner()
test.main()
#



