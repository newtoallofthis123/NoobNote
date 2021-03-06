# Application Name: NoobNote
# Version: v.1.1
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
from tkinter.messagebox import askokcancel
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
        
    About = "NoobNote is a beginner friendly python project.It is registered under the MIT lisence. Feel free to use it however you like. NoobNote is feature rich and can easily replace Notepad for beginners when learning to code or for writing simple files. Hope you enjoy using it."
    Author = "I am a learning python and wrote this to learn tkinter. Check out some of my other projects at https://github.com/newtoallofthis123. Also Check out my Website for other projects https://newtoallofthis123.github.io/About. Hope you enjoy using it."

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

    def docOpen(e):
        try:
            text.delete(1.0, END)
            doc = open("README.txt")
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
        text.config(fg = "black",bg="white", selectbackground="#0618FF", selectforeground="white")
        
    def darkTheme(e):
        status_bar.config(text=f'Theme set to : dark', bg="white", fg="black")
        gui.config(bg="black")
        text.config(fg="white",bg="black", selectbackground="yellow", selectforeground="black")
    
    def relaxTheme(e):
        status_bar.config(text=f'Theme set to : relax', bg="#F2DD2D", fg="black")
        gui.config(bg="#F2DD2D")
        text.config(fg="black",bg="#F2DD2D", selectbackground="#FA9133", selectforeground="black")
        
    def timeDate(e):
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

    def check_for_updates(e):
        import update_check
        update_check.check_updates()
    
    def qr(e):
        try:
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

        except:
            showerror("Error", "Something went wrong. Try again and check if pyqrcode is installed. Use pip install pyqrcode or report the issue at https://github.com/newtoallofthis123/NoobNote/issues")
            
    def month_calendar(e):
        from datetime import datetime
        from datetime import date
        import time
        import calendar    
        date_now = date.today()
        _month = int(date_now.month)
        _year = int(date_now.year)
        cal = calendar.month(_year, _month)
        text.insert(END, cal)
    
    def year_calendar(e):
        from datetime import datetime
        from datetime import date
        import time
        import calendar
        date_now = date.today()
        _month = int(date_now.month)
        _year = int(date_now.year)
        cal = calendar.calendar(_year)
        text.insert(END, cal)
    
    def clock(e):
        try:
            from time import strftime
            clock_widget = Tk()
            clock_widget.geometry("540x100")
            clock_widget.title("Clock Widget")
            clock_widget.iconbitmap("icon.ico")
            def clockconfig():
                time_clock = strftime('%H:%M:%S %p')
                clock_text.config(text = time_clock)
                clock_text.after(1000, clockconfig)
            clock_text = Label(clock_widget, bg="black", fg="#00FF54", font=("Cascadia", 72),borderwidth=0)
            clock_text.pack()
            clockconfig()
            mainloop()
        except:
            print("ShadowGuy123")
                
    def search_google():
        content = text.selection_get()
        url = 'https://www.google.com/search?hl=en&q=' + content
        webbrowser.open(url)
    
    def search_bing():
        content = text.selection_get()
        url = 'https://www.bing.com/search?q=' + content
        webbrowser.open(url)
        
    def search_yt():
        content = text.selection_get()
        url = 'https://www.youtube.com/results?search_query=' + content
        webbrowser.open(url)

    def search_searx():
        content = text.selection_get()
        url = 'https://searx.info/search?q=' + content
        webbrowser.open(url)
    
    def search_github():
        content = text.selection_get()
        url = 'https://github.com/search?q=' + content
        webbrowser.open(url)
    
    def search_vtip():
        content = text.selection_get()
        url = 'https://www.virustotal.com/gui/search/' + content
        webbrowser.open(url)
        
    def encode_64():
        try:
            import base64
            string = text.selection_get()
            string_bytes = string.encode("ascii")
            base64_bytes = base64.b64encode(string_bytes)
            base64_string = base64_bytes.decode("ascii")
            text.insert(END, base64_string)
        except:
            showerror("Error occured", "Something went wrong. Try Again or report the issue at https://github.com/newtoallofthis123/NoobNote/issues")
        
    def decode_64():
        try:
            import base64
            string = text.selection_get()
            string_bytes = string.encode("ascii")
            base64_bytes = base64.b64decode(string_bytes)
            base64_string = base64_bytes.decode("ascii")
            text.insert(END, base64_string)
        except:
            showerror("Error occured", "The selected string is not encoded to decode")
            
    def hash_sha256():
        import hashlib
        content = str(text.selection_get())
        encoded = content.encode()
        hash_str = hashlib.sha256(encoded)
        hash_hexa = hash_str.hexdigest()
        text.insert(END, hash_hexa)
        
    def hash_md5():
        import hashlib
        content = str(text.selection_get())
        encoded = content.encode()
        hash_str = hashlib.md5(encoded)
        hash_hexa = hash_str.hexdigest()
        text.insert(END, hash_hexa)

    def hash_sha1():
        import hashlib
        content = str(text.selection_get())
        encoded = content.encode()
        hash_str = hashlib.sha1(encoded)
        hash_hexa = hash_str.hexdigest()
        text.insert(END, hash_hexa)

    root = Frame(gui)
    root.pack()


    scroll_text = Scrollbar(root,)
    scroll_text.pack(side=RIGHT, fill=Y)

    horizontal_scroll = Scrollbar(root,orient='horizontal')
    horizontal_scroll.pack(side=BOTTOM, fill=X, ipadx=10)

    textWidth = gui.winfo_screenwidth()
    textHeight = int(gui.winfo_screenheight())

    text = Text(root, width=textWidth, height=textHeight, font=("Cascadia", 16), selectbackground="#0618FF", selectforeground="white", undo=True, yscrollcommand=scroll_text.set, wrap="none", xscrollcommand=horizontal_scroll.set, fg="black", bg="white",)
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
    textFormatMenu.add_separator()
    textFormatMenu.add_command(label="Encode in Base64", command=encode_64)
    textFormatMenu.add_command(label="Decode Base64 String", command=decode_64)

    viewMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="View", menu=viewMenu)
    viewMenu.add_command(label="Toggle FullScreen", command=lambda: fullScreen(False))
    viewMenu.add_command(label="Docs", command=lambda: docOpen(False))
    viewMenu.add_separator()
    viewMenu.add_command(label="Time and Date", command=lambda: timeDate(False))
    viewMenu.add_separator()
    viewMenu.add_command(label="Clock Widget", command=lambda: clock(False))
    
    searchMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Search", menu=searchMenu)
    searchMenu.add_command(label="Search with google", command=search_google)
    searchMenu.add_command(label="Search with bing", command=search_bing)
    searchMenu.add_command(label="Search with youtube", command=search_yt)
    searchMenu.add_command(label="Search with searx", command=search_searx)
    searchMenu.add_command(label="Search with github", command=search_github)
    searchMenu.add_command(label="Search url with virustotal", command=search_vtip)
    
    toolsMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Tools", menu=toolsMenu)
    toolsMenu.add_command(label="Qr-Code Generator", command=lambda: qr(False))
    toolsMenu.add_command(label="Insert Month Calendar", command=lambda: month_calendar(False))
    toolsMenu.add_command(label="Insert Year Calendar", command=lambda: year_calendar(False))
    toolsMenu.add_separator()
    toolsMenu.add_command(label="Generate sha256 Hash", command=hash_sha256)
    toolsMenu.add_command(label="Generate md5 Hash", command=hash_md5)
    toolsMenu.add_command(label="Generate sha1 Hash", command=hash_sha1)

    colorMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Color", menu=colorMenu)
    colorMenu.add_command(label="All Text Color", command=ColorAllText)
    colorMenu.add_command(label="BackGround", command=bgColor)
    colorMenu.add_command(label="Selected Text Color", command=textColor)
    colorMenu.add_separator()
    colorMenu.add_command(label="Light Theme", command=lambda: lightTheme(False))
    colorMenu.add_command(label="Dark Theme", command=lambda: darkTheme(False))
    colorMenu.add_command(label="Relaxing Theme", command=lambda: relaxTheme(False))

    aboutMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Help", menu=aboutMenu)
    aboutMenu.add_command(label="About Author", command=aboutAuthor)
    aboutMenu.add_command(label="About NoobNote", command=showInfo)
    aboutMenu.add_command(label="NoobScience Website", command=openNoobweb)
    aboutMenu.add_command(label="Some of my other projects", command=projects)
    aboutMenu.add_separator()
    aboutMenu.add_command(label="Check for Updates", command=lambda: check_for_updates(False))
    aboutMenu.add_separator()
    aboutMenu.add_command(label="NoobNote Website", command=openWeb)
    aboutMenu.add_command(label="Fork NoobNote", command=source)
    aboutMenu.add_command(label="Report any issues", command=issues)

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
    gui.bind('<Control-l>', clearAll)
    gui.bind('<Control-L>', clearAll)
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
    gui.bind('<Control-t>', qr)
    gui.bind('<Control-m>', month_calendar)
    gui.bind('<Control-y>', year_calendar)
    gui.bind('<Control-r>', clock)
    gui.bind('<Control-w>', timeDate)


    gui.mainloop()

if __name__ == '__main__':
    main()
