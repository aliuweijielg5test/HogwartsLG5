import yaml
from selenium.webdriver.common.by import By

from test_frame_homework.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        with open("../page/search_page.yaml", "r", encoding='utf-8') as f:
            data = yaml.load(f)
            # 遍历每一个动作
            for step in data:
                action = step["action"]
                # 如果动作是find_and_click，就调用basepage中的find_and_click
                if action == "find_and_click":
                    # 调用find_and_click并且传入参数
                    self.find_and_click(step["locator"])
                elif action == "send":
                    self.send(step["locator"],step["content"])
        # self.send((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']"),"alibaba")
        # self.find_and_click((By.XPATH,"//*[@text='阿里巴巴-SW']"))
        return True

