import random
from tkinter import *
from playsound import playsound
from tkinter import messagebox
from random import sample
from datetime import date, datetime, timedelta



root = Tk()
root.title("Lotto Machine: Thunderball")
root.geometry("750x400")
root.config(bg="purple")

#spinbox
num_label = LabelFrame(root, text="Enter your numbers", width=700, height=80, bg="yellow",font=("Arial",20))
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
results = Label(root, text="Results:", bg="yellow",font=("Arial",12),width=10)
results.place(x=100, y=150, width=400)


def play():
    try:
        lot = sample(range(1, 49), 6)
        user_numbers = [int(num1.get()), int(num2.get()), int(num3.get()), int(num4.get()), int(num5.get()),
                        int(num6.get())]
        print(user_numbers)

        s = set(user_numbers).intersection(lot)
        print(len(s))

        if len(s) == 0:
            results.config(text="Your numbers were: " + str(user_numbers) + "\n" +
                                "The winning numbers are: " +
                                str(lot) + "\n" + "Sorry today is not your day" + "\n" + str(date.today()))
        if len(s) == 1:
            results.config(text="Your numbers were: " + str(user_numbers) + "\n" +
                                "The winning numbers are: " +
                                str(lot) + "\n" + "Sorry today is not your day " + "\n" + str(date.today()))

        if len(s) == 2:
            results.config(text="Your numbers were: " + str(user_numbers) + "\n" +
                                "The winning numbers are: " +
                                str(lot) + "\n" + "You won R 20.00" + "\n" + str(date.today()))

        if len(s) == 3:
            results.config(text="your numbers were: " + str(user_numbers) + "\n" +
                                "The winning numbers are: " +
                                str(lot) + "\n" + "you won R 100.00" + "\n" + str(date.today()))

        if len(s) == 4:
            results.config(
                text="Your numbers were: " + str(user_numbers) + "\n" + "The winning numbers are: " +
                     str(lot) + "\n" + "You won R 2384.00" + "\n" + str(date.today()))

        if len(s) == 5:
            results.config(
                text="Your numbers were: " + str(user_numbers) + "\n" +
                     "The winning numbers are: " +
                     str(lot) + "\n" + "R 8584.00" + "\n" + str(date.today()))

        if len(s) == 6:
            results.config(
                text="Your numbers were: " + str(user_numbers) + "\n" + "The winning numbers are: " +
                     str(lot) + "\n" + "You won the jackpot: R 10 000 000.00" + "\n" + str(date.today()))
    finally:
        play_button["text"] = "PLAY AGAIN"
        messagebox.showinfo("Thanks","Thank you for playing")

def nextscreen():
    playsound("sound_effect.mp3")
    root.destroy()
    import main4

def prize_button():
    playsound("winner.mp3")
    msg = messagebox.askquestion("Really", "Play Again?")
    if msg == "no":
        root.destroy()
        import main4

def erase():
    num1.delete(0, "end")
    num2 .delete(0, "end")
    num3.delete(0, "end")
    num4.delete(0, "end")
    num5.delete(0, "end")
    num6.delete(0, "end")

#buttons
clear_button = Button(root, text="Clear", width=20, bg="yellow", command=erase)
clear_button.place(x=500, y=250)


prize_button = Button(root, text="Claim prize", width=20, bg="yellow",command=prize_button)
prize_button.place(x=100, y=300)


exit_button = Button(root, text="Exit", width=20, bg="yellow",command=exit)
exit_button.place(x=500, y=300)

play_button = Button(root, text="PLAY",bg="yellow", width=20, command=play)
play_button.place(x=100, y=250)

root.mainloop()