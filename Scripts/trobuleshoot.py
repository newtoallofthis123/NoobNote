#! /usr/bin/env python3
print("NoobNote Trobuleshooting")
print("")
try:
    from tkinter.messagebox import showinfo
    from tkinter.messagebox import showerror
    from tkinter import *
    from tkinter import filedialog
    from tkinter import font
    from tkinter import colorchooser
    print("tkinter import was successfull")
except:
    print("No Module Named tkinter found. Check if python is installed correctly")

try:
    import webbrowser
    print("webbrowser import was successfull")
    print("")
except:
    print("No Module Named webbrowser found. Check if python is installed correctly")
    print("")
print("Try running NoobNote now.")    
print("If this doesn't solve your problem, look for any errors in the code. Report any bugs or issues at https://github.com/newtoallofthis123/NoobNote/issues")
print("")

print("By NoobScience")
