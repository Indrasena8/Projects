from tkinter import *

def btnClick(number):
    global operator
    operator=operator+str(number)
    text_Input.set(operator)

def btnClear():
    global operator
    operator=""
    text_Input.set("")

def btnEquals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
cal = Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()
txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)
b7=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:btnClick(7),bg="powder blue").grid(row=1,column=0)
b8=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:btnClick(8),bg="powder blue").grid(row=1,column=1)
b9=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9),bg="powder blue").grid(row=1,column=2)
Add=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnClick('+'),bg="powder blue").grid(row=1,column=3)
################################################################################################################
b4=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4),bg="powder blue").grid(row=2,column=0)
b5=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",command=lambda:btnClick(5),bg="powder blue").grid(row=2,column=1)
b6=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6),bg="powder blue").grid(row=2,column=2)
Sub=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnClick('-'),bg="powder blue").grid(row=2,column=3)
################################################################################################################
b1=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1),bg="powder blue").grid(row=3,column=0)
b2=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2),bg="powder blue").grid(row=3,column=1)
b3=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3),bg="powder blue").grid(row=3,column=2)
Mul=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnClick('*'),bg="powder blue").grid(row=3,column=3)
################################################################################################################
b0=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda:btnClick(0),bg="powder blue").grid(row=4,column=0)
Div=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick('/'),bg="powder blue").grid(row=4,column=1)
Equals=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",command=btnEquals,bg="powder blue").grid(row=4,column=3)
clear=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",command=lambda:btnClear(),bg="powder blue").grid(row=4,column=2)

cal.mainloop()
