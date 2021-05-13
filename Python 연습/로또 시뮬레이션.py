import random

# 번호 뽑기 함수
def generate_numbers(n):
    random_list = []
    while len(random_list) < n:
        num = random.randint(1,45)
        if num not in random_list:
            random_list.append(num)
    return random_list


# 당첨 번호 뽑기
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


# 겹치는 번호 개수
def count_matching_numbers(list_1, list_2):
    s1 = set(list_1)
    s2 = set(list_2)
    return len(s1 & s2)


# 당첨금 확인
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_matching = count_matching_numbers(numbers, winning_numbers[6:])
    
    if count == 6:
        return 1000000000
    elif count == 5 and bonus_matching == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0