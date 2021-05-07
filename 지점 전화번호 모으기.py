import requests
from bs4 import BeautifulSoup

# HTML코드 받아오기
response = requests.get("https://workey.codeit.kr/orangebottle/index")
html_code = response.text

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(html_code, 'html.parser')

# "div.container" 클래스를 가진 태그에 중첩된 모든 <span> 태그 선택
span_tags = soup.select("div.container span")
# body > div.container > div:nth-child(1) > span
# body > div.container > div:nth-child(2) > span

# 빈 리스트 생성
phone_numbers = []

# 번호 추출해서 리스트에 담기
for span in span_tags:
    phone_numbers.append(span.text)
    
# 결과 출력
print(phone_numbers)