
class Config:
    def get_device_config(self):
        desired_capabilities = {"platformName": "Android",
            # "automationName": "UiAutomator2",
            "platformVersion": "10",
            "deviceName": "Honor 10 Lite",
            "appPackage": "com.achievo.vipshop",
            "appActivity": "com.achievo.vipshop.acuy7tivity.LodingActivity"}
            # 'appPackage': "com.eg.android.AlipayGphone",
            # 'appActivity': "com.eg.android.AlipayGphone.AlipayLogin'}
            # 'appPackage': 'com.gotokeep.keep',
            # 'appActivity': 'com.gotokeep.keep.splash.SplashActivity'}\
        return desired_capabilities