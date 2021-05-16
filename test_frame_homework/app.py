from appium import webdriver
from test_frame_homework.base_page import BasePage
from test_frame_homework.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            desired_caps = {
                "platformName": "Android",
                "platformVersion": "6.0",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": "common.MainActivity",
                "unicodeKeyboard": "True",
                "resetKeyboard": "True",
                "noReset": "True"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)


