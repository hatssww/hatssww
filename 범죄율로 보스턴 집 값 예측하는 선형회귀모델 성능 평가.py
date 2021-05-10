# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd  

# 보스턴 집 데이터 갖고 오기
boston_house_dataset = datasets.load_boston()

# 입력 변수를 사용하기 편하게 pandas dataframe으로 변환
X = pd.DataFrame(boston_house_dataset.data, columns=boston_house_dataset.feature_names)

# 목표 변수를 사용하기 편하게 pandas dataframe으로 변환
y = pd.DataFrame(boston_house_dataset.target, columns=['MEDV'])

# 입력 변수 범죄율 열 가져오기
x = X[['CRIM']]

# 학습 데이터와 평가 데이터 나누기
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)

# 선형 회귀 모델 학습시키기
model = LinearRegression()
model.fit(x_train, y_train)
model.intercept_  # theta_0
model.coef_  # theta_1
# f(x) = 24.12202188 -0.41546547x

# 평가 예측값
y_test_predict = model.predict(x_test)  

# 테스트 코드 (평균 제곱근 오차로 모델 성능 평가)
mse = mean_squared_error(y_test, y_test_predict)

print(mse ** 0.5)