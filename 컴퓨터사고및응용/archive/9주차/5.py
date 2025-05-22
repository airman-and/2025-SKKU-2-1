import random
from tkinter import *

window = Tk()
window.title("가위 바위 보 게임")
Label(window, text='선택하세요', font=('Helvetica', 16)).pack()

frame = Frame(window)
frame.pack()

scissors_image = PhotoImage(file=r"C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\컴퓨터사고및응용\archive\9주차\가위.png")
paper_image = PhotoImage(file=r"C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\컴퓨터사고및응용\archive\9주차\보.png")
rock_image = PhotoImage(file=r"C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\컴퓨터사고및응용\archive\9주차\묵.png")

def decide(human):
    computer = random.choice(["가위", "바위", "보"])
    if computer == "바위":
        computer_image.config(image=rock_image)
    elif computer == "보":
        computer_image.config(image=paper_image)
    else:
        computer_image.config(image=scissors_image)
    if (computer == "바위" and human == "보") or (computer == "보" and human == "가위") or (computer == "가위" and human == "바위"):
        result = "인간 승리!"
    elif computer == human:
        result = "비겼습니다."
    else:
        result = "컴퓨터 승리!"
    output.config(text=f"인간: {human}  컴퓨터: {computer}  결과: {result}")

def pass_s():
    decide("가위")

def pass_r():
    decide("바위")

def pass_p():
    decide("보")

rock = Button(frame, image=rock_image, command=pass_r)
rock.pack(side='left')
paper = Button(frame, image=paper_image, command=pass_p)
paper.pack(side='left')
scissors = Button(frame, image=scissors_image, command=pass_s)
scissors.pack(side='left')

computer_image = Label(window, image=rock_image)
computer_image.pack()

Label(window, text="컴퓨터는 다음을 선택하였다.", font=("Helvetica", 16)).pack()

output = Label(window, text="", font=("Helvetica", 16))
output.pack()

window.mainloop()