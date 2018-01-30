from tkinter import *
from tkinter import ttk

class Window:
    def __init__(self):
        window = Tk()
        window["bg"]="white"

        # manage menu
        menubar = Menu(window)
        filemenu = Menu(menubar, tearoff=0)
        setting = Menu(menubar, tearoff=0)
        filemenu.add_command(label="import config", command = self.file)
        filemenu.add_command(label="export settings", command = self.file)
        filemenu.add_command(label="import", command = self.file)

        setting.add_command(label="com config", command=self.file)
        setting.add_command(label="logs", command=self.file)

        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Settings", menu=setting)
        window["menu"] = menubar

        self.canvas1 = Canvas(window,bg="white", height=200, width=200)
        photo = PhotoImage(file="thermometer.png")
        self.canvas1.create_image(100,100, image = photo)
        self.canvas1.grid(row=0,column=0)

        photo1 = PhotoImage(file="spirit_level.png")
        self.canvas2 = Canvas(window, bg="white", height=200, width=200)
        self.canvas2.create_image(100,100, image = photo1)
        self.canvas2.grid(row=0, column=1)

        photo2 = PhotoImage(file="led-light.png")
        self.canvas3 = Canvas(window, bg="white", height=200, width=200)
        self.canvas3.create_image(100,100, image = photo2)
        self.canvas3.grid(row=0, column=2)

        photo3 = PhotoImage(file="switch.png")
        self.canvas4 = Canvas(window, bg="white", height=200, width=200)
        self.canvas4.create_image(100,100, image = photo3)
        self.canvas4.grid(row=0, column=3)

        photo4 = PhotoImage(file="photo-camera.png")
        self.canvas5 = Canvas(window, bg="white", height=200, width=200)
        self.canvas5.create_image(100,100, image = photo4    )
        self.canvas5.grid(row=2, column=0)

        photo5 = PhotoImage(file="microphone.png")
        self.canvas6 = Canvas(window, bg="white", height=200, width=200)
        self.canvas6.create_image(100,100, image = photo5    )
        self.canvas6.grid(row=2, column=1)

        photo7 = PhotoImage(file="laser-pointer.png")
        self.canvas7 = Canvas(window, bg="white", height=200, width=200)
        self.canvas7.create_image(100,100, image = photo7    )
        self.canvas7.grid(row=2, column=2)

        photo6 = PhotoImage(file="plus.png")
        self.canvas8 = Canvas(window, bg="white", height=200, width=200)
        self.canvas8.create_image(100,100, image = photo6    )
        self.canvas8.grid(row=2, column=3)

        ttk.Separator(window, orient=HORIZONTAL).grid(row=3, columnspan=5, sticky="ew")

        L1 = Label(window, text="enter serial Port : ", bg="white")
        L1.grid(row=4,column=0)

        E1 = Entry(window , bd=5)
        E1.grid(row=4, column=1)

        button = Button(window,text="pair", command=self.pair, bg="white")
        button.grid(row=4, column =2)

        L1 = Label(window, text="enter socket address::port : ", bg="white")
        L1.grid(row=5, column=0)

        E1 = Entry(window, bd=5, bg="white")
        E1.grid(row=5, column=1)

        button = Button(window, text="pair", command=self.pair, bg="white")
        button.grid(row=5, column=2)
       # window.bind("<Key>", key)

        window.bind("<Enter>", self.change_color)

        window.mainloop()

    def file(self):
        print("file")

    def pair(self):
        print("pair")

    def change_color(self, event):
        if event.x < 200 and event.y <200 :
            self.canvas1["bg"]="gray"


win = Window()

