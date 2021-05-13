import pandas as pd
import matplotlib.pyplot as plt


# 디스플레이 옵션 설정
pd.set_option('display.width', 320)
pd.set_option('display.max_columns', 20)


# 데이터 불러오기
covid_df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/cases_country.csv')
print(covid_df)


# 나라, 확진자, 사망자 데이터 추출
X = covid_df[['Country', 'Confirmed', 'Deaths']]
# 나라 이름을 인덱스로 지정
X.index = X['Country']
# 인덱스로 쓰인 열 제거
X = X.drop(['Country'], axis=1)


# 나라별 사망률 구하기
X['Death Rate (per 100)'] = 100 * X['Deaths'] / X['Confirmed']
print(X)


# 사망률 가장 높은 10개국 출력(사망자 1000명 이상)
top_10_country = X[X['Deaths'] >= 1000].sort_values('Death Rate (per 100)')[-10:]
print(top_10_country)


# 사망률 바 그래프
plt.barh(df_top10_countries_dr.index, df_top10_countries_dr['Death Rate (Per 100)'], color="darkcyan")
plt.tick_params(size=5, labelsize=11)
plt.xlabel("Death Rate (Per 100)", fontsize=14)
plt.title("Top 10 Countries by Death Rate", fontsize=18)
plt.grid(alpha=0.3)
plt.show()
