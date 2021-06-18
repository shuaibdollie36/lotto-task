from tkinter import *
from tkinter import messagebox
from playsound import playsound
from random import randint
from PIL import Image, ImageTk
import rsaidnumber
from datetime import date,datetime


root = Tk()
root.title("Lotto Machine: Thunderball")
root.geometry("750x400")
root.config(bg="purple")

image1 = ImageTk.PhotoImage(Image.open("lolo.png"))
image_label = Label(image=image1,bg='purple',pady=45,padx=45)
image_label.place(x=240,y=50)

class Intel:
    def __init__(self, root):
        self.next_button = Button(root, text="Click to Play", width=20, bg="yellow", command=self.nextscreen)
        self.next_button.place(x=290, y=300)

    def nextscreen(self):
        root.destroy()
        import main2


obj = Intel(root)
root.mainloop()