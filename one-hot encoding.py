import pandas as pd

# 경로 지정
TITANIC_FILE_PATH = '../머신러닝 수업/titanic.csv'
titanic_df = pd.read_csv(TITANIC_FILE_PATH)

# one-hot encoding할 열들 dataframe으로 추출
features_df = titanic_df[['Sex', 'Embarked']]

# 부분 one-hot encoding
one_hot_encoded_df1 = pd.get_dummies(features_df)

# 전체 데이터에서 원하는 열만 one-hot encoding 하기
one_hot_encoded_df2 = pd.get_dummies(data=titanic_df, columns=['Sex', 'Embarked'])


# 결과
print(one_hot_encoded_df1)  # 추출한 columns만 출력
print(one_hot_encoded_df2)  # 지정한 columns만 변환 후 전체 출력