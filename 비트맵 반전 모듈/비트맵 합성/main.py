# __init__에 필요한 함수와 모듈만 import 하도록 설정
import cil


# 이미지 불러와서 처리
logo = cil.read_image('codeit_logo')
text = cil.read_image('codeit_text')

"""
print('코드잇 로고:')
cil.display(logo)
print('\n코드잇 텍스트:')
cil.display(text)

inverted_text = cil.invert(text)  # text 색상 반전
merged_img = cil.merge(logo, text)  # logo + text 합성

print('\n색상 반전 텍스트:')
cil.display(inverted_text)
print('\n합성 이미지:')
cil.display(merged_img)
"""


upside_down_logo = cil.vertical_flip(logo)  # logo 상하반전
reversed_text = cil.horizontal_flip(text)  # text 좌우 반전

print('코드잇 로고:')
cil.display(logo)
print('\n상하 반전된 로고:')
cil.display(upside_down_logo)

print('\n코드잇 텍스트:')
cil.display(text)
print('\n좌우 반전된 텍스트:')
cil.display(reversed_text)


# 사용한 네임스페이스 확인
print()
key_functions = ['read_image', 'save_image', 'display', 'invert', 'merge', 'horizontal_flip', 'vertical_flip']
non_key_functions = ['get_size', 'empty_image', 'invert_bit', 'or_bits']
print(all(x in dir(cil) for x in key_functions))
print(not any(x in dir(cil) for x in non_key_functions))