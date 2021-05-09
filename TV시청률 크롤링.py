import requests
from bs4 import BeautifulSoup

# 각 기간별 페이지 모두 받아 리스트로 만들기
year = list(range(2010, 2019))
rating_pages = []

for i in year:
    month = 1
    while month < 13:
        week_index = 0
        while week_index < 5:
            url = f"https://workey.codeit.kr/ratings/index?year={i}&month={month}&weekIndex={week_index}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            if len(soup.select('.row')) > 1:
                rating_pages.append(soup)
            week_index += 1
        month += 1


# 레코드를 담는 빈 리스트 생성
records = []

# 각 페이지 파싱해서 정보 얻기
for page in rating_pages:
    date = page.select('option[selected=selected]')[2].text
    ranks = page.select('.row .rank')[1:]
    channels = page.select('.row .channel')[1:]
    programs = page.select('.row .program')[1:]
    percents = page.select('.row .percent')[1:]
    
    # 페이지에 있는 10개의 레코드를 리스트에 추가
    for i in range(10):
        record = []
        record.append(date)
        record.append(ranks[i].text)
        record.append(channels[i].text)
        record.append(programs[i].text)
        record.append(percents[i].text)
        records.append(record)
        
# DataFrame 만들기
df = pd.DataFrame(data = records, columns=['period', 'rank', 'channel', 'program', 'rating'])

# 결과 출력
df.head()