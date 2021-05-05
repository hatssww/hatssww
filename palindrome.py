def is_palindrome(word):
    word_list = list(word)
    for i in range(len(word) // 2):
        if word_list[i] != word_list[-1 - i]:
            return False
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))