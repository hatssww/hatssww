import pandas as pd
import numpy as np
from math import sqrt

# 받아올 평점 데이터 경로 정의
RATING_DATA_PATH = './data/ratings.csv'  
# 소수점 둘째 자리까지만 출력
np.set_printoptions(precision=2)


# 유클리드 거리 계산 함수
def distance(user_1, user_2):
    return sqrt(np.sum((user_1 - user_2)**2))
    

# movie_id 번째 영화를 평가하지 않은 유저들을 미리 제외하는 함수
def filter_users_without_movie(rating_data, movie_id):
    return rating_data[~np.isnan(rating_data[:,movie_id])]
    

# 평점 데이터의 빈값을 각 유저 평균 값으로 채워주는 함수
def fill_nan_with_user_mean(rating_data):
    filled_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    row_mean = np.nanmean(filled_data, axis=0)  # 유저 평균 평점 계산
    
    inds = np.where(np.isnan(filled_data))  # 비어 있는 인덱스 구하기
    filled_data[inds] = np.take(row_mean, inds[1])  # 빈 인덱스를 유저 평점으로 채움
    
    return filled_data
    

# user_id에 해당하는 유저의 이웃들을 찾아주는 함수
def get_k_neighbors(user_id, rating_data, k):
    distance_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    # 마지막에 거리 데이터를 담을 열 추가
    distance_data = np.append(distance_data, np.zeros((distance_data.shape[0], 1)), axis=1)
    
    for i in range(len(distance_data)):
        row = distance_data[i]
        if i == user_id:  # 자기 자신은 제외하기 위해 무한대로 거리 설정
            row[-1] = np.inf
        else:             # 대상 이웃과 user_id와의 거리를 저장
            row[-1] = distance(distance_data[user_id][:-1], row[:-1])
    
    # 데이터를 거리 열을 기준으로 정렬
    distance_data = distance_data[np.argsort(distance_data[:, -1])]
    
    # 가장 가까운 k개의 행만 리턴 + 마지막(거리) 열 제외
    return distance_data[:k, :-1]
    

# 실행 코드
# 영화 3을 본 유저들 중, 유저 0와 비슷한 유저 5명 찾기
rating_data = pd.read_csv(RATING_DATA_PATH, index_col='user_id').values  # 평점 데이터를 불러오기
filtered_data = filter_users_without_movie(rating_data, 3)  # 3 번째 영화를 보지 않은 유저를 데이터에서 미리 제외
filled_data = fill_nan_with_user_mean(filtered_data)  # 빈값들이 채워진 새로운 행렬 만들기
user_0_neighbors = get_k_neighbors(0, filled_data, 5)  # 유저 0과 비슷한 5개의 유저 데이터 찾기

# 결과 출력
print(user_0_neighbors)