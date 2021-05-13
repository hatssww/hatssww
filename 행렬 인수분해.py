import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# numpy에서 임의성 도구들의 결과가 일정하게 나오도록 설정
np.random.seed(5)

# 데이터 파일 경로 정의
RATING_DATA_PATH = './data/ratings.csv'

# numpy 출력 옵션 설정
np.set_printoptions(precision=2)  # 소수점 둘째 자리까지만 출력
np.set_printoptions(suppress=True)


# 예측 값 계산 함수
def predict(Theta, X):
    return Theta @ X


# 행렬 인수분해 알고리즘 손실 함수
def cost(prediction, R):
    return np.nansum((prediction - R)**2)


# 임의로 유저 취향과 상품 속성 행렬들을 만들어주는 함수
def initialize(R, num_features):
    num_users, num_items = R.shape  # 유저 데이터 개수와 영화 개수를 변수에 저장
    Theta = np.random.rand(num_users, num_features)
    X = np.random.rand(num_features, num_items)
    return Theta, X
    

# 행렬 인수분해 경사 하강 함수
def gradient_descent(R, Theta, X, iteration, alpha, lambda_):
    num_user, num_items = R.shape  # 유저 데이터 개수와 영화 개수를 변수에 저장
    num_features = len(X)  # 속성 개수
    costs = []
        
    for _ in range(iteration):
        prediction = predict(Theta, X)  # 예측값
        error = prediction - R  # 오차
        costs.append(cost(prediction, R))  # 손실값 저장
                          
        for i in range(num_user):
            for j in range(num_items):
                if not np.isnan(R[i][j]):
                    for k in range(num_features):
                        Theta[i][k] -= alpha * (np.nansum(error[i, :]*X[k, :]) + lambda_*Theta[i][k])
                        X[k][j] -= alpha * (np.nansum(error[:, j]*Theta[:, k]) + lambda_*X[k][j])
                        
    return Theta, X, costs



# 평점 데이터 불러오기
ratings_df = pd.read_csv(RATING_DATA_PATH, index_col='user_id')

# 평점 데이터에 mean normalization을 적용한다
for row in ratings_df.values:
    row -= np.nanmean(row)
       
# 목표 변수
R = ratings_df.values
        
Theta, X = initialize(R, 5)  # 행렬 초기화(임의 행렬 생성)
Theta, X, costs = gradient_descent(R, Theta, X, 200, 0.001, 0.01)  # 경사 하강
    
# 결과
print(Theta, X)

# 손실이 줄어드는 걸 시각화 하는 코드 (디버깅에 도움이 됨)
plt.plot(costs)