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

print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))