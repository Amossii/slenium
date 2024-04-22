from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
user_dir=r'C:\Users\50438\AppData\Local\Google\Chrome\User Data'

user_option = webdriver.ChromeOptions()
#添加浏览器用户数据
user_option.add_argument(f'--user-data-dir={user_dir}')

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'),options=user_option)


wd.get('https://tieba.baidu.com/p/8989876196?fid=20991085&pid=150160106294&cid=0#150160106294')

text=wd.find_element(By.CSS_SELECTOR,'#ueditor_replace>p')
text.send_keys(u'D:\Python\slenium\\tieba\sources\OIP-C.jpg')

submit=wd.find_element(By.CSS_SELECTOR,'[title="Ctrl+Enter快捷发表"]')
submit.click()

