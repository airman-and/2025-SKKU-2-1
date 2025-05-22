from tkinter import*

WIDTH =  600
HEIGHT = 200
def displayRect():
    canvas.create_rectangle(10,10,WIDTH-10,HEIGHT-10)

def displayOval():
    canvas.create_oval(10, 10, WIDTH - 10, HEIGHT - 10, fill="yellow")

def displayArc():
    canvas.create_arc(10, 10, WIDTH - 10, HEIGHT - 10, start=0, extent=120, width=10, fill='blue')

def displayPolygon():
    canvas.create_polygon(10, 10, WIDTH - 10, HEIGHT - 10, 200, 90, 300, 160)

def displayLine():
    canvas.create_line(10, 10, WIDTH - 10, HEIGHT - 10, fill='green')

def clearCanvas():
    canvas.delete("all")

window=Tk()
canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg='white')
canvas.pack()
frame=Frame(window)
frame.pack()

btRectangle = Button(frame, text="Rectangle", command=displayRect)
btRectangle.grid(row=1, column=0)

btOval = Button(frame, text="Oval", command=displayOval)
btOval.grid(row=1, column=1)

btArc = Button(frame, text="Arc", command=displayArc)
btArc.grid(row=1, column=2)

btPolygon = Button(frame, text="Polygon", command=displayPolygon)
btPolygon.grid(row=1, column=3)

btLine = Button(frame, text="Line", command=displayLine)
btLine.grid(row=1, column=4)

btClear = Button(frame, text="Clear", command=clearCanvas)
btClear.grid(row=1, column=5)

window.mainloop()