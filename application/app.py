import tkinter as tk
LARGE_FONT = ("Verdana", 12)

from tkinter import ttk
from application.board import *
from application.data_change import *
board = Board()
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, TemperatureFrame, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        print("pp")
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self["bg"]="white"
        global board
        self.menubar = tk.Menu(self)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        setting = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="import config", command=self.file)
        filemenu.add_command(label="export settings", command=self.file)
        filemenu.add_command(label="import", command=self.file)

        setting.add_command(label="com config", command=self.file)
        setting.add_command(label="logs", command=self.file)

        self.menubar.add_cascade(label="File", menu=filemenu)
        self.menubar.add_cascade(label="Settings", menu=setting)

        controller.configure(menu = self.menubar)

        self.canvas = [0] * 10
        self.state = [0] * 10
        self.canvas[1] = tk.Canvas(self, bg="white", height=200, width=200, bd=2, highlightthickness=0,
                                relief='ridge')
        self.photo = tk.PhotoImage(file="thermometer.png")
        self.canvas[1].create_image(100, 100, image=self.photo)
        self.canvas[1].create_text(100, 180, text="temperature")

        self.canvas[1].grid(row=0, column=0)

        self.photo1 = tk.PhotoImage(file="spirit_level.png")
        self.canvas[2] = tk.Canvas(self, bg="white", height=200, width=200, bd=2, highlightthickness=0,
                                relief='ridge')
        self.canvas[2].create_image(100, 100, image=self.photo1)
        self.canvas[2].create_text(100, 180, text="accelerometer")
        self.canvas[2].grid(row=0, column=1)

        self.photo2 = tk.PhotoImage(file="led-light.png")
        self.canvas[3] = tk.Canvas(self, bg="white", height=200, width=200, bd=2, highlightthickness=0,
                                relief='ridge')
        self.canvas[3].create_image(100, 100, image=self.photo2)
        self.canvas[3].create_text(100, 180, text="leds")

        self.canvas[3].grid(row=0, column=2)

        self.photo3 = tk.PhotoImage(file="switch.png")
        self.canvas[4] = tk.Canvas(self, bg="white", height=200, width=200, bd=2, highlightthickness=0,
                                relief='ridge')
        self.canvas[4].create_image(100, 100, image=self.photo3)
        self.canvas[4].create_text(100, 180, text="buttons")
        self.canvas[4].grid(row=0, column=3)

        self.photo4 = tk.PhotoImage(file="photo-camera.png")
        self.canvas[5] = tk.Canvas(self, bg="white", height=200, width=200, bd=2, highlightthickness=0,
                                relief='ridge')
        self.canvas[5].create_image(100, 100, image=self.photo4)
        self.canvas[5].create_text(100, 180, text="cam")

        self.canvas[5].grid(row=2, column=0)

        self.photo5 = tk.PhotoImage(file="microphone.png")
        self.canvas[6] = tk.Canvas(self, bg="white", height=200, width=200, bd=2, highlightthickness=0,
                                relief='ridge')
        self.canvas[6].create_image(100, 100, image=self.photo5)
        self.canvas[6].create_text(100, 180, text="sound")
        self.canvas[6].grid(row=2, column=1)

        self.photo7 = tk.PhotoImage(file="laser-pointer.png")
        self.canvas[7] = tk.Canvas(self, bg="white", height=200, width=200, bd=2, highlightthickness=0,
                                relief='ridge')
        self.canvas[7].create_image(100, 100, image=self.photo7)
        self.canvas[7].create_text(100, 180, text="laser")
        self.canvas[7].grid(row=2, column=2)

        self.photo6 = tk.PhotoImage(file="plus.png")
        self.canvas[8] = tk.Canvas(self, bg="white", height=200, width=200, bd=2, highlightthickness=0,
                                relief='ridge')
        self.canvas[8].create_image(100, 100, image=self.photo6)
        self.canvas[8].create_text(100, 180, text="add elements")
        self.canvas[8].grid(row=2, column=3)

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=3, columnspan=5, sticky="ew")

        L1 = tk.Label(self, text="enter serial Port : ", bg="white")

        L1.grid(row=4, column=0)

        self.c = ttk.Combobox(self, values=board.find_serials(), width=10)
        self.c.grid(row=4, column=1)
        self.c.bind("<Button-1>", self.menu_serial)

        button = tk.Button(self, text="pair", command=self.pair, bg="red")
        button.grid(row=4, column=2)

        L1 = tk.Label(self, text="enter socket address::port : ", bg="white")
        L1.grid(row=5, column=0)

        self.E1 = tk.Entry(self, bd=5, bg="white")
        self.E1.grid(row=5, column=1)

        self.button = tk.Button(self, text="pair", command=self.pair, bg="red")
        self.button.grid(row=5, column=2)

        self.num = 1
        self.canvas[1].bind('<Enter>', lambda event, arg=1: self.enter(event, arg))
        self.canvas[1].bind('<Leave>', lambda event, arg=1: self.leave(event, arg))
        self.canvas[1].bind('<Button-1>', lambda event:controller.show_frame(TemperatureFrame))
        self.num = 2
        self.canvas[2].bind('<Enter>', lambda event, arg=2: self.enter(event, arg))
        self.canvas[2].bind('<Leave>', lambda event, arg=2: self.leave(event, arg))


        self.num = 3
        self.canvas[3].bind('<Enter>', lambda event, arg=3: self.enter(event, arg))
        self.canvas[3].bind('<Leave>', lambda event, arg=3: self.leave(event, arg))
        self.canvas[3].bind('<Button-1>', self.send_led)

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

        self.photo8 = tk.PhotoImage(file="ok.png")
        self.canvas[9] = tk.Canvas(self, bg="white", height=30, width=30, bd=2, highlightthickness=0,
                                relief='ridge')
    def file(self):
        print("ok")

    def menu_serial(self, event):
        global board
        self.c["values"]=board.find_serials()

    def pair(self):
        global board
        portname = self.E1.get()
        portname = portname.split(":")
        board.connect_to_wifi(str(portname[0]), int(portname[1]))
        print("connect to "+ portname[0]+portname[1])
        #data = Data("192.168.0.11")
        #board.socketWriter.send(data)
        if(board.wifi_connected):
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

    def send_led(self, event):
        global board

        if self.state[2] == 0:
            data = DataChange("led", "01")
            self.state[2] = 1

        else:
            data = DataChange("led", "02")
            self.state[2] = 0
        # if board.wifi_connected == True:
        board.socketWriter.send(data)

    def send_led_off(self, event):
        global board

        if self.state[2]==0:
            data =DataChange("led", "01")
            self.state[2]=1

        else:
            data = DataChange("led", "02")
            self.state[2]=0
        #if board.wifi_connected == True:
        board.socketWriter.send(data)

class TemperatureFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self["bg"]="white"
        self.canvas = [0] * 10
        self.canvas[1] = tk.Canvas(self, bg="white", height=200, width=400, bd=2, highlightthickness=0,
                                relief='ridge')
        self.photo = tk.PhotoImage(file="thermometer.png")
        self.canvas[1].create_image(200, 100, image=self.photo)
        self.canvas[1].create_text(200, 180, text="temperature")
        self.canvas[1].grid(row=0, column = 0, columnspan=2, rowspan=2)

        self.canvas[2] = tk.Canvas(self, bg="white", height=40, width=400, bd=2, highlightthickness=0,
                                   relief='ridge')
        self.canvas[2].create_text(60, 21, text="on_value(value):")
        self.canvas[2].grid(row=0,column=3)
        self.txt = tk.Text(self, height=30, width=57, wrap=tk.WORD)
        self.txt.grid(row=1,column=3, rowspan=5)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

app = SeaofBTCapp()
app.mainloop()