import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import math
import random
import datetime
from PIL import Image, ImageTk

# ===== 상수 =====
BG_COLOR = '#FFF0F5'  # 연한 핑크
CARD_WIDTH = 400
CARD_HEIGHT = 700
CARNATION_IMG = "Screenshot 2025-05-08 183917.png"
FAMILY_IMG = "image.png"
FONT_MAIN = ("맑은 고딕", 20, "bold")
FONT_LABEL = ("맑은 고딕", 12)
FONT_DATE = ("맑은 고딕", 10)

# ===== 함수 분리 =====
def draw_carnation(canvas, x, y, size):
    # 카네이션 꽃잎 그리기
    for i in range(12):
        angle = i * 30
        rad = math.radians(angle)
        x1 = x + size * math.cos(rad)
        y1 = y + size * math.sin(rad)
        canvas.create_oval(x1-size/2, y1-size/2, x1+size/2, y1+size/2, fill='pink', outline='pink')
    
    # 카네이션 중앙 그리기
    canvas.create_oval(x-size/3, y-size/3, x+size/3, y+size/3, fill='yellow', outline='yellow')
    
    # 줄기 그리기
    canvas.create_line(x, y+size, x, y+size*2, fill='green', width=3)
    
    # 잎 그리기
    canvas.create_oval(x-size/2, y+size*1.5, x+size/2, y+size*2, fill='green', outline='green')

def draw_small_carnation(canvas, x, y, size):
    elements = []
    # 작은 카네이션 그리기
    for i in range(8):
        angle = i * 45
        rad = math.radians(angle)
        x1 = x + size * math.cos(rad)
        y1 = y + size * math.sin(rad)
        elements.append(canvas.create_oval(x1-size/3, y1-size/3, x1+size/3, y1+size/3, fill='pink', outline='pink'))
    elements.append(canvas.create_oval(x-size/4, y-size/4, x+size/4, y+size/4, fill='yellow', outline='yellow'))
    return elements

def draw_heart(canvas, x, y, size):
    # 하트 그리기
    points = [
        x, y-size/2,
        x-size/2, y-size,
        x-size, y-size/2,
        x-size, y,
        x, y+size,
        x+size, y,
        x+size, y-size/2,
        x+size/2, y-size
    ]
    return [canvas.create_polygon(points, fill='red', outline='red')]

def draw_money(canvas, x, y, size):
    elements = []
    # 돈 그리기
    elements.append(canvas.create_rectangle(x-size/2, y-size/3, x+size/2, y+size/3, fill='green', outline='gold'))
    elements.append(canvas.create_text(x, y, text="₩", font=("맑은 고딕", size//2, "bold"), fill='gold'))
    return elements

# ===== 애니메이션 개선 (간단한 움직임) =====
def animate_element(canvas, draw_func, x, y, size, dx, dy, steps=10, delay=30):
    elements = draw_func(canvas, x, y, size)
    def move_step(step):
        if step > steps:
            for el in elements:
                canvas.delete(el)
            return
        for el in elements:
            canvas.move(el, dx, dy)
        canvas.after(delay, lambda: move_step(step+1))
    move_step(0)

# show_animation 함수 내에서 랜덤 요소에 움직임 적용
def show_animation(event):
    for element in getattr(show_animation, 'current_elements', []):
        canvas.delete(element)
    show_animation.current_elements = []
    for _ in range(3):
        x = random.randint(50, 350)
        y = random.randint(50, 250)
        element_type = random.choice(['heart', 'carnation', 'money'])
        dx = random.choice([-3, 3])
        dy = random.choice([-3, 3])
        if element_type == 'heart':
            animate_element(canvas, draw_heart, x, y, 40, dx, dy)
        elif element_type == 'carnation':
            animate_element(canvas, draw_small_carnation, x, y, 30, dx, dy)
        else:
            animate_element(canvas, draw_money, x, y, 40, dx, dy)
    # 요소들은 애니메이션이 끝나면 자동 삭제됨

def show_message():
    message_window = tk.Toplevel(root)
    message_window.title("어버이날 축하")
    message_window.geometry("400x500")
    message_window.configure(bg=BG_COLOR)
    try:
        image = Image.open(FAMILY_IMG)
        image = image.resize((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(message_window, image=photo, bg=BG_COLOR)
        image_label.image = photo
        image_label.pack(pady=20)
    except:
        no_image_label = tk.Label(message_window, text="가족 사진을 넣어주세요!", font=FONT_LABEL, bg=BG_COLOR)
        no_image_label.pack(pady=20)
    message_text = """
    사랑하는 부모님께,\n\n항상 곁에서 든든하게 응원해주시고, 아낌없는 사랑과 희생으로 저를 키워주셔서 정말 감사합니다.\n부모님의 따뜻한 마음과 헌신 덕분에 지금의 제가 있을 수 있었습니다.\n\n앞으로도 건강하시고, 항상 행복하시길 진심으로 바랍니다.\n저도 항상 부모님 곁에서 힘이 되는 아들이 되겠습니다.\n\n사랑합니다 ♥\n\nby Andy Cho"""
    text_frame = tk.Frame(message_window, bg=BG_COLOR)
    text_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    message_widget = tk.Text(text_frame, font=FONT_LABEL, height=8, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    message_widget.insert(tk.END, message_text)
    message_widget.config(state=tk.DISABLED)
    message_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=message_widget.yview)
    close_button = tk.Button(message_window, text="닫기", font=FONT_LABEL, command=message_window.destroy, bg='#FFB6C1', activebackground='#FF69B4')
    close_button.pack(pady=10)

def on_btn_enter(e):
    btn.config(bg='#FFB6C1')
def on_btn_leave(e):
    btn.config(bg='SystemButtonFace')

# ===== 메인 윈도우 생성 =====
root = tk.Tk()
root.title("어버이날 축하 카드")
root.geometry(f"{CARD_WIDTH}x{CARD_HEIGHT}")
root.configure(bg=BG_COLOR)

# 날짜 표시
date_label = tk.Label(root, text=datetime.datetime.now().strftime('%Y년 %m월 %d일'), font=FONT_DATE, bg=BG_COLOR)
date_label.pack(side=tk.BOTTOM, pady=5)

# Canvas 추가
canvas = tk.Canvas(root, width=400, height=300, bg='white', highlightthickness=0)
canvas.pack(pady=10)

# 카네이션 이미지 표시
try:
    carnation_img = Image.open(CARNATION_IMG)
    carnation_img = carnation_img.resize((220, 220), Image.Resampling.LANCZOS)
    carnation_photo = ImageTk.PhotoImage(carnation_img)
    canvas.create_image(200, 150, image=carnation_photo)
    canvas.carnation_photo = carnation_photo  # 참조 유지
except Exception as e:
    # 이미지가 없거나 오류가 있을 경우 기존 카네이션 그림 유지
    draw_carnation(canvas, 200, 150, 40)

# 클릭 이벤트 바인딩
canvas.bind('<Button-1>', show_animation)

# 메인 제목
label = tk.Label(root, text="어버이날 축하드립니다!", font=FONT_MAIN, fg="red", bg=BG_COLOR)
label.pack(pady=10)

# 가족 정보 프레임
family_frame = tk.Frame(root, bg=BG_COLOR)
family_frame.pack(pady=10)

# 결혼 정보
marriage_label = tk.Label(family_frame, 
    text="2003년 결혼", 
    font=FONT_LABEL,
    justify=tk.CENTER,
    bg=BG_COLOR)
marriage_label.pack(pady=5)

# 아버지 정보
father_label = tk.Label(family_frame, 
    text="아버지: 조성헌 (1972년생)", 
    font=FONT_LABEL,
    justify=tk.LEFT,
    bg=BG_COLOR)
father_label.pack(pady=5)

# 어머니 정보
mother_label = tk.Label(family_frame, 
    text="어머니: 손성혜 (1978년생)", 
    font=FONT_LABEL,
    justify=tk.LEFT,
    bg=BG_COLOR)
mother_label.pack(pady=5)

# 메시지 버튼
btn = tk.Button(root, text="클릭해서 메시지 보기", font=("맑은 고딕", 14), command=show_message)
btn.pack(pady=20)
btn.bind('<Enter>', on_btn_enter)
btn.bind('<Leave>', on_btn_leave)

root.mainloop()
