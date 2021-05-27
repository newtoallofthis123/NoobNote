# Application Name: NoobNote
# Version: v.0.1
# Author: NoobScience
# Author Website: https://newtoallofthis123.github.io/About
# Application Docs and Trobule Shooting Website: https://newtoallofthis123.github.io/NoobNote

# Defining path for linux 
#! /usr/bin/env python3

from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
from tkinter.messagebox import showerror
import webbrowser
try:
    import os, sys
    import win32print
    import win32api
except:
    pass

def main():
    gui = Tk()
    gui.title("NoobNote")
    gui.iconbitmap('icon.ico')
    gui.geometry("600x600")
    global fsVar
    fsVar = False
    gui.attributes('-fullscreen',fsVar)

    global openFilename
    openFilename = False

    global selectedText
    selectedText = False

    def newFile(e):
        text.delete("1.0", END)
        gui.title('New File - NoobNote')
        status_bar.config(text="New File    ")

    def openFile(e):
        try:
            text.delete("1.0", END)
            #gui.title('New File - NoobScience')
            #status_bar.config(text="N    ")
            file = filedialog.askopenfilename(initialdir='I:\python-dev-bin', title="Choose A File", filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"),  ("All Files", "*.*")))
            if file:
                global openFilename
                openFilename = file
            name = file
            status_bar.config(text=f'{name}  opened')
            gui.title(f'{name} - NoobNote')

            file = open(file, 'r')
            content = file.read()
            text.insert(END, content)
            file.close()
        except:
            showerror("Not opened", "No file name given")
        
    About = "NoobNote is a beginner friendly python project.It is registered under the MIT lisence. Feel free to use it however you like"
    Author = "I am a learning python and wrote this to learn tkinter. Check out some of my other projects at https://github.com/newtoallofthis123. Also Check out my Website for other projects https://newtoallofthis123.github.io/About"

    def saveAs(e):
        try:
            file = filedialog.asksaveasfilename(defaultextension=".*", initialdir='I:\python-dev-bin', title="Save file as", filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"),  ("All Files", "*.*")))
            if file:
                name = file
                status_bar.config(text=f'{name}  opened')
                gui.title(f'{name} - NoobScience')

                file = open(file, 'w')
                file.write(text.get(1.0, END))
                file.close()
                status_bar.config(text='File saved')
        except:
            showerror("Not Saved", "No file name given")

    def saveFile(e):
        try:
            global openFilename
            if openFilename:
                file = openFilename
                file = open(file, 'w')
                file.write(text.get(1.0, END))
                file.close()
                status_bar.config(text='File saved')
            else:
                saveAs(e)
        except:
            showerror("Not Saved", "No file saved")

    def cutText(e):
        global selectedText
        if e:
            selectedText = gui.clipboard_get()
        else:
            if text.selection_get():
                selectedText = text.selection_get()
                status_bar.config(text='cut selected text')
                text.delete("sel.first", "sel.last")
                gui.clipboard_clear()
                gui.clipboard_append(selectedText)	

    def copyText(e):
        global selectedText
        if e:
            selectedText = gui.clipboard_get()
        if text.selection_get():
            selectedText = text.selection_get()
            status_bar.config(text='copied selected text')
            gui.clipboard_clear()
            gui.clipboard_append(selectedText)

    def pasteText(e):
        global selectedText
        if e:
            selectedText = gui.clipboard_get()
        else:
            if selectedText:
                positionCursor = text.index(INSERT)
                text.insert(positionCursor, selectedText)
                status_bar.config(text='pasted')

    def boldText(e):
        try:
            boldFont = font.Font(text, text.cget("font"))
            boldFont.configure(weight="bold")

            text.tag_configure("bold", font=boldFont)
            current_tags = text.tag_names("sel.first")
            if "bold" in current_tags:
                text.tag_remove("bold",  "sel.first", "sel.last")
            else:
                text.tag_add("bold", "sel.first", "sel.last")
        except:
            showerror("Selection", "No text selected")

    def italicText(e):
        try:
            italicFont = font.Font(text, text.cget("font"))
            italicFont.configure(slant="italic")

            text.tag_configure("italic", font=italicFont)
            current_tags = text.tag_names("sel.first")
            if "italic" in current_tags:
                text.tag_remove("italic",  "sel.first", "sel.last")
            else:
                text.tag_add("italic", "sel.first", "sel.last")
        except:
            showerror("Selection", "No text selected")

    def underlineText(e):
        try:
            underlineFont = font.Font(text, text.cget("font"))
            underlineFont.configure(underline=True)

            text.tag_configure("underline", font=underlineFont)
            current_tags = text.tag_names("sel.first")
            if "underline" in current_tags:
                text.tag_remove("underline",  "sel.first", "sel.last")
            else:
                text.tag_add("underline", "sel.first", "sel.last")
        except:
            showerror("Selection", "No text selected")

    def textColor():
        colorChoice = colorchooser.askcolor()[1]
        status_bar.config(text=f'Selected Font Color Set to: {colorChoice}')
        bgFont = font.Font(text, text.cget("font"))
        #bgFont.configure(slant="italic")

        text.tag_configure("colored", font=bgFont, foreground=colorChoice)
        current_tags = text.tag_names("sel.first")
        if "colored" in current_tags:
            text.tag_remove("colored",  "sel.first", "sel.last")
        else:
            text.tag_add("colored", "sel.first", "sel.last")

    def ColorAllText():
        colorChoice = colorchooser.askcolor()[1]
        status_bar.config(text=f'All Font Color Set to: {colorChoice}')
        if colorChoice:
            text.config(fg=colorChoice)

    def bgColor():
        colorChoice = colorchooser.askcolor()[1]
        status_bar.config(text=f'Background Color set to : {colorChoice}')
        if colorChoice:
            text.config(bg=colorChoice)

    def showInfo():
        showinfo("About NoobNote", About)
        
    def aboutAuthor():
        showinfo("NoobScience", Author)

    def docOpen():
        try:
            text.delete(1.0, END)
            doc = open("README3.txt")
            gui.title("NoobNote Docs")
            docContent = doc.read()
            text.insert(END, docContent)
        except:
            showerror("Doc", "README.txt not Found")
        
    def fullScreen(e):
        global fsVar
        if fsVar:
            gui.attributes('-fullscreen',False)
            fsVar = False
        else:
            fsVar = True
            gui.attributes('-fullscreen',True)
        
    def lightTheme(e):
        #colorChoice = colorchooser.askcolor()[1]
        status_bar.config(text=f'Theme set to : light', bg="white", fg="black")
        gui.config(bg="white")
        text.config(fg = "black",bg="white", selectbackground="blue", selectforeground="white")
        
    def darkTheme(e):
        status_bar.config(text=f'Theme set to : dark', bg="white", fg="black")
        gui.config(bg="black")
        text.config(fg="white",bg="black", selectbackground="yellow", selectforeground="black")
        
    def timeDate():
        from datetime import datetime
        from datetime import date
        current_t = datetime.now()
        current_date = str(date.today())
        current_t_f = current_t.strftime("%H:%M:%S")
        timeAnddate = (f'{current_t_f} {current_date}')
        text.insert(END, timeAnddate)

    def selectAll(e):
        text.tag_add('sel', '1.0', 'end')
        status_bar.config(text='All Text Selected')

    def clearAll(e):
        text.delete(1.0, END)
        status_bar.config(text='All Text Delted')
        
    def openNoobweb():
        webbrowser.open("https://newtoallofthis123.github.io/About")
        
    def openWeb():
        webbrowser.open("https://newtoallofthis123.github.io/NoobNote")
        
    def source():
        webbrowser.open("https://github.com/newtoallofthis123/NoobNote")

    def projects():
        webbrowser.open("https://github.com/newtoallofthis123")

    def issues():
        webbrowser.open("https://github.com/newtoallofthis123/NoobNote/issues")
    
    def newWin(e):
        newWinChoice = askquestion("New Window", "Do you want to open a new NoobNote Window")
        if newWinChoice == 'yes':
            import NoobNote
        else:
            pass

    def printFile(e):
        try:
            printerName = win32print.GetDefaultPrinter()
            printAsk = f'Do you want to print with your deflaut printer: {printerName} ? You can change your default printer in your system preferences'
            printChoice = askquestion("Print File?", printAsk)
            if printChoice == 'yes':
                fileToprint = filedialog.askopenfilename(initialdir="/", title="Open File", filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")))
                if fileToprint:
                    win32api.ShellExecute(0, "print", fileToprint, None, ".", 0)
            elif printChoice == 'no':
                showerror("Printing Aborted", "Printing Aborted")
            else:
                showerror("Error", "Something went wrong. Printing Aborted")
        except:
            showerror("Unable to Print", "Something went wrong.Printer is most likely offline. Try again when the printer is online or report this issue to https://github.com/newtoallofthis123/NoobNote/issues")
            
    def newWinmain(e):
        main()

    def quit1(e):
        gui.quit()

    root = Frame(gui)
    root.pack()


    scroll_text = Scrollbar(root,)
    scroll_text.pack(side=RIGHT, fill=Y)

    horizontal_scroll = Scrollbar(root,orient='horizontal')
    horizontal_scroll.pack(side=BOTTOM, fill=X, ipadx=10)

    textWidth = gui.winfo_screenwidth()
    textHeight = int(gui.winfo_screenheight())

    text = Text(root, width=textWidth, height=textHeight, font=("Cascadia", 16), selectbackground="#330fff", selectforeground="black", undo=True, yscrollcommand=scroll_text.set, wrap="none", xscrollcommand=horizontal_scroll.set)
    text.pack()

    menu = Menu(gui)
    gui.config(menu=menu)

    fileMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=lambda: newFile(False))
    fileMenu.add_command(label="New Window", command=lambda: newWinmain(False))
    fileMenu.add_command(label="Open", command=lambda: openFile(False))
    fileMenu.add_command(label="Save", command=lambda: saveFile(False))
    fileMenu.add_command(label="SaveAs", command=lambda: saveAs(False))
    fileMenu.add_separator()
    fileMenu.add_command(label="Print", command=lambda: printFile(False))
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=lambda: quit1(False))

    editMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Cut", command=lambda: cutText(False))
    editMenu.add_command(label="Copy", command=lambda: copyText(False))
    editMenu.add_command(label="Paste", command=lambda: pasteText(False))
    editMenu.add_command(label="Select All", command=lambda: selectAll(False))
    editMenu.add_command(label="Clear All", command=lambda: clearAll(False))
    editMenu.add_separator()
    editMenu.add_command(label="Undo", command=text.edit_undo)
    editMenu.add_command(label="Redo", command=text.edit_redo)

    textFormatMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Format", menu=textFormatMenu)
    textFormatMenu.add_command(label="Bold", command=lambda: boldText(False))
    textFormatMenu.add_command(label="Italic", command=lambda: italicText(False))
    textFormatMenu.add_command(label="Underline", command=lambda: underlineText(False))

    viewMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="View", menu=viewMenu)
    viewMenu.add_command(label="Toggle FullScreen", command=lambda: fullScreen(False))
    viewMenu.add_command(label="Docs", command=docOpen)
    viewMenu.add_separator()
    viewMenu.add_command(label="Time and Date", command=timeDate)


    colorMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Color", menu=colorMenu)
    colorMenu.add_command(label="All Text Color", command=ColorAllText)
    colorMenu.add_command(label="BackGround", command=bgColor)
    colorMenu.add_command(label="Selected Text Color", command=textColor)
    colorMenu.add_separator()
    colorMenu.add_command(label="Light Theme", command=lambda: lightTheme(False))
    colorMenu.add_command(label="Dark Theme", command=lambda: darkTheme(False))

    aboutMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Help", menu=aboutMenu)
    aboutMenu.add_command(label="About Author", command=aboutAuthor)
    aboutMenu.add_command(label="About NoobNote", command=showInfo)
    aboutMenu.add_command(label="NoobScience Website", command=openNoobweb)
    aboutMenu.add_command(label="NoobNote Website", command=openWeb)
    aboutMenu.add_command(label="Fork NoobNote", command=source)
    aboutMenu.add_command(label="Report any issues", command=issues)
    aboutMenu.add_command(label="Some of my other projects", command=projects)
    aboutMenu.add_separator()

    status_bar = Label(root, text='Ready        ', anchor=E)
    status_bar.pack(fill=X, side=BOTTOM, ipady=15)
    #status_bar.grid(row=0, column=1)

    scroll_text.config(command=text.yview)
    horizontal_scroll.config(command=text.xview)

    gui.bind('<Control-Key-x>', cutText)
    gui.bind('<Control-Key-c>', copyText)
    gui.bind('<Control-Key-v>', pasteText)
    gui.bind('<Control-F>', fullScreen)
    gui.bind('<Control-f>', fullScreen)
    gui.bind('<Control-L>', lightTheme)
    gui.bind('<Control-l>', lightTheme)
    gui.bind('<Control-d>', darkTheme)
    gui.bind('<Control-D>', darkTheme)
    gui.bind('<Control-A>', selectAll)
    gui.bind('<Control-a>', selectAll)
    gui.bind('<Control-X>', clearAll)
    gui.bind('<Control-x>', clearAll)
    gui.bind('<Control-b>', boldText)
    gui.bind('<Control-i>', italicText)
    gui.bind('<Control-u>', underlineText)
    gui.bind('<Control-h>', docOpen)
    gui.bind('<Control-H>', docOpen)
    gui.bind('<Control-o>', openFile)
    gui.bind('<Control-n>', newFile)
    gui.bind('<Control-S>', saveAs)
    gui.bind('<Control-s>', saveFile)
    gui.bind('<Control-N>', newWinmain)
    gui.bind('<Control-q>', quit1)
    gui.bind('<Control-p>', printFile)


    gui.mainloop()

if __name__ == '__main__':
    main()
