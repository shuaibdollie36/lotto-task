from tkinter import *
from playsound import playsound
from tkinter import messagebox


root = Tk()
root.title("Lotto Machine")
root.geometry("750x400")
root.config(bg="purple")


num_label = LabelFrame(root, text="Enter your numbers", width=700, height=100, bg="yellow",font=("Arial",20))
num_label.place(x=25, y=40)
num1 = Spinbox(num_label, from_=1, to=49 , width=2,bg="purple",fg="white",font=("Arial",20))
num1.place(x=90, y=10)
num2 = Spinbox(num_label , from_=1, to=49, width=2,bg="purple",fg="white",font=("Arial",20))
num2.place(x=190, y=10)
num3 = Spinbox(num_label, from_=1, to=49, width=2,bg="purple",fg="white",font=("Arial",20))
num3.place(x=290, y=10)
num4 = Spinbox(num_label, from_=1, to=49, width=2,bg="purple",fg="white",font=("Arial",20))
num4.place(x=390, y=10)
num5 = Spinbox(num_label, from_=1, to=49, width=2,bg="purple",fg="white",font=("Arial",20))
num5.place(x=490, y=10)
num6 = Spinbox(num_label, from_=1, to=49, width=2,bg="purple",fg="white",font=("Arial",20))
num6.place(x=590, y=10)
results = Label(root, text="Results:", bg="yellow",font=("Arial",20))
results.place(x=100, y=200)

def nextscreen():
    root.destroy()
    import main4
prize_button = Button(root, text="Claim prize", width=20, bg="yellow",command=nextscreen)
prize_button.place(x=100, y=300)


exit_button = Button(root, text="Exit", width=20, bg="yellow",command=exit)
exit_button.place(x=500, y=300)



root.mainloop()