%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_details.csv')

# 조건 만들기
boolean_adobe = df['company'] == 'Adobe'  # 회사가 'Adobe'
boolean_all_races = df['race'] == 'Overall_totals'  # 인종은 전체
boolean_not_zero = df['count'] != 0  # 직군 0명인 데이터 제외
boolean_job_category = (df['job_category'] != 'Totals') & (df['job_category'] != 'Previous_totals')  # 직군에서 필요없는 데이터 제외

# 조건 합침
df_adobe = df[boolean_adobe & boolean_all_races & boolean_not_zero & boolean_job_category]

# 파이그래프 출력(직군 분포)
df_adobe.plot(kind='pie', y='count')