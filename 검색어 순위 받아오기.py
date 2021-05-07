import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

# HTML코드 받아오기
response = requests.get("https://workey.codeit.kr/music/index")
html_code = response.text

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(html_code, 'html.parser')

# "rank__order" 클래스를 가진 태그에 중첩된 모든 <li> 태그 선택
li_tags = soup.select(".rank__order li")

# 빈 리스트 생성
search_ranks = []

# 검색어 추출해서 리스트에 담기
for li in li_tags:
    search_ranks.append(li.text.strip().split(' ')[2])
    
# 결과 출력
print(search_ranks)