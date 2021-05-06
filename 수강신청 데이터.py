import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 수강신청 가능 여부 판단 조건
df['status'] = 'allowed'

# 1학년은 들을 수 없는 수업 제한
bullian1 = df['year'] == 1
bullian2 = df["course name"] == "information technology"

df.loc[bullian1 & bullian2, 'status'] = 'not allowed'

# 4학년은 들을 수 없는 수업 제한
df.loc[(df['year'] == 4) & (df['course name'] == "commerce"), 'status'] = 'not allowed'

# 5명 미만 수강과목 폐강
count = df['course name'].value_counts()
closed_courses= list(count[count < 5].index)

for course in closed_courses:
    df.loc[df['course name'] == course, 'status'] = 'not allowed'