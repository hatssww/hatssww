import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 수강신청 가능 여부 column 추가
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


# 개강 가능 과목 추출
allowed = df["status"] == "allowed"

# 개강 가능 과목 당 학생수 추출
count = df.loc[allowed, "course name"].value_counts()

# 강의실 사용 조건
auditorium = list(count[count >= 80].index)
large_room = list(count[(count < 80) & (count >= 40)].index)
medium_room = list(count[(count < 40) & (count >= 15)].index)
small_room = list(count[(count < 15) & (count >= 5)].index)

# 폐강 과목 강의실 사용 불가 지정
not_assigned = df["status"] == "not allowed"
df.loc[not_assigned, "room assignment"] = "not assigned"

# 강의실 지정
for course in auditorium:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Auditorium"
for course in large_room:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Large room"
for course in medium_room:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Medium room"
for course in small_room:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Small room"


# 과목별 분반 지정
for i in range(len(auditorium)):
    df.loc[(df["course name"] == sorted(auditorium)[i]) & allowed, "room assignment"] = "Auditorium-" + str(i + 1)
for i in range(len(large_room)):
    df.loc[(df["course name"] == sorted(large_room)[i]) & allowed, "room assignment"] = "Large-" + str(i + 1)
for i in range(len(medium_room)):
    df.loc[(df["course name"] == sorted(medium_room)[i]) & allowed, "room assignment"] = "Medium-" + str(i + 1)
for i in range(len(small_room)):
    df.loc[(df["course name"] == sorted(small_room)[i]) & allowed, "room assignment"] = "Small-" + str(i + 1)

# column 이름 변경
df.rename(columns={"room assignment": "room number"}, inplace = True)

# 결과 출력
df