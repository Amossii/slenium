from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID, 'kw')

element.send_keys('通讯\n')


# 返回页面 ID为1 的元素
element = wd.find_element(By.CSS_SELECTOR,'[_nk="wmpB52"]')

element.click()

username=wd.find_element(By.CSS_SELECTOR,'[placeholder="手机号"]')
password=wd.find_element(By.CSS_SELECTOR,'[type="password"]')

username.send_keys('15097550885')
password.send_keys('okklkxmyt@66')

submit=wd.find_element(By.CSS_SELECTOR,'.lb-login-box-con-submit')
submit.click()

# 打印该元素的文字内容
print(element.text)