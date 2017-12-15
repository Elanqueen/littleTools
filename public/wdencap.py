#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

class SeEncap(object):
    ''' 封装了selenium2的部分方法'''

    def __init__(self, browser="ff"):
        '''
        Run class initialization method, the default is proper
        to drive the Firefox browser. Of course, you can also
        pass parameter for other browser, Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        '''
        if browser == "firefox" :
            self.driver = webdriver.Firefox()
        elif browser == "chrome" or browser == "ff":
            self.driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == "opera":
            self.driver = webdriver.Opera()
        elif browser == "chrome_headless":
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise NameError(
                "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'edge', 'chrome' or 'chrome_headless'." % browser)

#============================页面等待==============================

    def element_wait(self,cls,secs=5):
        WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((cls[0],cls[1])))

    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    # =========================打开页面==============================

    def open(self,url):
        self.driver.get(url)

    def max_window(self):
        self.driver.maximize_window()

    def set_window_size(self,wight,hight):
        self.driver.set_window_size(wight,hight)

#==========================定位元素=====================================

    def get_element(self,cls):
        '''定位单一元素
        cls为传入的定位元素元祖，格式为[定位方式,定位元素]，例如：[By.ID,'loginform-username']
        可定位的方式支持：ID,NAME,XPATH,CLASS,LINK_TEXT,
        '''
        element = self.driver.find_element(cls[0],cls[1])
        return element

    def get_elements(self,cls):
        #待继续完善
        '''定位一组元素，返回所有元素
            cls为传入的定位元素元祖，格式为[定位方式,定位元素]，例如：[By.ID,'loginform-username']
            可定位的方式支持：ID,NAME,XPATH,CLASS,LINK_TEXT,
        '''
        elements = self.driver.find_element(cls[0], cls[1])
        return elements

#============================操作元素===============================

    def type(self,cls,text):
        self.element_wait(cls)
        el=self.get_element(cls)
        el.send_keys(text)

    def element_click(self,el):
        el.click()

    def click(self,cls):
        self.element_wait(cls)
        el=self.get_element(cls)
        el.click()

    def right_click(self, css):
        '''
        Right click element.

        Usage:
        driver.right_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def clear(self,cls):
        self.element_wait(cls)
        el = self.get_element(cls)
        el.clear()

    def move_to_element(self, css):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        '''
        Double click element.

        Usage:
        driver.double_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):
        '''
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        '''
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        '''
        self.driver.find_element_by_partial_link_text(text).click()

    def submit(self, css):
        '''
        Submit the specified form.

        Usage:
        driver.submit("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.submit()

#============================下拉框选择=================================
    def element_select(self,cls,type,value=2):
        '''勾选下拉框内容
        根据三种方式选择：index-----依据数字，例：1,2,3
                         visible_text-----依据显示的文字，例：“text”
                         value------依据value属性
        '''
        select=Select(self.get_element(cls))
        if (type=="index"):
            select.select_by_index(value)
        elif (type=="visible_text"):
            select.select_by_visible_text(value)
        elif (type=="value"):
            select.select_by_value(value)

    def element_deselect(self,cls,type,value):
        '''取消下拉框勾选操作'''
        select = Select(self.get_element(cls))
        if (type == 'index'):
            select.deselect_by_index(value)
        elif (type == 'visible_text'):
            select.deselect_by_visible_text(value)
        elif (type == 'value'):
            select.dedeselect_by_value(value)



#===========================获取页面元素================================

    def get_text(self,cls):
        '''获取文本'''
        self.element_wait(cls)
        el=self.get_element(cls)
        return el.text

    def get_url(self):
        '''获取当前页面地址'''
        return self.driver.current_url

    def get_attribute(self,cls,attribute):
        '''获取元素属性'''
        el=self.get_element(cls)
        return  el.get_attribute(attribute)

    def get_windows_img(self, file_path):
        '''
        Get the current window screenshot.

        Usage:
        driver.get_windows_img()
        '''
        self.driver.get_screenshot_as_file(file_path)

    #==========================判断元素可见、已选、可用=======================

    def element_display(self,cls):
        '''查看元素是否可见，返回ture/false'''
        self.element_wait(cls)
        el=self.get_element(cls)
        return  el.is_displayed()

    def element_selected(self,cls):
        '''查看元素是否已经选中，返回ture/false'''
        self.element_wait(cls)
        el = self.get_element(cls)
        return el.is_selected()

    def element_enabled(self,cls):
        '''查看元素是否可用，返回ture/false'''
        self.element_wait(cls)
        el = self.get_element(cls)
        return el.is_enabled()

    #=======================切换窗口=================================

    def switch_to_new_window(self):
        current_handle=self.driver.current_window_handle
        handles=self.driver.window_handles
        for handle in handles:
            if handle !=current_handle:
                self.driver.switch_to.window(handle)


#==========================处理警告框===============================
    def accept_alert(self):
        '''切换到弹窗页面'''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''忽略警告弹窗'''
        self.driver.switch_to.alert.dismiss()

#==========================切换到iframe=========================
    def switch_to_frame(self,cls):
        '''切换到iframe
        定位元素可以是：id,name,tag_name,
                      例： driver.switch_to.frame("frame1")  # 2.用id来定位
                           driver.switch_to.frame("myframe")  # 3.用name来定位
                           driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        也可以通过index和WebElement来定位，
                      例：
                          index从0开始，传入整型参数即判定为用index定位，传入str参数则判定为用id/name定位
                          WebElement对象，即用find_element系列方法所取得的对象，我们可以用tag_name、xpath等来定位frame对象
                      <iframe src="myframetest.html" />
                       则，
                      driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'myframe')]"))

        '''
        self.driver.switch_to.frame(cls)  #仅用于第一种定位方式

    def switch_to_parent_frame(self):
        '''从frame2切回frame1'''
        self.driver.switch_to.parent_frame()

    def switch_to_frame_out(self):
        '''从frame切换回主页面'''
        self.driver.switch_to.default_content()

#============================页面刷新============================

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    #================================关闭页面=================================

    def close(self):
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        '''
        self.driver.quit()


if __name__=='__main__':
    SeEncap("chrome")