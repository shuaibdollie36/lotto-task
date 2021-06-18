from tkinter import *
import requests as rq
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests.exceptions

root = Tk()
root.title("Lotto Machine: Thunderball")
root.geometry("750x400")
root.config(bg="purple")

value = IntVar()

information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
information_json = information.json()

conversion_rate = information_json['conversion_rates']

value_label = Label(root, text="Value", font=("Arial", 11))
value_label.config(bg="yellow")
value_label.place(x=80, y=50, width=180, height=30)

value_entry = Entry(root, textvariable=value, width=20)
value_entry.config(bg="white")
value_entry.place(x=80, y=100, width=180, height=30)


winnings_label = Label(root, text="Winnings", font=("Arial", 11))
winnings_label.config(bg="yellow")
winnings_label.place(x=300, y=250, width=180, height=30)



from_label = Label(root, text="From: ZAR", font=("Arial", 11))
from_label.config(bg="YELLOW")
from_label.place(x=80, y=150, width=180, height=30)

convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
    convert_list.place(x=500,y=40)

convert_label = Label(root, text="Converted to: ", font=("", 11))
convert_label.config(bg="yellow")
convert_label.place(x=330,y=150,height=30)


def convert_curr():
    num = float(value_entry.get())
    print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    convert_label['text'] = round(ans, 2)


convert_btn = Button(root, command=convert_curr, text="Convert", font=("Arial", 11), width=10)
convert_btn.config(bg="yellow")
convert_btn.place(x=330, y=100)

def back_button():
    msg = messagebox.askquestion("Return","Would you like to return to your Banking Details")
    if msg == "yes":
        root.destroy()
        import main4

back_button = Button(root, text="Back", width=20, bg="yellow", command=back_button)
back_button.place(x=80, y=300)

exit_button = Button(root, text="Exit", width=20, bg="yellow", command=exit)
exit_button.place(x=490, y=300)

def erase():
    value_entry.delete(0,"end")


clear_button = Button(root, text="Clear", width=20, bg="yellow", command=erase)
clear_button.place(x=80, y=240)








root.mainloop()



