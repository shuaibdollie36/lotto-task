from tkinter import *
from tkinter import messagebox
from playsound import playsound
from random import randint
from PIL import Image, ImageTk


import rsaidnumber
from playsound import playsound
from datetime import date, datetime, timedelta

root = Tk()
root.title("Lotto Machine: Thunderball")
root.geometry("750x400")
root.config(bg="purple")

now = datetime.now()





bank_label = Label(root, text="Banking Details", bg="yellow",font=("serif",20))
bank_label.place(x=270, y=20)

label6 = Label(root, text="Account Holder", bg="yellow")
label5 = Label(root, text="Bank", bg="yellow")
label5.place(x=50, y=80, width=220, height=30)
label6.place(x=50, y=120, width=220, height=30)

default_bank = "Select Bank"
default_var = StringVar(value=default_bank)
entry6 = OptionMenu(root, default_var,"Capitec","Standard Bank","Absa","FNB","Nedbank")
entry6.place(x=400, y=80, width=180, height=30)

label7 = Label(root, text="Account Number", bg="yellow")
label7.place(x=50, y=160, width=220, height=30)
entry7 = Entry(root, state="normal", bg="white")
entry7.place(x=400, y=160, width=180, height=30)


def submit():
    w = open("BankDetails.txt", "a+")
    w.write( entry5.get() + " " + " " + " " + " " + entry7.get() + " " + "Logged into App at:" + " " + " " + str(
            now) + "\n")
    w.close()


    if len(entry7.get()) > 11 or len(entry7.get()) < 11:
        messagebox.showerror("Error!","Account number must consist of 11 numbers")

    else:
        messagebox.showinfo("Thank You", "Your Details Have Been Submitted")
        root.destroy()


entry5 = Entry(root, state="normal", bg="white")
entry5.place(x=400, y=120, width=180, height=30)

accept_button = Button(root, text="Accept", width=20, bg="yellow", command=submit)
accept_button.place(x=500, y=300)

def erase():
    entry7.delete(0, "end")
    entry5.delete(0,"end")


clear_button = Button(root, text="Clear", width=20, bg="yellow", command=erase)
clear_button.place(x=100, y=300)


root.mainloop()