# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd  

# 당뇨병 데이터 갖고 오기
diabetes_dataset = datasets.load_diabetes()

# 다항 속성 만들기
polynomial_transformer = PolynomialFeatures(2)  # 2차 함수
polynomial_data = polynomial_transformer.fit_transform(diabetes_dataset.data)

# 다항 속성 이름 가져오기
polynomial_feature_names = polynomial_transformer.get_feature_names(diabetes_dataset.feature_names)

# 다항 입력 변수를 pandas dataframe으로 변환
X = pd.DataFrame(polynomial_data, columns=polynomial_feature_names)

# 목표 변수를 pandas dataframe으로 변환
y = pd.DataFrame(diabetes_dataset.target, columns=['diabetes'])

# 학습 데이터와 평가 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# 선형 회귀 모델 학습시키기
model = LinearRegression()
model.fit(X_train, y_train)

# 평가 예측값
y_test_predict = model.predict(X_test)

# 평균 제곱근 오차로 모델 성능 평가
mse = mean_squared_error(y_test, y_test_predict)
print(mse ** 0.5)