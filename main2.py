from tkinter import *
from tkinter import messagebox

import rsaidnumber
from playsound import playsound
from datetime import date, datetime, timedelta
import re

now = datetime.now()

root = Tk()
root.title("Lotto Machine: Thunderball")
root.geometry("750x400")
root.config(bg="purple")

def check():

    w = open("Details.txt", "a+")
    w.write(
        entry1.get() + " " + " " + entry2.get() + " " + " " + entry3.get() + " " + " " + entry4.get()+ " " + " " + "Logged into App at:" + " " + " " + str(
            now) + "\n")
    w.close()

    if int(entry4.get()) < 18:
        messagebox.showerror(message="You are too young to play")
    elif int(entry4.get()) >= 18:
        messagebox.showinfo(message="Lets play")
        root.destroy()
        import main3


# labels
label1 = Label(root, text="Name:", bg="yellow", width=10)
label2 = Label(root, text="Surname:", bg="yellow", width=10)

labelid = Label(root, text="ID number", bg="yellow", width=10)
labelid.place(x=100, y=200)
identry = Entry(root, state="normal", bg="white")
identry.place(x=100, y=240, width=180, height=30)

label3 = Label(root, text="Email:", bg="yellow", width=10)
label4 = Label(root, text="Age:", bg="yellow", width=10)
label3.place(x=100, y=120)
label4.place(x=440, y=120)

# Placement for labels
label1.place(x=100, y=40)
label2.place(x=440, y=40)

entry1 = Entry(root, state="normal", bg="white")
entry1.place(x=100, y=75, width=180, height=30)
entry2 = Entry(root, state="normal", bg="white")
entry2.place(x=440, y=75, width=180, height=30)

entry3 = Entry(root, state="normal", bg="white")
entry3.place(x=100, y=155, width=180, height=30)





entry4 = Entry(root, state="normal", bg="white")
entry4.place(x=440, y=155, width=180, height=30)


def check():
    player_id = identry.get()
    year = player_id[:2]
    if year >= "22":
        year = "19" + year
    else:
        year = "20" + year
    month = player_id[2:4]
    day = player_id[4:6]
    today = date.today()

    age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))

    if len(player_id) != 13:
        messagebox.showerror("Error", "Please enter valid ID number")
    elif age >= 18:
        messagebox.showinfo("Welcome", "Let's Play")
        root.destroy()
        import main3
    else:
        age = 18 - age
        messagebox.showerror("Warning", "You are too young to play. Please try again in " + str(age) + " years")

def erase():
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")
    entry4.delete(0, "end")
    identry.delte(0,"end")

clear_button = Button(root, text="Clear", width=20, bg="yellow", command=erase)
clear_button.place(x=100, y=300)

def exit():
    playsound("sound_effect.mp3")
    msg = messagebox.askquestion("Really", "Are you sure you want to exit ?")
    if msg == "yes":
        root.destroy()


def nextscreen():
    root.destroy()
    import main3


exit_button = Button(root, text="Exit", width=20, bg="yellow", command=exit)
exit_button.place(x=300, y=300)

verify_button = Button(root, text="Verify", width=20, bg="yellow", command=check)
verify_button.place(x=500, y=300)

root.mainloop()
