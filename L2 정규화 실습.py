from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from math import sqrt

import numpy as np
import pandas as pd

# 데이터 파일 경로 정의
INSURANCE_FILE_PATH = './datasets/insurance.csv'
insurance_df = pd.read_csv(INSURANCE_FILE_PATH)

# 필요한 열들에 One-hot Encoding
insurance_df = pd.get_dummies(data=insurance_df, columns=['sex', 'smoker', 'region'])

# 입력 변수 데이터
X = insurance_df.drop(['charges'], axis=1)

# 다항 함수 만들기
polynomial_transformer = PolynomialFeatures(4)  # 4 차항 변형기 정의
polynomial_features = polynomial_transformer.fit_transform(X.values)  # 4차 항 변수로 변환

# 새로운 변수 이름 생성
features = polynomial_transformer.get_feature_names(X.columns)

# 다항 입력 변수
X = pd.DataFrame(polynomial_features, columns=features)

# 목표 변수
y = insurance_df[['charges']]

# 학습 데이터와 평가 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)

# Ridge 모델 학습시키기
model = Ridge(alpha=0.01, max_iter=2000, normalize=True)
model.fit(X_train, y_train)

# 학습 예측값
y_train_predict = model.predict(X_train)

# 평가 예측값
y_test_predict = model.predict(X_test)


# 평균 제곱 오차
mse = mean_squared_error(y_train, y_train_predict)

print("training set에서 성능")
print("-----------------------")
print(f'오차: {sqrt(mse)}')

mse = mean_squared_error(y_test, y_test_predict)

print("testing set에서 성능")
print("-----------------------")
print(f'오차: {sqrt(mse)}')