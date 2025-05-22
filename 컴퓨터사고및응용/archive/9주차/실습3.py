import tkinter as tk

# ──── 콜백 함수 ────
def grow(event):
    # 현재 사각형 좌표 가져오기
    x1, y1, x2, y2 = canvas.coords(rect)
    # 우측·하단으로 10px씩 확장
    canvas.coords(rect, x1, y1, x2 + 10, y2 + 10)

def shrink(event):
    x1, y1, x2, y2 = canvas.coords(rect)
    # 최소 크기(너비·높이 20px) 이상일 때만 축소
    if (x2 - x1) > 20 and (y2 - y1) > 20:
        canvas.coords(rect, x1, y1, x2 - 10, y2 - 10)

# ──── 메인 윈도우 설정 ────
root = tk.Tk()
root.title("사각형 크기 조절")

# ──── 캔버스 생성 ────
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(padx=10, pady=10)

# ──── 사각형 그리기 ────
# (x1, y1) = (50, 50), (x2, y2) = (150, 100)
rect = canvas.create_rectangle(50, 50, 150, 100, fill="skyblue")

# ──── 마우스 이벤트 바인딩 ────
canvas.bind("<Button-1>", grow)   # 왼쪽 클릭 → 키우기
canvas.bind("<Button-3>", shrink) # 오른쪽 클릭 → 줄이기

root.mainloop()
