#coding=utf-8
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'public')))
from public import constant
from public.wdencap import SeEncap
from public.page import pageZhuce
from public.page import Login

import unittest
import xml.dom.minidom


#获取xml文件中的参数
dom = xml.dom.minidom.parse(constant.LOGUP)
root = dom.documentElement
def get_xml_attribute(name,number=0,attribute='text'):
    dots = root.getElementsByTagName(name)
    text = dots[number].getAttribute(attribute)
    return text

class LogIn(unittest.TestCase,SeEncap):
    '''【服务管理】-【注册】页面的表单填充功能
        不能进行文件和图片的上传
    '''
    dr=SeEncap()
    def setUp(self):
        self.dr.open(constant.LOGIN_URL)
        self.dr.max_window()
        self.dr.wait(5)
        #登录
        self.dr.type(Login.username,get_xml_attribute('username'))
        self.dr.type(Login.password,get_xml_attribute('password'))
        self.dr.click(Login.loginbtn)

    def test_typein(self):
        self.dr.element_wait(pageZhuce.fwgl)
        self.dr.click(pageZhuce.fwgl)
        self.dr.wait(20)
        self.dr.switch_to_frame(pageZhuce.fwgl_iframe)
        self.dr.wait(5)
        self.dr.click(pageZhuce.zhuce)

        self.dr.type(pageZhuce.ms_name,get_xml_attribute('ms_name'))
        self.dr.type(pageZhuce.ms_version,get_xml_attribute('ms_version'))
        self.dr.type(pageZhuce.ms_test_url,get_xml_attribute('ms_test_url'))
        self.dr.click(pageZhuce.ms_test_url)
        self.dr.wait(3)
        self.dr.type(pageZhuce.ms_desc_url,get_xml_attribute('ms_desc_url'))

        #选择服务类型，select
        self.dr.element_select(pageZhuce.ms_type,"index")
        self.dr.switch_to_frame_out()

    def tearDown(self):
        pass

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(LogIn("test_typein"))

    runner = unittest.TextTestRunner()
    runner.run(suite)



