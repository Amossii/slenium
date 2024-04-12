
archive=wd.find_element(By.CLASS_NAME,'icon-mulu31')
archive.click()

login=wd.find_element(By.ID,'code-login')
login.click()

# pw = wd.find_element(By.CLASS_NAME,'way-choose')
# pw.click()

username=wd.find_element(By.CSS_SELECTOR,'[placeholder="手机号"]')
# password=wd.find_element(By.CSS_SELECTOR,'[type="6位短信验证码"]')

username.send_keys('15097550885')
# password.send_keys('okklkxmyt@66')

submit=wd.find_element(By.CSS_SELECTOR,'.lb-login-box-con-submit')
submit.click()



#
# password=wd.find_element(By.CSS_SELECTOR,)