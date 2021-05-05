import random

# 번호 뽑기 함수
def generate_numbers(n):
    random_list =[]
    i = 1
    while i <= 6:
        random_list.append(random.randint(1,45))
        i += 1
    return random_list

print(generate_numbers(6))