import numpy as np
import pandas as pd

# numpy 임의성 조절
np.random.seed(42)

# 데이터 셋 가지고 오기
dataset = pd.read_csv('./data/MNIST_preprocessed.csv', sep=',', header=None).values

# 입력, 목표 변수 데이터 셋 나누기
X = dataset[:, 0:784]
Y = dataset[:, 784:]

# training, testing 데이터 셋 나누기
X_train, X_test = X[0:250,], X[250:,]
Y_train, Y_test = Y[0:250,], Y[250:,]


# 시그모이드 함수
def sigmoid(x):
    return 1/(1 + np.exp(-x))


# 신경망의 가중치와 편향 초기화 함수
def initialize_parameters(nodes_per_layer):
    L = len(nodes_per_layer) - 1  # 층 개수 저장
    parameters = {}
    
    # 1층 ~ L층을 돌면서 가중치와 편향 초기화
    for l in range(1, L+1):
        parameters['W' + str(l)] = np.random.randn(nodes_per_layer[l], nodes_per_layer[l-1]) * np.sqrt(1. / nodes_per_layer[l])
        parameters['b' + str(l)] = np.random.randn(nodes_per_layer[l]) * np.sqrt(1. / nodes_per_layer[l])
        
    return parameters


# 순전파 함수
def feed_forward(x, parameters):
    cache = {'a0': x}  # 0 번째 층 출력 저장
    L = len(parameters) // 2  # 층 수 저장
    
    for l in range(1, L+1):
        # 전 층 뉴런의 출력, 현재 층 뉴런들의 가중치, 편향 데이터
        a_prev = cache[f'a{l-1}']
        W = parameters[f'W{l}']
        b = parameters[f'b{l}']
        
        # z와 새로운 a 계산
        z = W @ a_prev + b
        a = sigmoid(z)

        # 결과 값 캐시에 저장
        cache['z' + str(l)] = z
        cache['a' + str(l)] = a
                
    return a, cache


# 실행 코드
neurons_per_layer = [784, 128, 64, 10]
parameters = initialize_parameters(neurons_per_layer)
feed_forward(X_train[0], parameters)[0]  # a 결과값 출력