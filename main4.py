from tkinter import *
from tkinter import messagebox
from playsound import playsound
from random import randint
from PIL import Image, ImageTk


root = Tk()
root.title("Lotto Machine: Thunderball")
root.geometry("750x400")
root.config(bg="purple")

bank_label = Label(root, text="Banking Details", bg="yellow",font=("Arial",20))
bank_label.place(x=270, y=20)

label5 = Label(root, text="Account Holder", bg="yellow")
label6 = Label(root, text="Bank", bg="yellow")
label5.place(x=50, y=80, width=220, height=30)
label6.place(x=50, y=120, width=220, height=30)

entry5 = Entry(root, state="normal", bg="white")
entry5.place(x=400, y=80, width=180, height=30)




entry6 = Entry(root, state="normal", bg="white")
entry6.place(x=400, y=120, width=180, height=30)



root.mainloop()