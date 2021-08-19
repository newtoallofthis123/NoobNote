# Application Name: CompactNote
# Version: v.0.1
# Author: NoobScience
# Author Website: https://newtoallofthis123.github.io/About
# Github: https://github.com/newtoallofthis123

# Defining path for linux
#! /usr/bin/env python3

from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo
import webbrowser
try:
    import os, sys
    import win32print
    import win32api
    import subprocess
except:
    pass

def main():
	current_dir = os.getcwd()
	gui = Tk()
	gui.title("CompactNote")
	gui.geometry("720x490")
	global fsVar
	fsVar = False
	gui.attributes('-fullscreen',fsVar)

	global openFilename
	openFilename = False

	global selectedText
	selectedText = False

	global wrapVar
	wrapVar = False

	global fontvar
	global sizevar
	iconvar = "icon.ico"
	fontvar = "Arial"
	sizevar = "14"
	bgvar = "white"
	fgvar = "black"
	selectbgvar = "#FFBE00"
	selectfgvar = "black"
	try:
		gui.iconbitmap(iconvar)
	except:
		pass

	def new_file(e):
		text.delete("1.0", END)
		gui.title("Untitled-CompactNote")
	def open_file(e):
		try:
		    text.delete("1.0", END)
		    file = filedialog.askopenfilename(initialdir=current_dir, title="Choose A File", filetypes=(("All Files", "*.*"),("Text Files", "*.txt")))
		    if file:
		        global openFilename
		        openFilename = file
		    name = file
		    gui.title(f'{name}-Notepad')

		    file = open(file, 'r')
		    content = file.read()
		    text.insert(END, content)
		    file.close()
		except:
		    showerror("Not opened", "No file name given")
	def saveas_file(e):
	    try:
	        file = filedialog.asksaveasfilename(defaultextension=".*", initialdir=current_dir, title="Save file as", filetypes=(("All Files", "*.*"),("Text Files", "*.txt")))
	        if file:
	            name = file
	            gui.title(f'{name}-CompactNote')

	            file = open(file, 'w')
	            file.write(text.get(1.0, END))
	            file.close()
	    except:
	        showerror("Not Saved", "No file name given")
	def save_file(e):
	    try:
	        global openFilename
	        if openFilename:
	            file = openFilename
	            file = open(file, 'w')
	            file.write(text.get(1.0, END))
	            file.close()
	        else:
	            saveas_file(e)
	    except:
	        showerror("Not Saved", "No file saved")
	def save_exit(e):
	    saveFile(False)
	    gui.quit()
	def new_window(e):
		main()
	def cut_text(e):
	    global selectedText
	    if e:
	        selectedText = gui.clipboard_get()
	    else:
	        if text.selection_get():
	            selectedText = text.selection_get()
	            text.delete("sel.first", "sel.last")
	            gui.clipboard_clear()
	            gui.clipboard_append(selectedText)
	def copy_text(e):
	    global selectedText
	    if e:
	        selectedText = gui.clipboard_get()
	    if text.selection_get():
	        selectedText = text.selection_get()
	        gui.clipboard_clear()
	        gui.clipboard_append(selectedText)
	def paste_text(e):
	    global selectedText
	    if e:
	        selectedText = gui.clipboard_get()
	    else:
	        if selectedText:
	            positionCursor = text.index(INSERT)
	            text.insert(positionCursor, selectedText)
	def time_date(e):
	    from datetime import datetime
	    from datetime import date
	    current_t = datetime.now()
	    current_date = str(date.today())
	    current_t_f = current_t.strftime("%H:%M:%S")
	    timeAnddate = (f'{current_t_f} {current_date}')
	    text.insert(END, timeAnddate)
	def select_all(e):
		text.tag_add('sel', '1.0', 'end')
	def del_text(e):
		try:
		    text.delete(SEL_FIRST, SEL_LAST)
		except:
		    showerror("Error", "No Text Selected to Search")
	def right_click_menu(e):
		rightClickmenu.tk_popup(e.x_root, e.y_root)
	def word_wrap(e):
	    global wrapVar
	    if wrapVar:
	        text.config(wrap=WORD)
	        wrapVar = False
	    else:
	        wrapVar = True
	        text.config(wrap="none")
	def full_screen(e):
	    global fsVar
	    if fsVar:
	        gui.attributes('-fullscreen',False)
	        fsVar = False
	    else:
	        fsVar = True
	        gui.attributes('-fullscreen',True)
	def zoom_in(e):
	    global sizevar
	    sizevar = int(sizevar) + 1
	    text.config(font=(fontvar, sizevar))
	def zoom_out(e):
	    global sizevar
	    sizevar = int(sizevar) - 1
	    text.config(font=(fontvar, sizevar))
	def default_zoom(e):
		text.config(font=(fontvar, 13))
	def font_settings(e):
		global fontvar
		fontvar = e
		text.config(font=(fontvar, sizevar))
	def search_google(e):
	    try:
	        content = text.selection_get()
	        url = 'https://www.google.com/search?hl=en&q=' + content
	        webbrowser.open(url)
	    except:
	        showerror("Error", "No Text Selected to Search")
	def search_duckduckgo(e):
	    try:
	        content = text.selection_get()
	        url = 'https://duckduckgo.com/search?q=' + content
	        webbrowser.open(url)
	    except:
	        showerror("Error", "No Text Selected to Search")
	def print_file(e):
		try:
			printerName = win32print.GetDefaultPrinter()
			printAsk = f'Do you want to print with your deflaut printer: {printerName} ? You can change your default printer in your system preferences'
			printChoice = askquestion("Print File?", printAsk)
			if printChoice == 'yes':
				try:
					global openFilename
					fileToprint = openFilename
				except:
					fileToprint = filedialog.askopenfilename(initialdir=current_dir, title="Select File to Print", filetypes=(("All Files", "*.*"),("Text Files", "*.txt")))
				if fileToprint:
					win32api.ShellExecute(0, "print", fileToprint, None, ".", 0)
			elif printChoice == 'no':
			    showerror("Printing Aborted", "Printing Aborted")
			else:
			    showerror("Error", "Something went wrong. Printing Aborted")
		except:
		    showerror("Unable to Print", "Something went wrong.Printer is most likely offline. Try again when the printer is online or report this issue to https://github.com/newtoallofthis123/NoobNote/issues")
	def quit1(e):
		gui.quit()
	def about_(e):
	    about = f'CompactNote is an almost exact copy of Notepad.\nNotepadd is a beginner friendly project and is very easy to understand.\nIt is registered under the MIT License, Hence you are free to use it.\nTo learn more on how to contribute, see CONTRIBUTE.md and README.md'
	    author = f'I wrote NoobNote to learn tkinter(python gui module) and python.\nI also wanted to have a good alternative to Notepad, but not notepad++.\nHence NoobNote, it is as light weight, fast and as simple as Notepad,\nbut at the same time, a bit more feature rich, private and secure.\nNoobNote took a considerable amount of time and effort to make.\nso, if you want to contribute, be sure to check out CONTRIBUTE.md\n'
	    details = f'Author: NoobScience\nProjectName: CompactNote\nAuthor Website: kutt.it/author_web\nGithub: @newtoallofthis123\n'
	    about_gui = Tk()
	    about_gui.title(f'About Notepadd')
	    about_gui.iconbitmap(f'{iconvar}')
	    about_gui.geometry("780x510")
	    about_gui.resizable(False, False)
	    def quit_3(e):
	    	about_gui.destroy()
	    def open_author_web():
	    	webbrowser.open("https://newtoallofthis123.github.io/About")
	    def projects_web():
	    	webbrowser.open("https://github.com/newtoallofthis123")
	    title = Label(about_gui, font=("Cascadia Code", 18), fg="black", bg="#F0F0F0", text="CompatNote")
	    title.pack()
	    subtitle = Label(about_gui, font=("Lucida Handwriting", 10), fg="black", bg="#F0F0F0", text="A Simple Compact Version of NoobNote, by NoobScience\n")
	    subtitle.pack()
	    about_root = Frame(about_gui,)
	    about_root.pack()
	    about_title = Label(about_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text="About: ")
	    about_title.grid(row=0, column=0)
	    about_title_content = Label(about_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text=about)
	    about_title_content.grid(row=0, column=1)
	    about_title = Label(about_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text="About Author: ")
	    about_title.grid(row=1, column=0)
	    about_title_content = Label(about_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text=author)
	    about_title_content.grid(row=1, column=1)
	    about_details = Label(about_gui, font=("Cascadia Code", 14), fg="black", bg="#F0F0F0", text="Details")
	    about_details.pack()
	    about_details_content = Label(about_gui, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text=details)
	    about_details_content.pack()
	    about_root_2 = Frame(about_gui, bg="red")
	    about_root_2.pack()
	    about_author_website_btn = Button(about_root_2, text="Website", font=("Cascadia Code", 12),fg="black", bg="#9CACCC", borderwidth=0, command=open_author_web)
	    about_author_website_btn.grid(row=0, column=0)
	    about_author_space_btn = Button(about_root_2, text="   ", font=("Cascadia Code", 12),fg="black", bg="#F0F0F0", borderwidth=0, command=projects_web)
	    about_author_space_btn.grid(row=0, column=1)
	    about_author_github_btn = Button(about_root_2, text="Github", font=("Cascadia Code", 12),fg="black", bg="#9CACCC", borderwidth=0, command=projects_web)
	    about_author_github_btn.grid(row=0, column=2)
	    about_gui.bind('<Return>', quit_3)
	def open_author_web():
		webbrowser.open("https://newtoallofthis123.github.io/About")
	def projects_web():
		webbrowser.open("https://github.com/newtoallofthis123")
	def options(e):
	    def save_settings(e):
	        settings_file = 'settings.ini'
	        file = open(settings_file, 'w')
	        if font_entry.get() == "":
	            font_entry_ = "Cascadia Code"
	        else:
	            font_entry_ = font_entry.get()
	        if size_entry.get() == "":
	            size_entry_ = "14"
	        else:
	            size_entry_ = size_entry.get()
	        if bg_entry.get() == "":
	            bg_entry_ = "white"
	        else:
	            bg_entry_ = bg_entry.get()
	        if fg_entry.get() == "":
	            fg_entry_ = "black"
	        else:
	            fg_entry_  = fg_entry.get()
	        if select_bg_entry.get() == "":
	            select_bg_entry_ = "#F9C500"
	        else:
	            select_bg_entry_ = select_bg_entry.get()
	        if select_fg_entry.get() == "":
	            select_fg_entry_ = "black"
	        else:
	            select_fg_entry_ = select_fg_entry.get()
	        if icon_entry.get() == "":
	            icon_entry_ = "icon.ico"
	        else:
	            icon_entry_ = icon_entry.get()
	        content = f'[Font]\nfontvar = {font_entry_}\nsizevar = {size_entry_}\n\n[Colors]\nbgvar = {bg_entry_}\nfgvar = {fg_entry_}\nselectbgvar = {select_bg_entry_}\nselectfgvar = {select_fg_entry_}\n\n[NoobNote]\nicon = {icon_entry_}\n\n[Profile]\nauthorvar = NoobScience\nprojectvar = NoobNote\nlinkvar = https://newtoallofthis123.github.io/About'
	        file.write(content)
	        file.close()
	        try:
	            set_gui.destroy()
	        except:
	            pass
	        try:
	            runner_gui.destroy()
	        except:
	            pass
	        try:
	            find_gui.destroy()
	        except:
	            pass
	        try:
	            music_gui.destroy()
	        except:
	            pass
	        try:
	            gui.destroy()
	        except:
	            pass
	    set_gui = Tk()
	    set_gui.title("Settings - LiteNote")
	    set_gui.iconbitmap("icon.ico")
	    set_gui.geometry("450x230")
	    set_gui.resizable(False, False)
	    set_root = Frame(set_gui,)
	    set_root.pack()
	    font_label = Label(set_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text="Font")
	    font_label.grid(row=0, column=0)
	    font_entry = Entry(set_root, font=("Cascadia Code", 12), fg="black", bg="white", borderwidth=0)
	    font_entry.grid(row=0, column=1, padx=10, pady=1)
	    font_entry.insert(0, fontvar)
	    size_label = Label(set_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text="Size")
	    size_label.grid(row=1, column=0)
	    size_entry = Entry(set_root, font=("Cascadia Code", 12), fg="black", bg="white", borderwidth=0)
	    size_entry.grid(row=1, column=1, padx=10, pady=1)
	    size_entry.insert(0, sizevar)
	    fg_label = Label(set_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text="Font Color")
	    fg_label.grid(row=2, column=0)
	    fg_entry = Entry(set_root, font=("Cascadia Code", 12), fg="black", bg="white", borderwidth=0)
	    fg_entry.grid(row=2, column=1, padx=10, pady=1)
	    fg_entry.insert(0, fgvar)
	    bg_label = Label(set_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text="Background Color")
	    bg_label.grid(row=3, column=0)
	    bg_entry = Entry(set_root, font=("Cascadia Code", 12), fg="black", bg="white", borderwidth=0)
	    bg_entry.grid(row=3, column=1, padx=10, pady=1)
	    bg_entry.insert(0, bgvar)
	    select_fg_label = Label(set_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text="Selection Font Color")
	    select_fg_label.grid(row=4, column=0)
	    select_fg_entry = Entry(set_root, font=("Cascadia Code", 12), fg="black", bg="white", borderwidth=0)
	    select_fg_entry.grid(row=4, column=1, padx=10, pady=1)
	    select_fg_entry.insert(0, selectfgvar)
	    select_bg_label = Label(set_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text="Selection Background Color")
	    select_bg_label.grid(row=5, column=0)
	    select_bg_entry = Entry(set_root, font=("Cascadia Code", 12), fg="black", bg="white", borderwidth=0)
	    select_bg_entry.grid(row=5, column=1, padx=10, pady=1)
	    select_bg_entry.insert(0, selectbgvar)
	    icon_label = Label(set_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text="Icon Path")
	    icon_label.grid(row=7, column=0)
	    icon_entry = Entry(set_root, font=("Cascadia Code", 12), fg="black", bg="white", borderwidth=0)
	    icon_entry.grid(row=7, column=1, padx=10, pady=1)
	    icon_entry.insert(0, iconvar)
	    save = Button(set_gui, font=("Cascadia Code", 12), fg="black", bg="white", text="Save", borderwidth=0, command=lambda: save_settings(False))
	    save.pack()
	    set_gui.bind('<Return>', save_settings)
	    set_gui.mainloop()

	scroll_text = Scrollbar(gui,)
	scroll_text.pack(side=RIGHT, fill=Y)

	horizontal_scroll = Scrollbar(gui,orient='horizontal')
	horizontal_scroll.pack(side=BOTTOM, fill=X, ipadx=10)

	textWidth = gui.winfo_screenwidth()
	textHeight = int(gui.winfo_screenheight())

	text = Text(gui, width=textWidth, height=textHeight, font=(fontvar, sizevar), borderwidth=0,selectbackground=selectbgvar, selectforeground=selectfgvar, undo=True, yscrollcommand=scroll_text.set, xscrollcommand=horizontal_scroll.set, fg=fgvar, bg=bgvar,)
	text.pack()

	menu = Menu(gui,)
	gui.config(menu=menu,)

	fileMenu = Menu(menu, tearoff=False,)
	menu.add_cascade(label="File", menu=fileMenu)
	fileMenu.add_command(label="New", command=lambda: new_file(False), accelerator="Ctrl+N")
	fileMenu.add_command(label="New Window", command=lambda: new_window(False), accelerator="Ctrl+Shift+N")
	fileMenu.add_command(label="Open...", command=lambda: open_file(False), accelerator="Ctrl+O")
	fileMenu.add_command(label="Save", command=lambda: save_file(False), accelerator="Ctrl+S")
	fileMenu.add_command(label="Save As...", command=lambda: saveas_file(False), accelerator="Ctrl+Shift+S")
	fileMenu.add_separator()
	fileMenu.add_command(label="Print...", command=lambda: print_file(False), accelerator="Ctrl+P")
	fileMenu.add_separator()
	fileMenu.add_command(label="Exit", command=lambda: quit1(False))

	editMenu = Menu(menu, tearoff=False)
	menu.add_cascade(label="Edit", menu=editMenu)
	editMenu.add_command(label="Undo", command=text.edit_undo, accelerator="Ctrl+Z")
	editMenu.add_separator()
	editMenu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="Ctrl+X")
	editMenu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="Ctrl+C")
	editMenu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="Ctrl+V")
	editMenu.add_command(label="Delete", command=lambda: del_text(False), accelerator="Del")
	editMenu.add_separator()
	editMenu.add_command(label="Search with Google", command=lambda: search_google(False), accelerator="Crtl+G")
	editMenu.add_command(label="Search with DuckDuckGo", command=lambda: search_duckduckgo(False), accelerator="Crtl+D")
	editMenu.add_separator()
	editMenu.add_command(label="Select All", command=lambda: select_all(False), accelerator="Ctrl+A")
	editMenu.add_command(label="Time/Date", command=lambda: time_date(False), accelerator="F5")

	rightClickmenu = Menu(gui, tearoff=False)
	rightClickmenu.add_command(label="Undo", command=text.edit_undo)
	rightClickmenu.add_separator()
	rightClickmenu.add_command(label="Cut", command=lambda: cut_text(False))
	rightClickmenu.add_command(label="Copy", command=lambda: copy_text(False))
	rightClickmenu.add_command(label="Paste", command=lambda: paste_text(False))
	rightClickmenu.add_command(label="Delete", command=lambda: del_text(False))
	rightClickmenu.add_separator()
	rightClickmenu.add_command(label="Select All", command=lambda: select_all(False))
	rightClickmenu.add_separator()
	rightClickmenu.add_command(label="Search with Google", command=lambda: search_google(False))
	rightClickmenu.add_command(label="Search with DuckDuckGo", command=lambda: search_duckduckgo(False))
	rightClickmenu.add_separator()
	rightClickmenu.add_command(label="Options", command=lambda: options(False))

	formatMenu = Menu(menu, tearoff=False)
	menu.add_cascade(label="Format", menu=formatMenu)
	formatMenu.add_checkbutton(label="Word Wrap", command=lambda: word_wrap(False),)
	fontMenu = Menu(menu, tearoff=False)
	formatMenu.add_cascade(label="Font", menu=fontMenu)
	fontMenu.add_command(label="Arial", command=lambda: font_settings("Arial"))
	fontMenu.add_command(label="Calibri", command=lambda: font_settings("Calibri"))
	fontMenu.add_command(label="Cascadia Code", command=lambda: font_settings("Cascadia Code"))
	fontMenu.add_command(label="Comic Sans MS", command=lambda: font_settings("Comic Sans MS"))
	fontMenu.add_command(label="Consolas", command=lambda: font_settings("Consolas"))
	fontMenu.add_command(label="Jetbrains Mono", command=lambda: font_settings("Jetbrains Mono"))
	fontMenu.add_command(label="Lucida Calligraphy", command=lambda: font_settings("Lucida Calligraphy"))
	fontMenu.add_command(label="Lucida Console", command=lambda: font_settings("Lucida Console"))
	fontMenu.add_command(label="Lucida Handwriting", command=lambda: font_settings("Lucida Handwriting"))
	fontMenu.add_command(label="Microsoft Sans Serif", command=lambda: font_settings("Microsoft Sans Serif"))
	fontMenu.add_command(label="Times New Roman", command=lambda: font_settings("Times New Roman"))

	viewMenu = Menu(menu, tearoff=False)
	menu.add_cascade(label="View", menu=viewMenu)
	zoomMenu = Menu(menu, tearoff=False)
	viewMenu.add_cascade(label="Zoom", menu=zoomMenu)
	zoomMenu.add_command(label="Zoom In", command=lambda: zoom_in(False), accelerator="Ctrl+Plus")
	zoomMenu.add_command(label="Zoom Out", command=lambda: zoom_out(False), accelerator="Ctrl+Minus")
	zoomMenu.add_command(label="Restore Default Zoom", command=lambda: default_zoom(False), accelerator="Ctrl+0")
	viewMenu.add_checkbutton(label="FullScreen", command=lambda: full_screen(False), accelerator="F11")
	viewMenu.add_separator()
	viewMenu.add_command(label="Options", command=lambda: options(False), accelerator="Ctrl+Shift+P")

	helpMenu = Menu(menu, tearoff=False)
	menu.add_cascade(label="Help", menu=helpMenu)
	helpMenu.add_command(label="Author Website", command=open_author_web)
	helpMenu.add_command(label="Author Github", command=projects_web)
	helpMenu.add_separator()
	helpMenu.add_command(label="About", command=lambda: about_(False), accelerator="Ctrl+H")

	gui.bind('<Control-Key-x>', cut_text)
	gui.bind('<Control-Key-c>', copy_text)
	gui.bind('<Control-Key-p>', paste_text)
	gui.bind('<Button-3>', right_click_menu)
	gui.bind('<Control-Key-s>', save_file)
	gui.bind('<Control-Key-o>', open_file)
	gui.bind('<Control-Key-n>', new_file)
	gui.bind('<Control-Key-S>', saveas_file)
	gui.bind('<Control-Key-p>', print_file)
	gui.bind('<Control-Key-N>', new_window)
	gui.bind('<Control-Key-d>', search_duckduckgo)
	gui.bind('<Control-Key-g>', search_google)
	gui.bind('<Control-Key-a>', select_all)
	gui.bind('<F5>', time_date)
	gui.bind('<Delete>', del_text)
	gui.bind('<Control-Key-minus>', zoom_out)
	gui.bind('<Control-Key-plus>', zoom_in)
	gui.bind('<F11>', full_screen)
	gui.bind('<Control-Key-0>', default_zoom)
	gui.bind('<Control-Key-q>', quit1)
	gui.bind('<Control-Key-h>', about_)
	gui.bind('<Control-Key-P>', options)

	gui.mainloop()

if __name__ == '__main__':
	main()
