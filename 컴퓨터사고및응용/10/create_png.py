from PIL import Image, ImageDraw
import os

# 현재 스크립트의 디렉토리 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__))

# 새로운 이미지 생성 (100x100 크기의 흰색 배경)
img = Image.new('RGB', (100, 100), color='white')
draw = ImageDraw.Draw(img)

# 빨간색 원 그리기
draw.ellipse([20, 20, 80, 80], fill='red')

# 이미지를 PNG 파일로 저장
output_path = os.path.join(current_dir, '123.png')
img.save(output_path)
print(f"이미지가 성공적으로 저장되었습니다: {output_path}") 