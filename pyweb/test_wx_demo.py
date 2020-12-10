import json
import shelve
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestWxDemo():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.db = shelve.open('cookies')
        self.cookies = self.db.get('cookies', None)
        if self.cookies == None:
            with open('./cookies.txt', 'r', encoding='utf-8') as f:
                self.db['cookies'] = json.loads(f.read())
            self.cookies = self.db.get('cookies')
        self.db.close()

    def teardown(self):
        time.sleep(1)
        self.driver.quit()

    def test_wx_demo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in self.cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.refresh()

        """# 此路没通
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar .ww_btn_PartDropdown_left[0]").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".qui_dropdownMenu_itemLink.ww_dropdownMenu_itemLink.js_import_member[1]").click()
        """

        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)'))).click()
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.ww_fileImporter_fileContainer_uploadInputMask"))). \
            send_keys("/Users/fg/Desktop/通讯录批量导入模板.xlsx")

        # 获取上传成功的文件名称,检测文件是否上传成功
        # filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        filename = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames'))).text
        # 断言上传文件是否成功
        assert filename == "通讯录批量导入模板.xlsx"

        # self.driver.find_element(By.CSS_SELECTOR,
        #                          '.qui_btn.ww_btn.ww_btn_Large.ww_btn_Blue.ww_fileImporter_submit').click()
        # time.sleep(5)
