#Music Player in Python

from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer

#colours
colour1 = "#ffffff" #white
colour2 = "#3C1DC6" #purple
colour3 = "#333333" #black
colour4 = "#CFC7F8" #light purple

#window
window = Tk()
window.title("Music Player")
window.geometry("400x300")
window.configure(background=colour1)
window.resizable(width=FALSE, height=FALSE)

#events
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()  

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def next_music():
    playing =  running_song['text']
    index = songs.index(playing)
    new_index = index+1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0,END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

def previous_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index - 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0,END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

def stop_music():
    mixer.music.stop()

#frames
left_frame = Frame(window, width=200, height=200, bg=colour3)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width=200, height=200, bg=colour2)
right_frame.grid(row=0, column=1, padx=0, pady=0)

down_frame = Frame(window, width=400, height=100, bg=colour4)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=1)

#right frame
listbox = Listbox(right_frame, selectmode=SINGLE, font=('Arial 9 bold'), width=25, bg=colour4, fg=colour1)
listbox.grid(row=0,column=0)

w = Scrollbar(right_frame)
w.grid(row=0, column=1)

listbox.config(yscrollcommand = w.set)
w.config(command= listbox.yview)

#images
image_1 = Image.open('E:\Code Clause\Music Icons\Music icon.png')
image_1 = image_1.resize((200,200))
image_1 = ImageTk.PhotoImage(image_1)
app_image = Label(left_frame, height=200, image=image_1, padx=5, bg=colour1)
app_image.place(x=0,y=0)

image_2 = Image.open('E:\Code Clause\Music Icons\Previous.png')
image_2 = image_2.resize((50,50))
image_2 = ImageTk.PhotoImage(image_2)
pre_butt = Button(down_frame, width=40, height=60, image=image_2, padx=10, bg=colour4, font=('Ivy 10'), command=previous_music)
pre_butt.place(x=42+10,y=25)

image_3 = Image.open('E:\Code Clause\Music Icons\play.png')
image_3 = image_3.resize((50,50))
image_3 = ImageTk.PhotoImage(image_3)
ply_butt = Button(down_frame, width=50, height=60, image=image_3, padx=10, bg=colour4, font=('Ivy 10'), command=play_music)
ply_butt.place(x=65+40,y=25)

image_4 = Image.open('E:\Code Clause\Music Icons\pnext.png')
image_4 = image_4.resize((50,50))
image_4 = ImageTk.PhotoImage(image_4)
nxt_butt = Button(down_frame, width=40, height=60, image=image_4, padx=10, bg=colour4, font=('Ivy 10'), command=next_music)
nxt_butt.place(x=125+40,y=25)

image_5 = Image.open('E:\Code Clause\Music Icons\Pause.jpg')
image_5 = image_5.resize((50,50))
image_5 = ImageTk.PhotoImage(image_5)
pause_butt = Button(down_frame, width=40, height=60, image=image_5, padx=10, bg=colour4, font=('Ivy 10'), command=pause_music)
pause_butt.place(x=175+40,y=25)

image_6 = Image.open('E:\Code Clause\Music Icons\Stop.png')
image_6 = image_6.resize((50,50))
image_6 = ImageTk.PhotoImage(image_6)
stop_butt = Button(down_frame, width=50, height=60, image=image_6, padx=10, bg=colour4, font=('Ivy 10'), command=stop_music)
stop_butt.place(x=275+40,y=25)

image_7 = Image.open('E:\Code Clause\Music Icons\continue.png')
image_7 = image_7.resize((50,50))
image_7 = ImageTk.PhotoImage(image_7)
con_butt = Button(down_frame, width=40, height=60, image=image_7, padx=10, bg=colour4, font=('Ivy 10'), command=continue_music)
con_butt.place(x=225+40,y=25)

line = Label(left_frame, width=200, height=1, padx=10, bg=colour3)
line.place(x=0,y=1)

line = Label(left_frame, width=200, height=1, padx=10, bg=colour1)
line.place(x=0,y=3)

running_song = Label(down_frame, text='Choose a Song:', font=('Ivy 10'), width=50, height=1, padx=10, bg=colour3, fg=colour1, anchor=NW)
running_song.place(x=0,y=0)


os.chdir(r'E:\Code Clause\songs')
songs = os.listdir()

def show():
    for i in songs:
        listbox.insert(END, i)

show()

mixer.init()
music_state = StringVar()
music_state.set('Choose one!')

window.mainloop()

