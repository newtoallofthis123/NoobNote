from tkinter import *

font = Tk()
font.title("Font Chooser")
font.iconbitmap("icon.ico")

clicked = StringVar()
clicked.set("Cascadia")

font_options = [
"Cascadia",
"Arial",
"Lucida",
"Calibri",
"Segoe UI",
"Times New Roman",
"Verdana",
"Noto Sans",
"Noto Mono",
"MS Sans Serif",
"Lucida Calligraphy",
"Ink Free",
"Courier",
]

def show():
    user_font = str("'" + clicked.get()+ "'" + ", " + size.get())
    #text.config(font=clicked.get())
    #text.config(font=size.get())
    text.config(font=user_font)
    print(user_font)
    #print(tk_font.names())

drop_font = OptionMenu(font , clicked, *font_options,)
drop_font.pack()

size = Spinbox(font, from_=2, to=128, width=8)
size.pack()

text = Text(font,)
text.pack()

button = Button(font, command=show).pack()

font.mainloop()