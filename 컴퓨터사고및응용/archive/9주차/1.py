from tkinter import*

window = Tk()

Label(window, text="너비").grid(row=0,column=0)
Label(window, text="높이").grid(row=1,column=0)

e1=Entry(window)
e2=Entry(window)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

# Update the file path to the correct location of the image
# Update the file path to the correct location of the image
photo = PhotoImage(file=r"c:/Users/andycho/OneDrive/Desktop/2025 2학년 1학기/컴퓨터사고및응용/archive/Screenshot 2025-05-01 094944.png")
window.photo = photo  # Keep a reference to the PhotoImage object
label = Label(window, image=photo)
label.grid(row=0,column=2,columnspan=2,rowspan=2)

Button(window, text="확대").grid(row=2,column=2)
Button(window,text='축소').grid(row=2,column=3)

window.mainloop()