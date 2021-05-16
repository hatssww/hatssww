import time

from selenium import webdriver
import urllib.request

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
driver.find_element_by_css_selector("div:nth-child(1) > div > label > input").send_keys('ID')
# 비밀번호 입력
time.sleep(1.0)
driver.find_element_by_css_selector("div:nth-child(2) > div > label > input").send_keys('PW')
# 로그인
time.sleep(1.0)
driver.find_element_by_css_selector("div:nth-child(3) > button").click()

# https://www.instagram.com/hatssww/ 접속
time.sleep(7)
driver.get('https://www.instagram.com/hatssww/')


# 웹 페이지 가장 밑으로 스크롤
# scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight 까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # scrollHeight 비교
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 작은 이미지 선택하기
images = driver.find_elements_by_css_selector(".FFVAD")

# 이미지 저장하기
count = 1
b = 0
for i in range(len(images) + 1):
    try:
        time.sleep(3)
        i += 1
        if i % 3 == 1:
            a = 1
            b += 1
        elif i % 3 == 2:
            a = 2
        else:
            a = 3
        
        imgUrl = driver.find_element_by_css_selector(f"#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child({b}) > div:nth-child({a}) > a > div > div.KL4Bh > img").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count += 1
    except:
        pass

driver.close()