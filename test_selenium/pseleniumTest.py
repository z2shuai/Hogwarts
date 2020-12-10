import time

from selenium import webdriver
import pytest, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待5s
        # wait = WebDriverWait(self.driver,5)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()
        pass

    def test_selenium(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()

        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_css_selector('#TANGRAM__PSP_4__userName').send_keys("zgd_ceshiren")
        self.driver.find_element_by_css_selector('#TANGRAM__PSP_4__phone').send_keys(18292733135)
        time.sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        # self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('15691906882')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('15691906882')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('Mm2shuai')

        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()


if __name__ == "__main__":
    pytest.main(['pseleniumTest.py', '-v', '-s'])
