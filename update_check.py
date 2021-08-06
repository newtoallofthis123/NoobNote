from tkinter import *
import webbrowser
import os
import requests
from tkinter.messagebox import askquestion, showinfo

def check_updates():
	def content_get():
		latest_release_page = requests.get("https://raw.githubusercontent.com/newtoallofthis123/NoobNote/main/latest_release.txt")
		latest_release_page_raw = str(latest_release_page.content)
		latest_release_page_pre = latest_release_page_raw.replace("b'", "")
		final_content = latest_release_page_pre.replace("'", "")
		return final_content
	def download_update():
		webbrowser_choice = askquestion("NoobNote Update Checker", "Do you want to open NoobNote releases page to download the new update now?")
		if webbrowser_choice == "yes":
			webbrowser.open("https://github.com/newtoallofthis123/NoobNote/releases")
		else:
			showinfo("NoobNote Update Checker", "Okay, some other time, you are still fine with this update, no major security fixes. Hope you enjoy NoobNote")
	update_gui = Tk()
	update_gui.title("NoobNote Update Checker")
	update_gui.geometry("500x150")
	update_gui.resizable(False, False)
	update_gui.iconbitmap("icon.ico")
	title_label = Label(update_gui, fg="black", bg="#F0F0F0", font=("Cascadia Code", 12), text=content_get())
	title_label.pack()
	check_below_label = Label(update_gui, fg="black", bg="#F0F0F0", font=("Cascadia Code", 12), text="Click below to download it")
	check_below_label.pack(padx=10, pady=20)
	download_btn = Button(update_gui, fg="#E7DB74", bg="#282923", font=("Cascadia Code", 12), text="🔽Download Now", borderwidth=1.2, command=download_update)
	download_btn.pack()
	update_gui.mainloop()