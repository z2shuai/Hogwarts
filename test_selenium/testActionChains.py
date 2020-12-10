import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time


class TestActionChains():
    def setup(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()
        # 显式等待
        self.wait = WebDriverWait(self.driver, 10)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.skip
    def test_Action_lx(self):
        # 加载指定URL地址
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 切换 frame 窗口
        self.driver.switch_to.frame('iframeResult')
        # 获取两个节点对象
        drag = self.driver.find_element(By.ID, 'draggable')
        drop = self.driver.find_element(By.ID, 'droppable')
        # 实施拖拽操作
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        alert = self.driver.switch_to.alert
        # 解散现有alert弹框
        alert.dismiss()
        # print(alert.text)
        # alert.accept()
        # 切换至默认frame窗口
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '//*[contains(@class,"btn btn-success")]').click()

    @pytest.mark.skip
    def test_file_sc(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.ID, 'sttb').click()
        self.driver.find_element(By.ID, 'stfile').send_keys("/Users/fg/Desktop/Yoyo/timg2.jpeg")

    # def test_js1(self):
    #     self.driver.get("http://www.baidu.com")
    #     kw = self.driver.execute_script("return document.getElementById('kw')").send_keys("slect")
    #     # self.driver.find_element(By.ID,'kw').send_keys("selenium execute")
    #     ele = self.driver.execute_script("return document.getElementById('su')")
    #     ele.click()
    #     self.driver.execute_script("document.documentElement.scrollTop=100000")
    #     time.sleep(3)
    #     self.driver.find_element(By.CSS_SELECTOR,'#page > div > a.n').click()

    def test_js2(self):
        self.driver.get("https://www.12306.cn/index/")
        # js = "document.getElementById('train_date').removeAttribute('readonly')"
        # self.driver.execute_script(js)
        js2 = "a=document.getElementById('train_date');a.removeAttribute('readonly')"
        self.driver.execute_script(js2)
        time.sleep(2)
        self.driver.execute_script("document.getElementById('train_date').value='2020-11-11'")
        print(self.driver.execute_script(("return document.getElementById('train_date').value")))
