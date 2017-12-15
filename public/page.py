#coding=utf-8
'''页面定位信息维护'''
from selenium.webdriver.common.by import By

class Login(object):
    username=[By.ID,'username']
    password=[By.ID,'password']
    loginbtn=[By.ID,'login-btna']

class pageZhuce(object):
    #服务管理
    fwgl=[By.XPATH,".//*[@id='topNavBar']/li[1]/a"]
    fwgl_iframe="viewFrame"

    #“注册”按钮定位
    zhuce=[By.XPATH,".//*[@id='shangbao']/a[1]"]
    zhuce_iframe="viewFrame"

    #“注册”页面元素定位
    ms_name=[By.ID,'ms_name']
    ms_type=[By.ID,'ms_type']
    ms_version=[By.ID,'ms_version']
    dev=[By.ID,'dev']
    ms_test_url = [By.ID, 'ms_test_url']
    checkHeartBtn = [By.ID, 'checkHeartBtn']
    ms_desc_url = [By.ID, 'ms_desc_url']
    checkBtn = [By.XPATH, ".//*[@id='checkHeartBtn']/i"]
    ms_desc = [By.ID, 'ms_desc']

    save_btn=[By.ID,'saveBtn']
    calcleBtn=[By.ID,'calcleBtn']