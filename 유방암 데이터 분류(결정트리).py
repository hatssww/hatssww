from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import pandas as pd

# 데이터 셋 가져오기
cancer_data = load_breast_cancer()

# 입력, 목표 변수 데이터 프레임에 저장
X = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
y = pd.DataFrame(cancer_data.target, columns=['class'])

# training/test 셋 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
y_train = y_train.values.ravel()

"""
# 결정 트리 모델 만들기
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)  # 모델 학습

# 랜덤 포레스트 모델 만들기
model = RandomForestClassifier(n_estimators=10, max_depth=4, random_state=42)
model.fit(X_train, y_train)  # 모델 학습
"""

# 에다 부스트 모델 만들기
model = AdaBoostClassifier(n_estimators=50, random_state=5)
model.fit(X_train, y_train)  # 모델 학습

# testing set 예측값
predictions = model.predict(X_test)

# 모델 성능 평가
score = model.score(X_test, y_test)

# 결과 출력
print(predictions, score)