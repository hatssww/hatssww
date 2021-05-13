import cil
from cil import display

# 이미지 파일 불러오기
img1 = cil.read_image('img1')
img2 = cil.read_image('img2')

# 이미지 반전시키기
inverted_img1 = cil.invert(img1)
inverted_img2 = cil.invert(img2)


# 결과 출력
print('원본 이미지')
print('\nimage1:')
display(img1)
print('\nimage2:')
display(img2)

print('\n색상 반전된 이미지')
print('\nimage1:')
display(inverted_img1)
print('\nimage2:')
display(inverted_img2)