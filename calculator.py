from tkinter import*
def clicked(num):
    first_num=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(first_num)+str(num))
def add():
    first_number=e1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="addition"
    e1.delete(0,END)
def sub():
    first_number=e1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="sub"
    e1.delete(0,END)
def multy():
    first_number=e1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="multy"
    e1.delete(0,END)
def div():
    first_number=e1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="div"
    e1.delete(0,END)
def clear():
    e1.delete(0,END)
def eq():
    if math=="addition":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_value)+int(new_value))
    if math=="sub":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_value)-int(new_value))
    if math=="multy":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_value)*int(new_value))
    if math=="div":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_value)/int(new_value))
root=Tk()
root.title("hello world")
root.geometry("121x250")
txt=StringVar(None)
e1=Entry(root, textvariable=txt)
e1.place(x=1,y=215)
btn7=Button(text="7",width=3,height=3,command=lambda:clicked(7))
btn7.place(x=1,y=1)
btn8=Button(text="8",width=3,height=3,command=lambda:clicked(8))
btn8.place(x=30,y=1)
btn9=Button(text="9",width=3,height=3,command=lambda:clicked(9))
btn9.place(x=60,y=1)
btn4=Button(text="4",width=3,height=3,command=lambda:clicked(4))
btn4.place(x=1,y=55)
btn5=Button(text="5",width=3,height=3,command=lambda:clicked(5))
btn5.place(x=30,y=55)
btn6=Button(text="6",width=3,height=3,command=lambda:clicked(6))
btn6.place(x=60,y=55)
btn1=Button(text="1",width=3,height=3,command=lambda:clicked(1))
btn1.place(x=1,y=105)
btn2=Button(text="2",width=3,height=3,command=lambda:clicked(2))
btn2.place(x=30,y=105)
btn3=Button(text="3",width=3,height=3,command=lambda:clicked(3))
btn3.place(x=60,y=105)
btnmulty=Button(text="x",width=3,height=3,command=multy)
btnmulty.place(x=90,y=1)
btnneg=Button(text="-",width=3,height=3, command=sub)
btnneg.place(x=90,y=55)
btnpos=Button(text="+",width=3,height=3, command=add)
btnpos.place(x=90,y=105)
btndiv=Button(text="/",width=3,height=3,command=div)
btndiv.place(x=60,y=160)
btneq=Button(text="=",width=3,height=3,command=eq)
btneq.place(x=90,y=160)
btnclear=Button(text="C",width=3,height=3,command=clear)
btnclear.place(x=30,y=160)
btn0=Button(text="0",width=3,height=3,command=lambda:clicked(0))
btn0.place(x=1,y=160)
root.mainloop()