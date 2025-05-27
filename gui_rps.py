from tkinter import *

window = Tk()
window.title("Rock Papers Siccors")
window.geometry("500x500")
window.config(bg="black")

label = Label(window,
              text="welcome to Rock\n Papers and Sciccors.",
              font=("Comic Sans",20,"bold"),
              foreground="#00ff00",
              background="black")
label.pack()

window.mainloop()