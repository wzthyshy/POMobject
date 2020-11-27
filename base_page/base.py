from time import sleep

from selenium import webdriver
import unittest
# 基类
'''
    基类：在所有的页面中，都有一些公共的内容需要执行
    1：定位元素
    2：启动浏览器，访问页面URL
    3：关闭浏览器，释放资源
'''
class BasePage(object):
    driver = webdriver.Chrome()

    # 构造函数
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
    # 定位元素；考虑对定位的元素进行操作，所以需要返回值
    def locator(self, loc):
        return self.driver.find_element(*loc)
        # 实例化元素定位的方式并返回，方便testcase中元素定位来使用

    # 访问URl
    def open(self ):
        self.driver.get(self.url)

    # 关闭浏览器，释放资源
    def quit(self):
        sleep(2)
        self.driver.quit()



























