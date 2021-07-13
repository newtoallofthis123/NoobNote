from tkinter import *
import webbrowser

titlevar = "LiteNote"
iconvar = "icon.ico"

about = f'{titlevar} is a simple Notepad written purely in python with tkinter.\nIt is very feature rich though being light weight at the same time.\n{titlevar} is a beginner friendly project and is very easy to understand.\nIt is registered under the MIT License, Hence you are free to use it.\nTo learn more on how to contribute, see CONTRIBUTE.md and README.md\nTo learn to use {titlevar} functions, see MODULE.md or pypi.org/NoobNote\n'
author = f'I wrote NoobNote to learn tkinter(python gui module) and python.\nI also wanted to have a good alternative to Notepad, but not notepad++.\nHence NoobNote, it is as light weight, fast and as simple as Notepad,\nbut at the same time, a bit more feature rich, private and secure.\nNoobNote took a considerable amount of time and effort to make.\nso, if you want to contribute, be sure to check out CONTRIBUTE.md\n'
details = f'Author: NoobScience\nProjectName: NoobNote\nWebsite: tinu.be/NoobNote\nAuthor Website: tinu.be/About\nGithub: @newtoallofthis123'
about_gui = Tk()
about_gui.title(f'About {titlevar}')
about_gui.iconbitmap(f'{iconvar}')
about_gui.geometry("780x600")
title = Label(about_gui, font=("Cascadia Code", 18), fg="black", bg="#F0F0F0", text=titlevar)
title.pack()
subtitle = Label(about_gui, font=("Lucida Handwriting", 10), fg="black", bg="#F0F0F0", text="A Simple Light Weight NotePad\n")
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
about_root_2 = Frame(about_gui,)
about_root_2.pack()
about_author_website_btn = Button(about_root_2, text="Author Web", font=("Cascadia Code", 12),fg="black", bg="white", borderwidth=0, command=openNoobweb())
about_author_website_btn.grid(row=0, column=0)
about_NoobNote_website_btn = Button(about_root_2, text="NoobNote Web", font=("Cascadia Code", 12),fg="black", bg="white", borderwidth=0, command=openWeb())
about_NoobNote_website_btn.grid(row=0, column=1)
about_author_github_btn = Button(about_root_2, text="Author Github", font=("Cascadia Code", 12),fg="black", bg="white", borderwidth=0, command=projects())
about_author_github_btn.grid(row=0, column=2)
about_NoobNote_github_btn = Button(about_root_2, text="NoobNote Github", font=("Cascadia Code", 12),fg="black", bg="white", borderwidth=0, command=source())
about_NoobNote_github_btn.grid(row=0, column=3)
about_gui.mainloop()