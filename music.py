from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo
import pygame

music = Tk()
music.title("Music Player")
music.iconbitmap("icon.ico")
music.geometry("400x280")

pygame.mixer.init()

def add():
    songs = filedialog.askopenfilenames(initialdir='D:\Songs', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    
    for song in songs:
        songBox.insert(END, song)

def play():
    song = songBox.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    songBox.selection_clear(ACTIVE)

songBox = Listbox(music, font=("Cascadia", 12), width=60)
songBox.pack()

add_btn = Button(music, text="Add Songs", borderwidth=0, font=("Cascadia", 12), command=add)
add_btn.pack()
play_btn = Button(music, text="Play", borderwidth=0, font=("Cascadia", 12), command=play)
play_btn.pack()
stop_btn = Button(music, text="Stop", borderwidth=0, font=("Cascadia", 12), command=stop)
stop_btn.pack()

music.mainloop()