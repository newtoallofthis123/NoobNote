from tkinter import *
import webbrowser

font = Tk()
font.title("Font Chooser")
font.iconbitmap("icon.ico")

text = Text(font,)
text.pack()

def search():
    choice = text.selection_get()
    lst =  [choice]
    global x
    x = (lst[0].split())
    sear = []
    for word in x:
        y = [word + "+"]
        sear.append(y)
    url = 'https://www.google.com/search?hl=en&q=' + choice
    webbrowser.open(url)
    print(sear)

button = Button(font, command=search)
button.pack()

font.mainloop()


