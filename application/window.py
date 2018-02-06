#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
from application.board import *
from tkinter import tix
import tkinter as tk

class SeaofBTCapp(tix.Tk):

    def __init__(self, *args, **kwargs):
        tix.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Window, TemperatureFrame):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Window)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.window["bg"]="white"

        self.board = Board()
        # manage menu
        menubar = Menu(self.window)
        filemenu = Menu(menubar, tearoff=0)
        setting = Menu(menubar, tearoff=0)
        filemenu.add_command(label="import config", command = self.file)
        filemenu.add_command(label="export settings", command = self.file)
        filemenu.add_command(label="import", command = self.file)

        setting.add_command(label="com config", command=self.file)
        setting.add_command(label="logs", command=self.file)

        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Settings", menu=setting)
        self.window["menu"] = menubar

        self.canvas = [0]*10
        self.canvas[1] = Canvas(self.window,bg="white", height=200, width=200, bd=2,highlightthickness=0, relief='ridge')
        photo = PhotoImage(file="thermometer.png")
        self.canvas[1].create_image(100,100, image = photo)
        self.canvas[1].create_text(100,180, text="temperature")

        self.canvas[1].grid(row=0,column=0)

        photo1 = PhotoImage(file="spirit_level.png")
        self.canvas[2] = Canvas(self.window, bg="white", height=200, width=200, bd=2,highlightthickness=0, relief='ridge')
        self.canvas[2].create_image(100,100, image = photo1)
        self.canvas[2].create_text(100,180, text="accelerometer")
        self.canvas[2].grid(row=0, column=1)

        photo2 = PhotoImage(file="led-light.png")
        self.canvas[3] = Canvas(self.window, bg="white", height=200, width=200, bd=2,highlightthickness=0, relief='ridge')
        self.canvas[3].create_image(100,100, image = photo2)
        self.canvas[3].create_text(100,180, text="leds")

        self.canvas[3].grid(row=0, column=2)

        photo3 = PhotoImage(file="switch.png")
        self.canvas[4] = Canvas(self.window, bg="white", height=200, width=200, bd=2,highlightthickness=0, relief='ridge')
        self.canvas[4].create_image(100,100, image = photo3)
        self.canvas[4].create_text(100,180, text="buttons")
        self.canvas[4].grid(row=0, column=3)

        photo4 = PhotoImage(file="photo-camera.png")
        self.canvas[5] = Canvas(self.window, bg="white", height=200, width=200, bd=2,highlightthickness=0, relief='ridge')
        self.canvas[5].create_image(100,100, image = photo4    )
        self.canvas[5].create_text(100,180, text="cam")

        self.canvas[5].grid(row=2, column=0)

        photo5 = PhotoImage(file="microphone.png")
        self.canvas[6] = Canvas(self.window, bg="white", height=200, width=200, bd=2,highlightthickness=0, relief='ridge')
        self.canvas[6].create_image(100,100, image = photo5    )
        self.canvas[6].create_text(100,180, text="sound")
        self.canvas[6].grid(row=2, column=1)

        photo7 = PhotoImage(file="laser-pointer.png")
        self.canvas[7] = Canvas(self.window, bg="white", height=200, width=200, bd=2,highlightthickness=0, relief='ridge')
        self.canvas[7].create_image(100,100, image = photo7    )
        self.canvas[7].create_text(100,180, text="laser")
        self.canvas[7].grid(row=2, column=2)

        photo6 = PhotoImage(file="plus.png")
        self.canvas[8] = Canvas(self.window, bg="white", height=200, width=200, bd=2,highlightthickness=0, relief='ridge')
        self.canvas[8].create_image(100,100, image = photo6    )
        self.canvas[8].create_text(100,180, text="add elements")
        self.canvas[8].grid(row=2, column=3)

        ttk.Separator(self.window, orient=HORIZONTAL).grid(row=3, columnspan=5, sticky="ew")

        L1 = Label(self.window, text="enter serial Port : ", bg="white")

        L1.grid(row=4,column=0)

        self.c = ttk.Combobox(self.window, values=self.board.find_serials(), width=10)
        self.c.grid(row=4, column=1)
        self.c.bind("<Button-1>", self.menu_serial)




        button = Button(self.window,text="pair", command=self.pair, bg="red")
        button.grid(row=4, column =2)

        L1 = Label(self.window, text="enter socket address::port : ", bg="white")
        L1.grid(row=5, column=0)

        self.E1 = Entry(self.window, bd=5, bg="white")
        self.E1.grid(row=5, column=1)

        self.button = Button(self.window, text="pair", command=self.pair, bg="red")
        self.button.grid(row=5, column=2)
       # window.bind("<Key>", key)


        self.num = 1
        self.canvas[1].bind('<Enter>', lambda event, arg=1: self.enter(event, arg))
        self.canvas[1].bind('<Leave>', lambda event, arg=1: self.leave(event, arg))
        self.canvas[1].bind('<Button-1>',   command = lambda: controller.show_frame(TemperatureFrame))
        self.num = 2
        self.canvas[2].bind('<Enter>', lambda event, arg=2: self.enter(event, arg))
        self.canvas[2].bind('<Leave>', lambda event, arg=2: self.leave(event, arg))

        self.num = 3
        self.canvas[3].bind('<Enter>', lambda event, arg=3: self.enter(event, arg))
        self.canvas[3].bind('<Leave>', lambda event, arg=3: self.leave(event, arg))

        self.num = 4
        self.canvas[4].bind('<Enter>', lambda event, arg=4: self.enter(event, arg))
        self.canvas[4].bind('<Leave>', lambda event, arg=4: self.leave(event, arg))

        self.num = 5
        self.canvas[5].bind('<Enter>', lambda event, arg=5: self.enter(event, arg))
        self.canvas[5].bind('<Leave>', lambda event, arg=5: self.leave(event, arg))

        self.num = 6
        self.canvas[6].bind('<Enter>', lambda event, arg=6: self.enter(event, arg))
        self.canvas[6].bind('<Leave>', lambda event, arg=6: self.leave(event, arg))

        self.num = 7
        self.canvas[7].bind('<Enter>', lambda event, arg=7: self.enter(event, arg))
        self.canvas[7].bind('<Leave>', lambda event, arg=7: self.leave(event, arg))

        self.num = 7
        self.canvas[8].bind('<Enter>', lambda event, arg=8: self.enter(event, arg))
        self.canvas[8].bind('<Leave>', lambda event, arg=8: self.leave(event, arg))

        self.photo8 = PhotoImage(file="ok.png")
        self.canvas[9] = Canvas(self.window, bg="white", height=30, width=30, bd=2, highlightthickness=0,
                                relief='ridge')

    def file(self):
        print("file")

    def pair(self):
        portname = self.E1.get()
        portname = portname.split(":")
        self.board.connect_to_wifi(str(portname[0]), int(portname[1]))
        print("connect to "+ portname[0]+portname[1])
        if(self.board.wifi_connected):
            self.button["bg"]="green"
        else:
            self.button["bg"]="red"


    def enter(self, event, num):
        #print(event.x)
        print("ok")
        self.canvas[num]["bg"]="#bec2d6"


    def leave(self, event, num):
        #print(event.x)
        print("leave")
        self.canvas[num]["bg"]="white"

    def menu_serial(self, event):
        #self.c = ttk.Combobox(self.window, values=self.board.find_serials(), width=10)
        #self.c.grid(row=4, column=1)
        #print("youp")
        self.c["values"]=self.board.find_serials()

class TemperatureFrame:
    def __init__(self, parent, controler):
        tk.Frame.__init__(self,parent)
        # manage menu
        menubar = Menu(self.window)
        filemenu = Menu(menubar, tearoff=0)
        setting = Menu(menubar, tearoff=0)
        filemenu.add_command(label="import config", command=self.file)
        filemenu.add_command(label="export settings", command=self.file)
        filemenu.add_command(label="import", command=self.file)

        setting.add_command(label="com config", command=self.file)
        setting.add_command(label="logs", command=self.file)

        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Settings", menu=setting)
        self.window["menu"] = menubar



app = SeaofBTCapp()
app.mainloop()

