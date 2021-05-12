from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

import pandas as pd

# 데이터 셋 가져오기
cancer_data = load_breast_cancer()

# 입력, 목표 변수 데이터 프레임에 저장
X = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
y = pd.DataFrame(cancer_data.target, columns=['class'])

# training/test 셋 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
y_train = y_train.values.ravel()

# 트레이닝 셋 확인
print(X_train.head())