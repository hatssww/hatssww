import random

# 번호 뽑기 함수
def generate_numbers(n):
    random_list = []
    while len(random_list) < n:
        num = random.randint(1,45)
        if num not in random_list:
            random_list.append(num)
    return random_list

print(generate_numbers(6))