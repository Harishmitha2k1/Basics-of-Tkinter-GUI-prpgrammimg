from tkinter import *
top = Tk()
top.geometry("200x100")
radio = IntVar()
rbtn1 = Radiobutton(top, text="red",variable=radio,value="1")
rbtn1.pack()
rbtn2 = Radiobutton(top, text="Green",variable=radio,value="2")
rbtn2.pack()
rbtn3 = Radiobutton(top, text="Blue",variable=radio,value="3")
rbtn3.pack()
top.mainloop()