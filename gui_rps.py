from tkinter import *

window = Tk()
window.title("Rock Papers Siccors")
window.geometry("500x500")
window.config(bg="black")

def No():
    labelNo = Label(window,
                    text="Thanks for visiting Bye...",
                    font=("Arial",20),
                    foreground="cyan",
                    background="black")
    labelNo.pack()
def Yes():
    game()
def game():
    print("Hi")

game()

def IfPlay():
        
    label = Label(window,
                text="welcome to Rock\n Papers and Sciccors.",
                font=("Comic Sans",20,"bold"),
                foreground="#00ff00",
                background="black")
    label.pack()
    label2 = Label(window,
                text="Do you want to play.",
                font=("Comic Sans",15),
                foreground="white",
                background="black",
                pady=100)
    label2.pack()
    button = Button(window,
                    command=Yes,
                    text="yes",
                    font=('Arial',15,'underline'),
                    foreground="black",
                    background="white",
                    activeforeground="black",
                    activebackground="white",
                    )
    button.place(x=100,y=350)
    button2 = Button(window,
                    command=No,
                    text="no",
                    font=('Arial',15,'underline'),
                    foreground="black",
                    background="white",
                    activeforeground="black",
                    activebackground="white",
                    )
    button2.place(x=350,y=350)
IfPlay()


window.mainloop()