from tkinter import *
def cal_func():
    gui=Tk()
    gui.geometry("330x350")
    gui.title("NoobNote Calculator")
    gui.iconbitmap("icon.ico")
    gui.resizable(False, False)
    gui.configure(bg="#282923")

    def calc1():
        b = txt1.get()
        txt1.delete(0, END)
        b1 = b + btn1["text"]
        txt1.insert(0, b1)

    def calc2():
        b = txt1.get()
        txt1.delete(0, END)
        b1 = b + btn2["text"]
        txt1.insert(0, b1)
    def calc3():
        b = txt1.get()
        txt1.delete(0, END)
        b1 = b + btn3["text"]
        txt1.insert(0, b1)
    def calc4():
        b = txt1.get()
        txt1.delete(0, END)
        b1 = b + btn4["text"]
        txt1.insert(0, b1)
    def calc5():
        b = txt1.get()
        txt1.delete(0, END)
        b1 = b + btn5["text"]
        txt1.insert(0, b1)
    def calc6():
        b = txt1.get()
        txt1.delete(0, END)
        b1 = b + btn6["text"]
        txt1.insert(0, b1)
    def calc7():
        b = txt1.get()
        txt1.delete(0, END)
        b1 = b + btn7["text"]
        txt1.insert(0, b1)
    def calc8():
        b = txt1.get()
        txt1.delete(0, END)
        b1 = b + btn8["text"]
        txt1.insert(0, b1)
    def calc9():
        b = txt1.get()
        txt1.delete(0, END)
        b1 = b + btn9["text"]
        txt1.insert(0, b1)
    def calc0():
        b = txt1.get()
        txt1.delete(0, END)
        b1 = b + btn0["text"]
        txt1.insert(0, b1)
    x = 0
    def add():
        global x
        add.b = (eval(txt1.get()))
        txt1.delete(0, END)
        x = x + 1
    def subtract():
        global x
        subtract.b = (eval(txt1.get()))
        txt1.delete(0, END)
        x = x + 2
    def get():
        b = txt1.get()
    def equals():
        global x
        if x == 1:
            c = (eval(txt1.get())) + add.b
            calculate()
            txt1.insert(0, c)
        elif x == 2:
            c = subtract.b - (eval(txt1.get()))
            calculate()
            txt1.insert(0, c)
        elif x == 3:
            c = multiply.b*(eval(txt1.get()))
            calculate()
            txt1.insert(0, c)
        elif x == 4:
            c = divide.b/(eval(txt1.get()))
            calculate()
            txt1.insert(0,c)
    def calculate():
        global x
        x = 0
        txt1.delete(0, END)
    def multiply():
        global x
        multiply.b = (eval(txt1.get()))
        txt1.delete(0, END)
        x = x + 3
    def divide():
        global x
        divide.b = (eval(txt1.get()))
        txt1.delete(0, END)
        x = x + 4
    label = Label(gui, text="Calculator", font=("Cascadia", 36), fg="#E23636", bg="#2E2F2B", borderwidth=0)
    txt1 = Entry(gui, width=80, font=("Cascadia", 21), bg="#1B1B1B", fg="#F0F0F0", borderwidth=0)
    btn1 = Button(gui, text="1", font=("Cascadia", 24), command=calc1, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn2 = Button(gui, text="2", font=("Cascadia", 24), command=calc2, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn3 = Button(gui, text="3", font=("Cascadia", 24), command=calc3, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn4 = Button(gui, text="4", font=("Cascadia", 24), command=calc4, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn5 = Button(gui, text="5", font=("Cascadia", 24), command=calc5, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn6 = Button(gui, text="6", font=("Cascadia", 24), command=calc6, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn7 = Button(gui, text="7", font=("Cascadia", 24), command=calc7, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn8 = Button(gui, text="8", font=("Cascadia", 24), command=calc8, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn9 = Button(gui, text="9", font=("Cascadia", 24), command=calc9, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn0 = Button(gui, text="0", font=("Cascadia", 24), command=calc0, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn_addition = Button(gui, text="+", font=("Cascadia", 28), command=add, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn_equals = Button(gui, text="=", font=("Cascadia", 24,), command=equals, bg="#2E2F2B", fg="#E23636", borderwidth=0)
    btn_clear = Button(gui, text="AC", font=("Cascadia", 24,), command=calculate, bg="#2E2F2B", fg="#E23636", borderwidth=0)
    btn_subtract = Button(gui, text="- ", font=("Cascadia", 28), command=subtract, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn_multiplication = Button(gui, text="x", font=("Cascadia", 28), command=multiply, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    btn_division = Button(gui, text="÷", font=("Cascadia", 28), command=divide, bg="#2E2F2B", fg="#5DD8C3", borderwidth=0)
    label.place(x=70,y=0)
    txt1.place(x=0, y=50, height=40,)
    btn1.place(x=30, y=100)
    btn2.place(x=75, y=100)
    btn3.place(x=120, y=100)
    btn4.place(x=30, y=160)
    btn5.place(x=75, y=160)        
    btn6.place(x=120, y=160)
    btn7.place(x=30, y=220)
    btn8.place(x=75, y=220)
    btn9.place(x=120, y=220)
    btn0.place(x=75, y=280)
    btn_addition.place(x=210, y=100)
    btn_equals.place(x=270, y=275)
    btn_clear.place(x=190, y=275)
    btn_subtract.place(x=210, y=175)
    btn_multiplication.place(x=270, y=100)
    btn_division.place(x=270, y=175)
    gui.mainloop()