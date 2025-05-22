from tkinter import *
import random

answer = random.randint(1, 100)

def guessing():
    guess = int(guessField.get())

    if guess > answer:
        msg = '높음'
    elif guess < answer:
        msg = '낮음'
    else:
        msg = '정답'

    resultLabel['text'] = msg
    guessField.delete(0, END)

def reset():
    global answer
    answer = random.randint(1, 100)
    resultLabel['text'] = '다시해라'

window = Tk()
window.configure(bg='white')
window.title('숫자를 맞춰')

window.geometry('500x80')  # Corrected format
titleLabel = Label(window, text='숫자 게임에 온 걸 환영해', bg='white')
titleLabel.pack()

guessField = Entry(window)
guessField.pack(side="top")

tryButton = Button(window, text="시도", fg="green", bg="white", command=guessing)
tryButton.pack(side="left")

resetButton = Button(window, text="초기화", fg="red", bg="white", command=reset)
resetButton.pack(side="right")

resultLabel = Label(window, text="1 부터 100 사이의 숫자를 입력하시오.", bg="white")
resultLabel.pack(side="bottom")

window.mainloop()