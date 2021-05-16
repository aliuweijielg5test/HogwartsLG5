import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_frame_homework.handle_black import handle_black


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver
    #查找元素操作
    @handle_black
    def find(self,locator):
        black_lists = [(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/iv_close']")]
        #捕获异常（元素没找到）
        try:
            result = self.driver.find_element(*locator)
            return result
        except Exception as e:
            #遍历黑名单
            for black in black_lists:
                #如果发现黑名单中的元素存在
                eles = self.driver.find_elements(*black)
                #对其进行处理
                if len(eles)>0:
                    #通过点击的方式，关闭弹窗
                    eles[0].click()
                    return self.find(locator)
            raise e

    def send(self,locator,content):
         self.find(locator).send_keys(content)
    #鼠标点击操作
    def find_and_click(self,locator):
        self.find(locator).click()
    #鼠标点击滑动操作
    def scroll_find_click(self,text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find_and_click(element)
    #获取文本操作
    def find_and_get_text(self,locator):
        return self.find(locator).text




