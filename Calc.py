from tkinter import *

def click_1():
    txt.insert("end",'1')
def click_2():
    txt.insert("end",'2')
def click_3():
    txt.insert("end",'3')
def click_4():
    txt.insert("end",'4')
def click_5():
    txt.insert("end",'5')
def click_6():
    txt.insert("end", '6')
def click_7():
    txt.insert("end", '7')
def click_8():
    txt.insert("end", '8')
def click_9():
    txt.insert("end", '9')
def click_0():
    txt.insert("end", '0')
def click_Point():
    txt.insert("end", '.')
def click_Delete():
    txt.delete(len(txt.get())-1, END)
def click_FB():
    txt.insert("end", '(')
def click_SB():
    txt.insert("end", ')')
def click_Plus():
    txt.insert("end",'+')
def click_Minus():
    txt.insert("end",'-')
def click_Mult():
    txt.insert("end", '*')
def click_Div():
    txt.insert("end", '/')
def click_Eq():
    res = txt.get()
    txtCache.insert(END, eval(res))

def CreateButtons():
    size = 70
    startX = 5
    startY = 70

    btn1 = Button(window, text="1", command=click_1)
    btn1.place(x=startX, y=startY, width=size, height=size)
    btn2 = Button(window, text="2", command=click_2)
    btn2.place(x=startX + size, y=startY, width=size, height=size)
    btn3 = Button(window, text="3", command=click_3)
    btn3.place(x=startX + size * 2, y=startY, width=size, height=size)
    btn4 = Button(window, text="4", command=click_4)
    btn4.place(x=startX, y=startY + size, width=size, height=size)
    btn5 = Button(window, text="5", command=click_5)
    btn5.place(x=startX + size, y=startY + size, width=size, height=size)
    btn6 = Button(window, text="6", command=click_6)
    btn6.place(x=startX + size * 2, y=startY + size, width=size, height=size)
    btn7 = Button(window, text="7", command=click_7)
    btn7.place(x=startX, y=startY + size * 2, width=size, height=size)
    btn8 = Button(window, text="8", command=click_8)
    btn8.place(x=startX + size, y=startY + size * 2, width=size, height=size)
    btn9 = Button(window, text="9", command=click_9)
    btn9.place(x=startX + size * 2, y=startY + size * 2, width=size, height=size)
    btn0 = Button(window, text="0", command=click_0)
    btn0.place(x=startX, y=startY + size * 3, width=size * 2, height=size)
    btnPoint = Button(window, text=".", command=click_Point)
    btnPoint.place(x=startX + size * 2, y=startY + size * 3, width=size, height=size)
    btnDelete = Button(window, text="←", command=click_Delete)
    btnDelete.place(x=startX + size * 3, y=startY, width=size, height=size)
    btnEq = Button(window, text="=", command=click_Eq)
    btnEq.place(x=startX + size * 4, y=startY, width=size, height=size)
    btnFirstBracket = Button(window, text="(", command=click_FB)
    btnFirstBracket.place(x=startX + size * 3, y=startY + size, width=size, height=size)
    btnSecondBracket = Button(window, text=")", command=click_SB)
    btnSecondBracket.place(x=startX + size * 4, y=startY + size, width=size, height=size)
    btnPlus = Button(window, text="+", command=click_Plus)
    btnPlus.place(x=startX + size * 3, y=startY + size * 2, width=size, height=size)
    btnMinus = Button(window, text="-", command=click_Minus)
    btnMinus.place(x=startX + size * 4, y=startY + size * 2, width=size, height=size)
    btnMult = Button(window, text="*", command=click_Mult)
    btnMult.place(x=startX + size * 3, y=startY + size * 3, width=size, height=size)
    btnDiv = Button(window, text="/", command=click_Div)
    btnDiv.place(x=startX + size * 4, y=startY + size * 3, width=size, height=size)

window = Tk()
window.title("Калькулятор")
window.geometry('360x400')

txt = Entry(window, width = 30, font = ("Arial", 25))
txt.pack(fill=X, pady=6)

txtCache = Text(height=1, wrap="none")
txtCache.place(y=50)

CreateButtons()

list = ()

window.mainloop()