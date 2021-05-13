f = open('vocabulary.txt', 'r')

for line in f:
    new_data = line.strip().split(': ')
    question, answer = new_data[1], new_data[0]
    
    # 유저 입력
    user_input = input(f"{question}: ")
    
    # 정답 확인
    if user_input == answer:
        print("맞았습니다!\n")
    else:
        print(f"아쉽습니다. 정답은 {answer}입니다.\n")