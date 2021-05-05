f = open('vocabulary.txt', 'w')

while True:
    key = input("영어 단어를 입력하세요: ")
    if key == 'q':
        break
    value = input("한국어 뜻을 입력하세요: ")
    if value == 'q':
        break
            
    f.write(f"{key}: {value}\n")

f.close()