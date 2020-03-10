from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class AppCommon:
    # 判断是否有权限弹窗
    def handle_permision(self, driver):
        for i in range(5):
            loc = ("xpath", "//*[@text='始终允许']")
            try:
                e = WebDriverWait(driver).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass