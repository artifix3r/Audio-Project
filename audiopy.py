import pygame
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os
import json 





class MP:
    def __init__(self, win):
        # Create Tkinter window
        win.geometry('300x600')
        win.title('Music Player')
        win.resizable(0, 0)
        self.timedict=dict()
        self.isbool=True
        self.comdict=dict()
        # StringVar to change button text later
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')
        self.str_time = tk.StringVar()
        self.txt_time = tk.Label(win, textvariable=self.str_time)
        self.txt_time.place(x=100, y=320)
        # The buttons and their positions
        load_button = Button(win, text='Load', width=10, font=('Arial', 20), command=self.load)
        load_button.place(x=100, y=40, anchor='center')
        
        play_button = Button(win, textvariable=self.play_restart, width=10, font=('Arial', 20), command=self.play)
        play_button.place(x=100, y=80, anchor='center')
        
        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=('Arial', 20), command=self.pause)
        pause_button.place(x=100, y=120, anchor='center')

        stop_button = Button(win, text='Stop', width=10, font=('Arial', 20), command=self.stop)
        stop_button.place(x=100, y=160, anchor='center')
        
        ##commenter = Button(win, text='Adding', width=10, font=('Arial', 20), command=self.commenter)
        ##commenter.place(x=100, y=400, anchor='center')
        Comment=Label(win,text="Comment",font=('Arial',10))
        Comment.pack( side = LEFT)
        Comment.place(x=50,y=200,anchor='center')
        self.lable=Label(win,text="Comment",font=('Arial',10))
        self.lable.pack( side = LEFT)
        self.lable.place(x=100,y=360,anchor='center')
        self.time=Label(win,text="Time",font=('Arial',10))
        self.time.pack(side=LEFT)
        self.time.place(x=200,y=360,anchor='center')
        self.E1 = Entry(win, bd = 5)
        self.E1.pack(side = RIGHT)  
        self.E1.place(x=100,y=200)
        self.E1.config(state="disabled")
        add_button = Button(win, text='Save Comment', width=12, font=('Arial', 9),command=self.print_comment)
        add_button.place(x=200, y=280, anchor='center')
        commenter = Button(win, text='Add Comment', width=12, font=('Arial', 9), command=self.commenter)
        commenter.place(x=70, y=280, anchor='center')
        self.comstate=False
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
        print("Loaded: ", self.music_file)
        self.play_restart.set('Play')
    def play(self):
        global is_playing, is_paused
        self.isbool=True
        is_playing,is_paused=True,False
        if self.music_file:
            with open('comments.json') as json_file:
                self.timedict = json.load(json_file)
            mixer.init()
            mixer.music.load(str(self.music_file))
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')
            a = mixer.Sound(str(self.music_file))
            print(a.get_length())
            length=int(a.get_length())
            while(mixer.music.get_busy() and not self.comstate):
                for key,value in self.timedict.items():
                    if (mixer.music.get_pos())==value:
                        self.lable.config(text=key)
                        self.time.config(text=value)
                        root.update()
                        print(value,key)
    
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()

            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')

    def stop(self):
        with open("comments.json", "w") as outfile:
            json.dump(self.timedict, outfile)
        self.isbool=False
        print(self.timedict.values())
        mixer.music.stop()
   
    def commenter(self):
        self.E1.config(state="normal")
        mixer.music.pause()
        self.comstate=True
        self.str_time.set("")
    def print_comment(self):
        print(mixer.music.get_pos())
        _comment=self.E1.get()
        self.str_time.set("Comment Added Successfully")
        self.timedict[_comment]=mixer.music.get_pos()
        mixer.music.unpause()
        self.E1.delete(0,END)
        self.E1.config(state="disabled")
        self.comstate=False
        while(mixer.music.get_busy() and not self.comstate):
                for key,value in self.timedict.items():
                    if (mixer.music.get_pos())==value:
                        self.lable.config(text=key)
                        self.time.config(text=value)
                        root.update()
                        print(value,key)

root = Tk()
MP(root)
root.mainloop()
