import pytest
import pytest
import unittest
import os
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appcommon.common import AppCommon
from appcommon.config import Config
from loguru import logger


class TestTest(unittest.TestCase):
    def test_vipshop_test(self):
        logger.info("开始执行测试用例！！！！")
        server = 'http://localhost:4723/wd/hub'
        desired_capabilities = Config().get_device_config()
        logger.info("获取到的设备参数为：%s" % desired_capabilities)
        driver = webdriver.Remote(server, desired_capabilities)

        # wait = WebDriverWait(driver, 10)
        AppCommon().handle_permision(driver)

        # wait = WebDriverWait(driver, 10)
        time.sleep(5)
        # driver.find_element_by_accessibility_id("com.android.permissioncontroller:id/permission_allow_always_button").click()
        #
        # time.sleep(5)
        # # driver.find_element_by_id('com.xiangchao.starspace:id/skip').click()

        # driver.quit()

        # mActivityComponent = com.eg.android.AlipayGphone / com.alipay.mobile.security.login.ui.AlipayUserLoginActivity
        # mActivityComponent = com.eg.android.AlipayGphone /.AlipayLogin