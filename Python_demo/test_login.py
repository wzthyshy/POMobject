'''
时间：20201125
作者：王泽
功能：登录企业微信
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testlogin:
    def test_loin_debug(self):
        option = Options()
        option.debugger_address = 'localhost:49677'
        driver = webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/")


