f = open('vocabulary.txt', 'r')
data = f.readlines()

question = []
answer = []

for line in range(len(data)):
    new_data = data[line].strip().split(': ')
    question.append(new_data[1])
    answer.append(new_data[0])

for i in range(len(question)):
    print(f"{question[i]}: ", end="")
    user_input = input()
    if user_input == answer[i]:
        print("맞았습니다!")
    else:
        print(f"아쉽습니다. 정답은 {answer[i]}입니다.")