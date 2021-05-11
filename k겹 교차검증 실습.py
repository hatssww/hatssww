from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

import numpy as np
import pandas as pd

# 데이터 파일 경로 정의
GENDER_FILE_PATH = './datasets/gender.csv'
gender_df = pd.read_csv(GENDER_FILE_PATH)

# 입력, 목표 변수 데이터
X = pd.get_dummies(gender_df.drop(['Gender'], axis=1)) # 입력 변수를 one-hot encode
y = gender_df[['Gender']].values.ravel()

# 로지스틱 회귀 모델
model = LogisticRegression(solver='saga', max_iter=2000)

# k겹 교차검증
cross_val_score(model, X, y, cv=5)
k_fold_score = np.average(cross_val_score(model, X, y, cv=5))  # 평균값


# 결과
print(k_fold_score)