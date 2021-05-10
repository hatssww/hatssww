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

# 테스트 코드
X.head()