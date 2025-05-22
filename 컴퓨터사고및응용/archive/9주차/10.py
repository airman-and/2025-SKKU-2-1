from tkinter import *
import time
import random

window = Tk()
canvas=Canvas(window, width=600, height=400)
canvas.pack()

class Ball():
    def __init__(self, color, size):
        self.id=canvas.create_oval(0,0,size,size,fill=color)
        self.dx=random.randint(1,10)
        self.dy=random.randint(1,10)
#move는 이미 파이썬에서 만들어놓은 함수였다.
    def move(self):
        canvas.move(self.id, self.dx, self.dy)
        x0, y0, x1, y1 = canvas.coords(self.id)
        if y1 > canvas.winfo_height() or y0 < 0:
            self.dy = -self.dy
        if x1 > canvas.winfo_width() or x0<0:
            self.dx = -self.dx

'''ball1=Ball('blue', 60)
ball2=Ball('green',100)
ball3=Ball('orange',80)

while True:
    ball1.move()
    ball2.move()
    ball3.move()
    window.update()
    time.sleep(0.05)'''

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
ballList= [Ball(random.choice (colors), 60) for _ in range(30)]
while True:
    for ball in ballList:
        ball.move()
    window.update()
    time.sleep(1/180)



window.mainloop()