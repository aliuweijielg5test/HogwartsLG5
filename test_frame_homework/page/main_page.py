from time import sleep

import yaml
from selenium.webdriver.common.by import By
from test_frame_homework.base_page import BasePage
from test_frame_homework.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        with open("../page/main_page.yaml", "r", encoding='utf-8') as f:
            data = yaml.load(f)
            # 遍历每一个动作
            for step in data:
                action = step["action"]
                # 如果动作是find_and_click，就调用basepage中的find_and_click
                if action == "find_and_click":
                    # 调用find_and_click并且传入参数
                    self.find_and_click(step["locator"])
        # self.find_and_click((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        # sleep(5)
        # self.find_and_click((By.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)
