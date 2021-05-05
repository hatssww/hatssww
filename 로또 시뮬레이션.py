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


# 당첨 번호 뽑기
def draw_winning_numbers():
    winning_numbers = generate_numbers(6)
    winning_numbers.sort()
    
    # 보너스 번호 추첨
    bonus = random.randint(1,45)
    if bonus not in winning_numbers:
        winning_numbers.append(bonus)
    return winning_numbers

print(draw_winning_numbers())