import yaml
from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import WebDriver

def handle_black(fun):
    def run(*args,**kwargs):
        instance = args[0]
        with open("../black_list.yaml","r", encoding="utf-8") as f:
            black_list =yaml.safe_load(f)
        # 捕获异常  （元素没有找到）
        try:
            return fun(*args,**kwargs)
        except Exception as e:
            # 遍历黑名单
            for black in black_list:
                # 如果发现黑名单中的元素存在
                elements = instance.driver.find_elements(*black)
                # 对黑名单中的元素进行处理
                if len(elements) > 0:
                    elements[0].click()
                    # 再次查找
                    return fun(*args, **kwargs)
            raise e
    return run
