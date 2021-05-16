import yaml
from selenium.webdriver.common.by import By
from test_frame_homework.base_page import BasePage
from test_frame_homework.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search_page(self):
        #yaml 的读取
        with open("../page/market_page.yaml", "r", encoding='utf-8') as f:
            data = yaml.load(f)
            #遍历每一个动作
            for step in data:
                action = step["action"]
                #如果动作是find_and_click，就调用basepage中的find_and_click
                if action == "find_and_click":
                    #调用find_and_click并且传入参数
                    self.find_and_click(step["locator"])
        # self.find_and_click((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)

