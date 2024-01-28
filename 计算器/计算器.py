from tkinter import *
import tkinter.messagebox
import math
from PIL import Image, ImageTk

from distutils.cmd import Command
def alert(text,title=""):
    tkinter.messagebox.showinfo(title=title,message=text)

def btn01onclick():
    alert(math.pow(float(entry01.get()),2))
def btn02onclick():
    alert(math.sqrt(float(entry01.get())))
def btn03onclick():
    alert(float(entry01.get())*float(entry02.get()))
def btn04onclick():
    alert(float(entry01.get())/float(entry02.get()))
def btn05onclick():
    alert(float(entry01.get())+float(entry02.get()))
def btn06onclick():
    alert(float(entry01.get())-float(entry02.get()))
# def btn07onclick():
#     pass
# def btn08onclick():
#     pass
window = Tk()
pow_image = ImageTk.PhotoImage(Image.open("image\\pow.png"))
chu_image = ImageTk.PhotoImage(Image.open("image\\除.png"))
cheng_image = ImageTk.PhotoImage(Image.open("image\\乘.png"))
g_image = ImageTk.PhotoImage(Image.open("image\\根号.png"))
jia_image = ImageTk.PhotoImage(Image.open("image\\加.png"))
jian_image = ImageTk.PhotoImage(Image.open("image\\减.png"))
text01 = Label(window,text="a")
entry01 = Entry(window)
text02 = Label(window,text="b")
entry02 = Entry(window)
btn01 = Button(window, text="a的平方",image=pow_image,compound=RIGHT,command=btn01onclick)
btn02 = Button(window, text="根号a",image=g_image,compound=RIGHT,command=btn02onclick)
btn03 = Button(window, text="a × b",image=cheng_image,compound=RIGHT,command=btn03onclick)
btn04 = Button(window, text="a ÷ b",image=chu_image,compound=RIGHT,command=btn04onclick)
btn05 = Button(window, text="a + b",image=jia_image,compound=RIGHT,command=btn05onclick)
btn06 = Button(window, text="a - b",image=jian_image,compound=RIGHT,command=btn06onclick)
# btn07 = Button(window, text="换")
# btn08 = Button(window, text="换")



text01.pack()
entry01.pack()
text02.pack()
entry02.pack()
btn01.pack(side=LEFT)
btn02.pack(side=LEFT)
btn03.pack(side=LEFT)
btn04.pack(side=LEFT)
btn05.pack(side=LEFT)
btn06.pack(side=LEFT)
# btn07.pack(side=LEFT)
# btn08.pack(side=LEFT)
window.mainloop()
