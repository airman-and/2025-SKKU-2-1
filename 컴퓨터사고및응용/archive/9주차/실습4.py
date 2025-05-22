import tkinter as tk

# ── 키 이벤트 핸들러 ──
def on_key_press(event):
    dx, dy = 0, 0
    if event.keysym == 'Left':
        dx = -10
    elif event.keysym == 'Right':
        dx = 10
    elif event.keysym == 'Up':
        dy = -10
    elif event.keysym == 'Down':
        dy = 10
    # 사각형 이동
    canvas.move(rect, dx, dy)

# ── 메인 윈도우 설정 ──
root = tk.Tk()
root.title("화살표 키로 사각형 이동")

# ── 캔버스 생성 ──
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(padx=10, pady=10)

# ── 사각형 그리기 ──
# (x1, y1) = (50, 50), (x2, y2) = (150, 100)
rect = canvas.create_rectangle(50, 50, 150, 100, fill="lightgreen")

# ── 키 바인딩 ──
# 캔버스에 포커스를 맞춰야 키 입력을 받을 수 있습니다.
canvas.focus_set()
canvas.bind("<KeyPress>", on_key_press)

# ── 이벤트 루프 시작 ──
root.mainloop()
