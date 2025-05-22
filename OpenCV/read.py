import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import unsharp_mask
import os

# 한글 폰트 문제 해결을 위한 설정
import matplotlib.font_manager as fm
# 영문 폰트로 대체 (시스템에 맞게 조정)
plt.rcParams['font.family'] = 'DejaVu Sans'
# 유니코드 문제 해결
plt.rcParams['axes.unicode_minus'] = False

# 현재 디렉토리 확인 및 이미지 파일 존재 확인
print(f"현재 작업 디렉토리: {os.getcwd()}")
image_path = 'sample.jpg'
if not os.path.exists(image_path):
    print(f"'{image_path}' 파일이 현재 디렉토리에 없습니다.")
    print("현재 디렉토리의 파일 목록:", os.listdir())
    # 대체 이미지 사용
    alternate_path = os.path.join('opencv-course', 'Resources', 'Photos', 'cat.jpg')
    if os.path.exists(alternate_path):
        image_path = alternate_path
        print(f"대체 이미지를 사용합니다: {image_path}")
    else:
        print("대체 이미지도 찾을 수 없습니다.")
        exit(0)

# 이미지 읽기
img = cv.imread(image_path)
if img is None:
    print(f'이미지를 불러올 수 없습니다: {image_path}')
    exit(0)

try:
    # 원본 이미지 복사
    original = img.copy()

    # 그레이스케일 변환
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 가우시안 블러
    blurred = cv.GaussianBlur(img, (7, 7), 0)

    # 엣지 검출 (Canny)
    edges = cv.Canny(gray, 100, 200)

    # 이미지 선명화 (Unsharp Masking)
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    sharpened = unsharp_mask(rgb_img, radius=5, amount=2)
    sharpened = (sharpened * 255).astype(np.uint8)

    # 이미지 히스토그램 평활화
    gray_eq = cv.equalizeHist(gray)

    # 컬러 이미지 채널별 히스토그램 평활화
    img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])
    img_eq = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)

    # 이미지 리사이징
    resized = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

    # 이미지 회전
    rows, cols = img.shape[:2]
    M = cv.getRotationMatrix2D((cols/2, rows/2), 45, 1)
    rotated = cv.warpAffine(img, M, (cols, rows))    # 결과 시각화
    plt.figure(figsize=(16, 12))

    plt.subplot(3, 3, 1), plt.imshow(cv.cvtColor(original, cv.COLOR_BGR2RGB))
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 2), plt.imshow(gray, cmap='gray')
    plt.title('Grayscale'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 3), plt.imshow(cv.cvtColor(blurred, cv.COLOR_BGR2RGB))
    plt.title('Gaussian Blur'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 4), plt.imshow(edges, cmap='gray')
    plt.title('Canny Edge'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 5), plt.imshow(sharpened)
    plt.title('Sharpened'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 6), plt.imshow(gray_eq, cmap='gray')
    plt.title('Histogram Equalization'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 7), plt.imshow(cv.cvtColor(img_eq, cv.COLOR_BGR2RGB))
    plt.title('Color Histogram Equalization'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 8), plt.imshow(cv.cvtColor(resized, cv.COLOR_BGR2RGB))
    plt.title('Resized'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 9), plt.imshow(cv.cvtColor(rotated, cv.COLOR_BGR2RGB))
    plt.title('Rotated'), plt.xticks([]), plt.yticks([])

    plt.tight_layout()
    plt.show()

    # 이미지 저장
    output_path = 'processed_image.jpg'
    cv.imwrite(output_path, img_eq)
    print(f'처리된 이미지가 저장되었습니다: {output_path}')

except Exception as e:
    print(f'오류가 발생했습니다: {e}')

print('이미지 처리가 완료되었습니다.')