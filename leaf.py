from tkinter import *
import pyqrcode
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter.messagebox import askokcancel
from tkinter import filedialog
import webbrowser
import os

def generate():
    if name.get():
        global qr_name
        global qr_xbm
        qr = pyqrcode.create(data.get())
        qr_name = str(name.get()) + ".png"
        qr.png((qr_name), scale=10)
        label.config(text="Qr-Code Generated")
        showinfo("QR-Code Generated", "QR-Code generated. To open it, click the open button, or check the in directory you saved Leaf")
    else:
        qr = pyqrcode.create(data.get())
        qr_name = "Leaf QrCode.png"
        qr.png((qr_name), scale=10)
        label.config(text="Qr-Code Generated")
        showinfo("QR-Code Generated", "QR-Code with deflaut name generated. To open it, click the open button, or check the in directory you saved Leaf")

def openqr():
    try:
        file = qr_name
        os.system('"%s"' %file)
        label_text = str(file) + "Opened"
    except:
        showerror("No file found", "No Qr-Code saved to open found")

def open_any():
    try:
        choice = askokcancel("Go to the previous Directory", "This will now open a filedialog in the direcotry Test. Test is a directory in the directory you store Leaf. Just move back a direcotry to see all the QR-Codes")
        if choice:
            try:
                file = filedialog.askopenfilenames(initialdir='Test', title="Choose a Qr-Code", filetypes=(("Image Files", "*.png"), ("Image Files", "*.jpg")))
                os.system('"%s"' %file)
                label_text = str(file) + "Opened"
                label.config(text=label_text)
            except:
                showerror("No file found", "No Qr-Code selected")
        else:
            pass
    except:
        showerror("No file found", "No Qr-Code selected")
        
def delqr():
    try:
        file = qr_name
        os.remove(file)
        label_text = str(file) + "Deleted"
        label.config(text=label_text)
    except:
        showerror("No file found", "No Qr-Code saved to delete")

def del_any():
    try:
        choice = askokcancel("Go to the previous Directory", "This will now open a filedialog in the direcotry Test. Test is a directory in the directory you store Leaf. Just move back a direcotry to see all the QR-Codes")
        if choice:
            try:
                file = filedialog.askopenfilenames(initialdir='Test', title="Choose a Qr-Code", filetypes=(("Image Files", "*.png"), ("Image Files", "*.jpg")))
                os.remove(file)
                label_text = str(file) + "Deleted"
                label.config(text=label_text)
            except:
                showerror("No file found", "No Qr-Code saved to delete")
        else:
            pass
    except:
        showerror("No file found", "No Qr-Code saved to delete")

def del_all():
    try:
        
        for file in os.listdir(): 
            if file.endswith('.png'):
                os.remove(file) 
                showinfo("Deleted", "All Qr-Code Generated with Leaf Deleted. To save any Qr-Codes you Generated, transfer it from the directory you saved leaf to some other directory. ")
    except:
        showerror("No files found", "No Qr-Codes saved to delete")
    
Author = "I wrote Leaf because I needed a simple QR-Generator which is light-weight, safe and private. It is also very easy to use. It is also free and open source. You can check the code at https://github.com/newtoallofthis123/leaf. Leaf is written purely in python. It is a beginner friendly project. Hope you enjoy using it."    
About = "Leaf Qr-Code is a small project I made to learn tkinter. This is purely written in python. It is free and open source. It has no telementry and is completely safe and private. Check out some of my other projects at https://newtoallofthis123.github.io/About"
    
def openNoobweb():
    webbrowser.open("https://newtoallofthis123.github.io/About")
    
def showInfo():
    showinfo("About NoobNote", About)

def aboutAuthor():
    showinfo("NoobScience", Author)
    
def projects():
    webbrowser.open("https://github.com/newtoallofthis123")
    
def openleafweb():
    webbrowser.open("https://newtoallofthis123.github.io/leaf")

def source():
    webbrowser.open("https://github.com/newtoallofthis123/leaf")

def issue():
    webbrowser.open("https://github.com/newtoallofthis123/leaf/issues")
    
def quit1(e):
    qrCode.quit()

def doc(e):
    docs = Tk()
    docs.title("Leaf Qr-Code Generator Docs")
    docs.iconbitmap('icon.ico')
    readme = 'readme.txt'
    file = open(readme, 'r')
    content = file.read()
    textWidth = gui.winfo_screenwidth()
    textHeight = int(gui.winfo_screenheight())
    scroll_text = Scrollbar(docs,)
    scroll_text.pack(side=RIGHT, fill=Y)
    horizontal_scroll = Scrollbar(docs,orient='horizontal')
    horizontal_scroll.pack(side=BOTTOM, fill=X, ipadx=10)
    doc_text = Text(docs, width=textWidth, height=textHeight, font=("Cascadia", 16), selectbackground="#330fff", selectforeground="black", undo=True, yscrollcommand=scroll_text.set, wrap="none", xscrollcommand=horizontal_scroll.set)
    doc_text.pack()
    doc_text.insert(END, content)
    file.close()

qrCode = Tk()
qrCode.geometry('500x500')
qrCode.title("Leaf Qr-Code Generator")
qrCode.configure(bg="black")
qrCode.iconbitmap('icon.ico')

title = Label(qrCode, text="Leaf QrCode Generator", fg="#3FFFAB", bg="black", borderwidth=0, font=("Cascadia", 24))
title.pack(padx=10, pady=10, ipady=6)

data_title = Label(qrCode, text="Enter the data", fg="black", bg="#FB3649", borderwidth=0, font=("Cascadia", 18))
data_title.pack(padx=10,pady=4, ipady=4)

data = Entry(qrCode, fg="white", bg="#002240", borderwidth=0, font=("Cascadia", 16), width=30)
data.pack(padx=10,pady=4, ipady=6)

name_title = Label(qrCode, text="Enter Qr-Code Name", fg="black", bg="#00F7E3", borderwidth=0, font=("Cascadia", 18))
name_title.pack(padx=10, pady=4, ipady=4)

name = Entry(qrCode,fg="white", bg="#002240", borderwidth=0, font=("Cascadia", 16), width=30)
name.pack(padx=10, pady=10, ipady=6)

generate_btn = Button(qrCode, text="Generate", command=generate, font=("Cascadia", 14), fg="black", bg="#A9F700")
generate_btn.pack(padx=10, pady=10, ipady=3)

open_title = Label(qrCode, text="Press open to open the saved Qr-Code in your deflaut photoviewer", fg="#E8EDDD", bg="black", borderwidth=0, font=("Cascadia", 8))
open_title.pack(padx=10,)

open_btn = Button(qrCode, text="Open", command=openqr, font=("Cascadia", 14), fg="black", bg="#A9F700")
open_btn.pack(padx=10, pady=10, ipady=3)

about = Label(qrCode,text = "Made by NoobScience",font = ("Cascadia", 16),bg = "black",fg = "#C5FFB8",)
about.pack(fill=X, pady=10)

label = Label(qrCode, text="Enter data, name and click generate", font=("Cascadia", 8), fg="white", bg="black")
label.pack()

_menu = Menu(qrCode)
qrCode.config(menu=_menu)
file = Menu(_menu, tearoff=False)
_menu.add_cascade(label="File", menu=file)
file.add_command(label="Open current Qr-code", command=openqr)
file.add_command(label="Open any Qr-code", command=open_any)
file.add_separator()
file.add_command(label="Generate Qr-Code", command=generate)
file.add_separator()
file.add_command(label="Exit", command=qrCode.quit())

edit = Menu(_menu, tearoff=False)
_menu.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Delete Generated QR-Code", command=delqr)
edit.add_command(label="Delete any QR-Code", command=del_any)
edit.add_command(label="Delete all QR-Codes", command=del_all)

about = Menu(_menu, tearoff=False)
_menu.add_cascade(label="Help", menu=about)
about.add_command(label="Read the Docs", command=lambda: doc(False))
about.add_command(label="About Author", command=aboutAuthor)
about.add_command(label="About Leaf", command=showInfo)
about.add_command(label="NoobScience Website", command=openNoobweb)
about.add_command(label="Leaf Website", command=openleafweb)
about.add_command(label="View Source Code", command=source)
about.add_command(label="Report a Issue", command=issue)    
about.add_command(label="Some of my other projects", command=projects)

qrCode.bind('<Control-q>', quit1)

qrCode.mainloop()
