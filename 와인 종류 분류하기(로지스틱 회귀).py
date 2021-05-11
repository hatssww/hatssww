# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import pandas as pd  

# 와인 데이터 불러오기
wine_data = datasets.load_wine()

# 입력 변수 pandas dataframe으로 변환
X = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)

# 목표 변수 pandas dataframe으로 변환
y = pd.DataFrame(wine_data.target, columns=['Y/N'])

# 학습 데이터와 평가 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
y_train = y_train.values.ravel()

# 로지스틱 회귀 모델 학습시키기
model = LogisticRegression(solver='saga', max_iter=7500)
model.fit(X_train, y_train)

# 평가 예측값
y_test_predict = model.predict(X_test)

# 테스트 코드
score = model.score(X_test, y_test)
print(y_test_predict)
print(score)