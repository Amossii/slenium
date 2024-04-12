from selenium import webdriver
from selenium.webdriver.common.by import By
wd = webdriver.Chrome()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://cdn2.byhy.net/files/selenium/test3.html')

element = wd.find_element(By.ID, 'input1')
element.clear()
element.send_keys('ROSS')


input('等待回车键结束程序')