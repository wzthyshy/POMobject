from selenium import webdriver
from selenium.webdriver.common.by import By

# 登录页面对象
from base_page.base import BasePage

'''
    登录页面的对象，就是登录的流程
    1：获取登录中的元素
    2：对元素进行操作
'''


class Loginpage(BasePage):
    # 获取页面元素
    username = (By.ID, 'loginname')
    password = (By.ID, 'password')
    login_code = (By.XPATH, '//*[@id="code"]')
    click_el = (By.XPATH, '//*[@id="to-recover"]')

    # 页面URL
    url = 'http://18h236a233.imwork.net:13257/FHMYSQL/'

    # 元素操作进行封装
    def input_username(self, name):
        self.locator(self.username).send_keys(name)

    def input_password(self, psw):
        self.locator(self.password).send_keys(psw)

    def input_code(self, code):
        self.locator(self.login_code).send_keys(code)

    def click(self):
        self.locator(self.click_el).click()

    # 测试代码
    def test_case(self, name, psw, code):
        self.open()
        self.input_username(name)
        self.input_password(psw)
        self.input_code(code)
        self.click()
        self.quit()


# 页面对象执行

if __name__ == '__main__':
    driver = webdriver.Chrome()
    name = '超级权限'
    psw = '123456'
    code = '0000'
    sp = Loginpage(driver, Loginpage.url)
    sp.test_case(name, psw, code)
