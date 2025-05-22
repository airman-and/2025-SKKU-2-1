import tkinter as tk

def increase():
    global count
    count += 1
    lbl.config(text=str(count))

def decrease():
    global count
    count -= 1
    lbl.config(text=str(count))

# 메인 윈도우 생성
root = tk.Tk()
root.title("tk")

# 초기 카운터 값
count = 0

# (선택) 버튼들을 감쌀 프레임을 하나 만들어도 됩니다.
frame = tk.Frame(root)
frame.pack(padx=5, pady=5)

# pack 만 사용해서 왼쪽부터 차례대로 붙이기
btn_dec = tk.Button(frame, text="감소", command=decrease)
btn_dec.pack(side='left', padx=5)

lbl = tk.Label(frame, text=str(count), width=5, anchor='center')
lbl.pack(side='left', padx=5)

btn_inc = tk.Button(frame, text="증가", command=increase)
btn_inc.pack(side='left', padx=5)

root.mainloop()
