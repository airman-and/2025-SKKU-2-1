import tkinter as tk
from tkinter import messagebox

def on_login():
    user_id = ent_id.get()
    password = ent_pw.get()
    # 여기서는 입력값을 메시지 박스로 띄워 봅니다
    messagebox.showinfo("로그인 정보", f"아이디: {user_id}\n패스워드: {password}")

def on_cancel():
    # 입력란을 깨끗하게 비웁니다
    ent_id.delete(0, tk.END)
    ent_pw.delete(0, tk.END)

# 메인 윈도우 생성
root = tk.Tk()
root.title("tk")
root.resizable(False, False)  # 창 크기 고정

# ──────────── 위젯 생성 및 배치 ────────────
# 1행: 아이디 레이블 + 엔트리
lbl_id = tk.Label(root, text="아이디")
lbl_id.grid(row=0, column=0, padx=5, pady=5, sticky="e")

ent_id = tk.Entry(root)
ent_id.grid(row=0, column=1, padx=5, pady=5)

# 2행: 패스워드 레이블 + 엔트리 (입력 내용 숨김)
lbl_pw = tk.Label(root, text="패스워드")
lbl_pw.grid(row=1, column=0, padx=5, pady=5, sticky="e")

ent_pw = tk.Entry(root, show="*")
ent_pw.grid(row=1, column=1, padx=5, pady=5)

# 3행: 로그인 • 취소 버튼
btn_login = tk.Button(root, text="로그인", width=10, command=on_login)
btn_login.grid(row=2, column=0, padx=5, pady=10)

btn_cancel = tk.Button(root, text="취소", width=10, command=on_cancel)
btn_cancel.grid(row=2, column=1, padx=5, pady=10)

# ──────────── 그리드 컬럼 너비 조정 ────────────
root.grid_columnconfigure(0, weight=0)  # 첫 번째 컬럼(레이블)은 최소 크기
root.grid_columnconfigure(1, weight=1)  # 두 번째 컬럼(입력창+버튼)은 늘어날 수 있도록

# 이벤트 루프 시작
root.mainloop()
