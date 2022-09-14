from ast import Delete
from distutils.cmd import Command
from distutils.command.build_scripts import first_line_re
import math
from tkinter import*
from turtle import window_width
window=Tk()
window.geometry("300x400")

e=Entry(window,bg="black",fg="white",width=40)
e.pack()
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    now=e.get()
    global first
    global math
    math="addition"
    first=int(now)
    e.delete(0,END)

def button_sub():
    now=e.get()
    global first
    global math
    math="substract"
    first=int(now)
    e.delete(0,END)

def res():
    second=int(float(e.get()))
    e.delete(0,END)
    if math=="addition":
        res=first+second

        e.insert(0,str(res))
    else:
        e.insert(0,str(first-second))
    
    
    



mybutton=Button(window,text="0",width=10,height=5,command=lambda: button_click(0))
mybutton.place(x=0,y=50)
btn1=Button(window,text="1",width=10,height=5,command=lambda: button_click(1))
btn1.place(x=80,y=50)
mybutton2=Button(window,text="2",width=10,height=5,command=lambda: button_click(2))
mybutton2.place(x=160,y=50)
mybutton3=Button(window,text="3",width=10,height=5,command=lambda: button_click(3))
mybutton3.place(x=0,y=140)
mybutton4=Button(window,text="4",width=10,height=5,command=lambda: button_click(4))
mybutton4.place(x=80,y=140)
mybutton5=Button(window,text="5",width=10,height=5,command=lambda: button_click(5))
mybutton5.place(x=160,y=140)
mybutton6=Button(window,text="6",width=10,height=5,command=lambda: button_click(6))
mybutton6.place(x=0,y=230)
mybutton7=Button(window,text="7",width=10,height=5,command=lambda: button_click(7))
mybutton7.place(x=80,y=230)
mybutton8=Button(window,text="8",width=10,height=5,command=lambda: button_click(8))
mybutton8.place(x=160,y=230)
mybutton9=Button(window,text="9",width=10,height=5,command=lambda: button_click(9))
mybutton9.place(x=0,y=320)
mybutton10=Button(window,text="clear",width=10,height=5,command=button_clear)
mybutton10.place(x=80,y=320)
mybutton11=Button(window,text="=",width=10,height=5,command=res)
mybutton11.place(x=160,y=320)
mybutton12=Button(window,text="+",width=7,height=5,command=button_add)
mybutton12.place(x=240,y=230)
mybutton13=Button(window,text="-",width=7,height=5,command=button_sub)
mybutton13.place(x=240,y=140)
mybutton14=Button(window,text="/",width=7,height=5)
mybutton14.place(x=240,y=50)
mybutton15=Button(window,text="x",width=7,height=5)
mybutton15.place(x=240,y=320)







window.mainloop()