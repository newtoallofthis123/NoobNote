# Author : NoobScience
# License : MIT
# Name : tiny.py
# Usage: Free Usage with link to NoobScience
from tkinter import *
from tkinter.messagebox import showinfo
import pyperclip
import requests
def shortener():
    shorten_gui = Tk()
    shorten_gui.title("NoobNote-Url Shortener")
    shorten_gui.iconbitmap("icon.ico")
    shorten_gui.geometry("368x148")
    shorten_gui.config(bg="#282923")
    shorten_gui.resizable(False, False)
    def shorten():
        url_to = url_entry.get()
        url = f'https://tinyurl.com/api-create.php?url={url_to}'
        page = requests.get(url)
        final_url_raw = str(page.content)
        final_url_pre = final_url_raw.replace("b'", "")
        final_url = final_url_pre.replace("'", "")
        final_url_entry.config(text=final_url)
        pyperclip.copy(final_url)
        showinfo("NoobNote-Url Shortener", "Url Copied to clipboard")
    shorten_title = Label(shorten_gui, fg="#F8E1AB", bg="#282923", font=("Cascadia Code", 18), text="Url Shortener")
    shorten_title.pack()
    shorten_root = Frame(shorten_gui, bg="#282923")
    shorten_root.pack()
    url_entry_title = Label(shorten_root, fg="#F8E1AB", bg="#282923", font=("Cascadia Code", 12), text="Url: ")
    url_entry_title.grid(row=0, column=0)
    url_entry = Entry(shorten_root, fg="#67D8C3", bg="#1B1B1B", font=("Cascadia Code", 12), borderwidth=0, insertbackground="#67D8C3")
    url_entry.grid(row=0, column=1)
    final_url_entry_title = Label(shorten_root, fg="#F8E1AB", bg="#282923", font=("Cascadia Code", 12), text="Short: ")
    final_url_entry_title.grid(row=1, column=0)
    final_url_entry = Label(shorten_root, fg="#67D8C3", bg="#282923", font=("Cascadia Code", 12), borderwidth=0)
    final_url_entry.grid(row=1, column=1)
    shorten_btn = Button(shorten_gui, fg="#67D8C3", bg="#282923", font=("Cascadia Code", 12), borderwidth=0, command=shorten, text="Shorten")
    shorten_btn.pack()
    powered_by = Label(shorten_gui, fg="#E23636", bg="#282923", font=("Cascadia Code", 12), text="powered by tinyurl.com")
    powered_by.pack()
    shorten_gui.mainloop()