from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

import numpy as np
import pandas as pd

# 경고 메시지 출력 억제 코드
import warnings
warnings.simplefilter(action='ignore')

# 데이터 파일 경로 정의
GENDER_FILE_PATH = './datasets/gender.csv'
gender_df = pd.read_csv(GENDER_FILE_PATH)

# 입력, 목표 변수 데이터
X = pd.get_dummies(gender_df.drop(['Gender'], axis=1)) # 입력 변수를 one-hot encode
y = gender_df[['Gender']].values.ravel()

# 로지스틱 회귀 모델
model = LogisticRegression()

# 하이퍼파라미터 파이썬 딕셔너리 만들기
hyper_parameter = {
    'penalty': ['l1', 'l2'],
    'max_iter': [500, 1000, 1500, 2000]
}

# grid search 학습
hyper_parameter_tuner = GridSearchCV(model, hyper_parameter, cv=5)  # 5겹 교차 검증
hyper_parameter_tuner.fit(X, y)
best_params = hyper_parameter_tuner.best_params_


# 결과
print(best_params)