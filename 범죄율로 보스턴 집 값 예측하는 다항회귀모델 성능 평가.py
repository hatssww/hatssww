# 필요한 라이브러리 import
from sklearn.datasets import load_boston
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd 

# 보스턴 집 데이터 갖고 오기
boston_dataset = load_boston()

# 다항 속성 만들기
polynomial_transformer = PolynomialFeatures(2)  # 2차 함수
polynomial_data = polynomial_transformer.fit_transform(boston_dataset.data)

# 다항 속성 이름 가져오기
polynomial_feature_names = polynomial_transformer.get_feature_names(boston_dataset.feature_names)

# 다항 입력 변수를 pandas dataframe으로 변환
X = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)

# 목표 변수를 pandas dataframe으로 변환
y = pd.DataFrame(boston_dataset.target, columns=['MEDV'])


# 학습 데이터와 평가 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# 선형 회귀 모델 학습시키기
model = LinearRegression()
model.fit(X_train, y_train)
model.intercept_  # theta_0
model.coef_  # theta_1

# 평가 예측값
y_test_predict = model.predict(X_test)  

# 테스트 코드 (평균 제곱근 오차로 모델 성능 평가)
mse = mean_squared_error(y_test, y_test_predict)

print(mse ** 0.5)