from tkinter import *
from tkinter import messagebox
from playsound import playsound
from random import randint

root = Tk()
root.title("Lotto Machine: Thunderball")
root.geometry("750x400")
root.config(bg="purple")

#labels
label1 = Label(root, text="Name:", bg="yellow")
label2 = Label(root, text="Surname:", bg="yellow")


label3 = Label(root, text="Email:", bg="yellow")
label4 = Label(root, text="Age:", bg="yellow")
label3.place(x=100, y=120)
label4.place(x=440, y=120)

#Placement for labels
label1.place(x=100, y=40)
label2.place(x=440, y=40)

entry1 = Entry(root, state="normal", bg="white")
entry1.place(x=120, y=75, width=180, height=30)
entry2 = Entry(root, state="normal" , bg="white")
entry2.place(x=460, y=75, width=180, height=30)


entry3 = Entry(root, state="normal", bg="white")
entry3.place(x=120, y=155, width=180, height=30)




entry4 = Entry(root, state="normal", bg="white")
entry4.place(x=460, y=155, width=180, height=30)

clear_button = Button(root, text="Clear", width=20, bg="yellow")
clear_button.place(x=100, y=300)

def exit():
    playsound("sound_effect.mp3")
    msg = messagebox.askquestion("Really", "Are you sure you want to exit ?")
    if msg == "yes":
        root.destroy()

def nextscreen():
    root.destroy()
    import main3


exit_button = Button(root, text="Exit", width=20, bg="yellow",command=exit)
exit_button.place(x=300, y=300)



def check():
    if int (entry4.get()) < 18:
        messagebox.showerror(message="You are too young to play")
    elif int(entry4.get()) >= 18:
        messagebox.showinfo(message="Lets play")
        root.destroy()
        import main3


verify_button = Button(root, text="Verify", width=20, bg="yellow",command=check)
verify_button.place(x=500, y=300)




root.mainloop()
