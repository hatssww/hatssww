from cil.utils import read_image, display
from cil.processing import invert as inv, merge as mrg


# 이미지 불러와서 처리
logo = read_image('codeit_logo')
inverted_logo = inv(logo)  # 반전
merged_img = mrg(logo, inverted_logo)  # 원본 + 반전

print('원본 이미지:')
display(logo)
print('\n색상 반전 이미지:')
display(inverted_logo)
print('\n합성 이미지:')
display(merged_img)

# 결과 출력
print()
dir_list = dir()
key_names = ['read_image', 'display', 'inv', 'mrg']
print(all(x in dir_list for x in key_names))
print('save_image' not in dir_list)