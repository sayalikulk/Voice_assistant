import tkinter as tk
from PIL import Image, ImageTk
from ok_olivia import *


LARGE_FONT= ("Verdana", 12)

class mainfunc(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        logo = Image.open('image.png')
        newsize = (200, 200)
        logo=logo.resize(newsize)
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(self,image=logo)
        logo_label.image = logo
        logo_label.place(relx = 0.5,
                   rely = 0.2,
                   anchor = 'center')


        label = tk.Label(self, text="Ok Olivia!", font=("Arial", 25))
        label.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')

        button = tk.Button(self, text="Lets get started!",
                            command=lambda: controller.show_frame(PageOne))
        
        button.place(relx = 0.5, rely = 0.6, anchor = tk.CENTER)
    


class PageOne(tk.Frame):
    

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Ok Olivia!", font=("Arial", 25))
        label.place(relx = 0.5,
                   rely = 0.2,
                   anchor = 'center')


        logo1 = Image.open('mic.png')
        newsize = (100, 100)
        logo1=logo1.resize(newsize)
        logo1 = ImageTk.PhotoImage(logo1)
        button2 = tk.Button(self, text="Page Two",command=work)

        button2.config(image = logo1)
        button2.image = logo1
        button2.place(relx = 0.5,
                   rely = 0.4,
                   anchor = 'center')
        label = tk.Label(self, text="Ask me anything!", font=LARGE_FONT)
        label.place(relx = 0.5,
                   rely = 0.6,
                   anchor = 'center')
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(relx = 0.5,
                   rely = 0.7,
                   anchor = 'center')

app = mainfunc()
app.wm_geometry("600x600")
app.mainloop()
