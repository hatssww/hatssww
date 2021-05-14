import time

from selenium import webdriver
import requests


# 웹드라이버 생성
driver = webdriver.Chrome('C:/Users/USER/chromedriver_win32/chromedriver', options=options)
driver.implicitly_wait(3)

# https://www.instagram.com/accounts/login/ 접속
time.sleep(1)
driver.get('https://www.instagram.com/accounts/login/')


# ID 입력
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys('ID')
# 비밀번호 입력
time.sleep(1.5)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys('PW')
# 로그인
time.sleep(1.5)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div").click()