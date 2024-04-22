from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
user_dir=r'C:\Users\50438\AppData\Local\Google\Chrome\User Data'

user_option = webdriver.ChromeOptions()
#添加浏览器用户数据
user_option.add_argument(f'--user-data-dir={user_dir}')

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'),options=user_option)
wd.implicitly_wait(30)

wd.get('https://www.chatgptok.com/chat?sessionid=1778799307181903873')


problems=[]
with open('../dataset/ultra_problems1.txt','r',encoding='utf-8') as file:
    line=file.readline()
    while line:
        problems.append(line.strip('\n'))
        line=file.readline()


with open('answer2.txt','w',encoding='utf-8') as file:
    for problem in problems:
        text = wd.find_element(By.CSS_SELECTOR, '[placeholder="输入任意问题，Chat3.5将给你答案"]')
        text.send_keys(problem)
        sleep(2)
        submit=wd.find_element(By.CLASS_NAME,'icon-fasong1')
        submit.click()
        sleep(20)
        answers=wd.find_elements(By.CSS_SELECTOR,'.chatAIText-answer')
        answer =answers[-1]

        answer_txts=answer.find_elements(By.CSS_SELECTOR,'ol > li')

        file.write(problem+'\n')
        i=0
        for answer_txt in answer_txts:
            txt=answer_txt.text.strip('"')
            file.write(str(i)+'.'+txt+'\n')
            print(str(i)+'.'+txt)
            i+=1
        file.write('\n')



input()