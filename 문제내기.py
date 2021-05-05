import random

f = open('vocabulary.txt', 'r')

# 사전 생성
vocabulary = []

for line in f:
    new_data = line.strip().split(': ')
    [question, answer] = new_data[1], new_data[0]
    vocabulary.append([question, answer])


while True:
    # 난수 생성
    i = random.randint(0, len(vocabulary)-1)

    # 유저 입력
    user_input = input(f"{vocabulary[i][0]}: ")
    
    # 정답 확인
    if user_input == vocabulary[i][1]:
        print("맞았습니다!\n")
    elif user_input == 'q':  # 종료
        break
    else:
        print(f"아쉽습니다. 정답은 {vocabulary[i][1]}입니다.\n")