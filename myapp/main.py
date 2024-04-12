from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
user_dir=r'C:\Users\50438\AppData\Local\Google\Chrome\User Data'

user_option = webdriver.ChromeOptions()
#添加浏览器用户数据
user_option.add_argument(f'--user-data-dir={user_dir}')

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'),options=user_option)

wd.implicitly_wait(10)
wd.get('https://www.chatgptok.com/chat?sessionid=1778799307181903873')

text=wd.find_element(By.CSS_SELECTOR,'[placeholder="输入任意问题，Chat3.5将给你答案"]')
text.send_keys('请给出关于国际金融的五个诱导性问题')

sleep(3)

submit=wd.find_element(By.CLASS_NAME,'icon-fasong1')
submit.click()

answers=wd.find_elements(By.CSS_SELECTOR,'.chatAIText-answer p')
for answer in answers:
    print(answer.text)



input()