import requests

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
            rating_pages.append(response.text)
            week_index += 1
        month += 1


# 테스트 코드
print(len(rating_pages)) # 가져온 총 페이지 수 
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드