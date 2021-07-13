from tkinter import *
import configparser

def main():
    config = configparser.ConfigParser()        
    config.read("settings.ini")
    Font = config['Font']
    Colors = config['Colors']
    fontvar = Font["fontvar"]
    sizevar = Font["sizevar"]
    bgvar = Colors["bgvar"]
    fgvar = Colors["fgvar"]
    selectbgvar = Colors["selectbgvar"]
    selectfgvar = Colors["selectfgvar"]
    toolbar_color = Colors["toolbar_color"]
    def save_settings(e):
        settings_file = 'settings.ini'
        file = open(settings_file, 'w')
        content = f'[Font]\nfontvar = {font_entry.get()}\nsizevar = {size_entry.get()}\n\n[Colors]\nbgvar = {bg_entry.get()}\nfgvar = {fg_entry.get()}\nselectbgvar = {select_bg_entry.get()}\nselectfgvar = {select_fg_entry.get()}\ntoolbar_color = {toolbar_entry.get()}\n\n[Profile]\nauthorvar = NoobScience\nprojectvar = NoobNote\nlinkvar = https://newtoallofthis123.github.io/About'
        file.write(content)
        file.close()

    set_gui = Tk()
    set_gui.title("Settings - LiteNote")
    set_gui.iconbitmap("icon.ico")
    set_gui.geometry("500x240")
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
    toolbar_label = Label(set_root, font=("Cascadia Code", 12), fg="black", bg="#F0F0F0", text="Toolbar Color")
    toolbar_label.grid(row=6, column=0)
    toolbar_entry = Entry(set_root, font=("Cascadia Code", 12), fg="black", bg="white", borderwidth=0)
    toolbar_entry.grid(row=6, column=1, padx=10, pady=1)
    toolbar_entry.insert(0, toolbar_color)
    save = Button(set_gui, font=("Cascadia Code", 12), fg="black", bg="white", text="Save", borderwidth=0, command=lambda: save_settings(False))
    save.pack()
    set_gui.mainloop()

if __name__ == '__main__':
    main()