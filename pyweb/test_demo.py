from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains
from selenium.webdriver import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, json


class TestDemoAssert():
    def setup(self, m=2):
        driver = webdriver.ChromeOptions()
        if m == 1:
            driver.add_argument("--headless")
        elif m == 2:
            # driver.debugger_address = "127.0.0.1:9222"
            driver = Options()
            driver.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=driver)

    def teardown(self):
        self.driver.quit()
        pass

    def test_assert(self):
        self.driver.get("https://ceshiren.com/")
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.LINK_TEXT, '所有分类')).click().perform()
        # 断言
        time.sleep(2)
        element = self.driver.find_element(By.LINK_TEXT, '所有分类').get_attribute("class")
        assert 'active' == element

    def test_getCooke(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        with open("cookies.txt", 'w', encoding="utf-8") as f:
            f.write(json.dumps(cookies))

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")

    def test_addcooke(self):
        with open('./cookies.txt','r',encoding='utf-8') as f:
            cookies = json.loads(f.read())

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh() # 刷新页面
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
