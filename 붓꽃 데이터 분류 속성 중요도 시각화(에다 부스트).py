from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 데이터 가져오기
iris_data = load_iris()

# 입력, 목표 변수 데이터프레임 저장
X = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns=['class'])

# train/test 셋 만들기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
y_train = y_train.values.ravel()

# 에다 부스트 모델 만들기
model = AdaBoostClassifier(n_estimators=100)  # 스텀프 100개

# 모델 학습
model.fit(X_train, y_train)

# test set 예측값
y_predict = model.predict(X_test)

# 성능 평가
score = model.score(X_test, y_test)


# 속성 중요도
importances = model.feature_importances_

# 결정 트리 모델의 속성 중요도 시각화
indices_sorted = np.argsort(importances)

plt.figure()
plt.title("Feature importances")
plt.bar(range(len(importances)), importances[indices_sorted])
plt.xticks(range(len(importances)), X.columns[indices_sorted], rotation=90)
plt.show()