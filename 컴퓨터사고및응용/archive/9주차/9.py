from tkinter import *
from tkinter.colorchooser import askcolor

# 설정 상수
DEFAULT_PEN_SIZE = 1.0
DEFAULT_COLOR = "black"
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter 그림판")

        self.pen_size = DoubleVar(value=DEFAULT_PEN_SIZE)
        self.color = DEFAULT_COLOR
        self.mode = "pen"
        self.old_x = None
        self.old_y = None

        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        # 버튼들
        Button(self.root, text="펜", command=self.use_pen).grid(row=0, column=0, sticky=W)
        Button(self.root, text="브러쉬", command=self.use_brush).grid(row=0, column=1, sticky=W)
        Button(self.root, text="색상선택", command=self.choose_color).grid(row=0, column=2, sticky=W)
        Button(self.root, text="지우개", command=self.use_eraser).grid(row=0, column=3, sticky=W)
        Button(self.root, text="모두삭제", command=self.clear_canvas).grid(row=0, column=4, sticky=W)

        # 선 굵기 조절
        Scale(self.root, variable=self.pen_size, from_=1, to=10, orient=VERTICAL).grid(row=1, column=5, sticky=N)

        # 캔버스
        self.canvas = Canvas(self.root, bg="white", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.grid(row=1, column=0, columnspan=5)

    def bind_events(self):
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    # 모드 설정 함수들
    def use_pen(self):
        self.mode = "pen"

    def use_brush(self):
        self.mode = "brush"

    def choose_color(self):
        color = askcolor(color=self.color)[1]
        if color:
            self.color = color

    def use_eraser(self):
        self.mode = "erase"

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        fill_color = "white" if self.mode == "erase" else self.color
        width = self.pen_size.get() * (3 if self.mode == "brush" else 1)

        if self.old_x and self.old_y:
            self.canvas.create_line(
                self.old_x, self.old_y, event.x, event.y,
                width=width, fill=fill_color,
                capstyle=ROUND, smooth=True
            )
        self.old_x, self.old_y = event.x, event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

# 실행
if __name__ == "__main__":
    root = Tk()
    app = PaintApp(root)
    root.mainloop()
