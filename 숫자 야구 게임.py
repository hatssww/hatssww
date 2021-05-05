from random import randint


# 정답 숫자 3개 뽑기
def generate_numbers():
    numbers = []
    for i in range(3):
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 유저에게 3개의 숫자 입력받기
def take_guess():
    new_guess = []
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    i = 1
    while i < 4:
        user_num = int(input(f"{i}번째 숫자를 입력하세요: "))
        if 0 <= user_num <= 9 and user_num not in new_guess:
            new_guess.append(user_num)
            i += 1        
        elif user_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
    
    return new_guess


# 점수 계산
def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1
        else:
            pass
    
    return strike_count, ball_count


# 테스트
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)