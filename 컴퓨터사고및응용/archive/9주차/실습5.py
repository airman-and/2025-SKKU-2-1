import tkinter as tk
import random

# ─── 메인 윈도우 설정 ───
root = tk.Tk()
root.title("랜덤 사각형 10개")

# ─── 캔버스 생성 ───
WIDTH, HEIGHT = 600, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack(padx=10, pady=10)

# ─── 랜덤 사각형 10개 그리기 ───
for _ in range(10):
    # 위치 (x1,y1) 랜덤
    x1 = random.randint(0, WIDTH  - 50)
    y1 = random.randint(0, HEIGHT - 50)
    # 크기 (너비·높이) 랜덤 (20~100px)
    x2 = x1 + random.randint(20, 100)
    y2 = y1 + random.randint(20, 100)
    # 색상 랜덤 (hex 코드)
    color = "#{:02x}{:02x}{:02x}".format(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    # 사각형 그리기
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

# ─── 이벤트 루프 시작 ───
root.mainloop()
