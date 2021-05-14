import time

from selenium import webdriver
import requests


# USB기기 관련 문제시 추가 설정 옵션
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

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


# https://www.instagram.com/hatssww/ 접속
time.sleep(10)
driver.get('https://www.instagram.com/hatssww/')


# 웹 페이지 가장 밑으로 스크롤
# scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight 까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # scrollHeight 비교
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# 첫번째 게시물 선택
first_img_css="div.v1Nh3.kIKUG._bz0w"
driver.find_element_by_css_selector(first_img_css).click()


# 이미지 url 저장
img_object_css = "article > div._97aPb > div > div > div.KL4Bh > img"
img_object = driver.find_element_by_css_selector(img_object_css)
img_url = img_object.get_attribute("src")

# 이미지 저장할 경로 정의
img_path = 'C:/Users/USER/Desktop/my_images/' + '1.jpg'

# requests 패키지로 이미지 다운로드
response = requests.get(img_url)
if response.status_code == 200:
    with open(img_path, 'wb+') as f:
        f.write(response.content)