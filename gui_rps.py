from tkinter import *
from random import choices
from enum import Enum
import time

def main():
    def forget():
        label.pack_forget()
        label2.pack_forget()
        button.place_forget()
        button2.place_forget()

    def No():
        forget()
        no = Label(window,
                   text="Thanks for visiting.",
                   font=('Freestyle Script', 30),
                   fg="#00ff00",
                   bg='black')
        no.pack()

    def Yes():
        def win(pl, x, py, y):
            class RPS(Enum):
                ROCK = 1
                PAPER = 2
                SCISSORS = 3

            def forget3():
                yes.pack_forget()
                rock_button.place_forget()
                paper_button.place_forget()
                scissors_button.place_forget()
                try:
                    Win1_label.pack_forget()
                    win_label.pack_forget()
                except:
                    pass
                try:
                    Win2_label.pack_forget()
                    win2_label.pack_forget()
                except:
                    pass

            forget2()

            if x != y:
                Win1_label = Label(window,
                                text=f"{pl} won!...",
                                font=('Freestyle Script', 30),
                                fg='#00ff00',
                                bg="black")
                Win1_label.pack()
                win_label = Label(window,
                                text=f"{pl} chose {RPS(x).name}\n and {py} chose {RPS(y).name}.",
                                font=('Comic Sans', 20),
                                fg='cyan',
                                bg='black',
                                pady=100)
                win_label.pack()
                window.after(3000, lambda: [window.destroy(), main()])

            else:
                forget3()
                Win2_label = Label(window,
                                text=f"Game draw!...",
                                font=('Freestyle Script', 30),
                                fg='#00ff00',
                                bg="black")
                Win2_label.pack()
                win2_label = Label(window,
                                text=f"{pl} chose {RPS(x).name}\n and {py} chose {RPS(y).name}.",
                                font=('Comic Sans', 20),
                                fg='cyan',
                                bg='black',
                                pady=100)
                win2_label.pack()
                window.after(3000, lambda: [window.destroy(), main()])

        def forget2():
            yes.pack_forget()
            rock_button.place_forget()
            paper_button.place_forget()
            scissors_button.place_forget()

        def decide(num):
            forget2()
            player_choice = num
            rps_choice = int(choices([1, 2, 3])[0])  # Simulate computer move
            print(rps_choice)  # Debug output
            if player_choice == 2 and rps_choice == 1:
                win('You', player_choice, 'Python', rps_choice)
            elif player_choice == 3 and rps_choice == 2:
                win('You', player_choice, 'Python', rps_choice)
            elif player_choice == 1 and rps_choice == 3:
                win('You', player_choice, 'Python', rps_choice)
            elif player_choice == rps_choice:
                win('You', player_choice, 'Python', rps_choice)
            else:
                win('Python', rps_choice, 'You', player_choice)

        forget()

        yes = Label(window,
                    text="Choose Rock, Paper or Scissors.",
                    font=('Freestyle Script', 30),
                    fg="cyan",
                    bg='black')
        yes.pack()

        rock_button = Button(window, text='Rock',
                             command=lambda: decide(1),
                             font=('Arial', 16),
                             fg='#00ff00',
                             bg='black',
                             activeforeground='#00ff00',
                             activebackground='black')
        rock_button.place(x=50, y=350)

        paper_button = Button(window, text='Paper',
                              command=lambda: decide(2),
                              font=('Arial', 16),
                              fg='#00ff00',
                              bg='black',
                              activeforeground='#00ff00',
                              activebackground='black')
        paper_button.place(x=200, y=350)

        scissors_button = Button(window, text='Scissors',
                                 command=lambda: decide(3),
                                 font=('Arial', 16),
                                 fg='#00ff00',
                                 bg='black',
                                 activeforeground='#00ff00',
                                 activebackground='black')
        scissors_button.place(x=350, y=350)

    window = Tk()
    window.title("Rock Paper Scissors")
    window.geometry("500x500")
    window.config(bg="black")

    label = Label(window,
                  text="Welcome to Rock\n Paper and Scissors.",
                  font=("Comic Sans", 20, "bold"),
                  foreground="#00ff00",
                  background="black")
    label.pack()

    label2 = Label(window,
                   text="Do you want to play?",
                   font=("Comic Sans", 15),
                   foreground="white",
                   background="black",
                   pady=100)
    label2.pack()

    button = Button(window,
                    command=Yes,
                    text="Yes",
                    font=('Arial', 15, 'underline'),
                    foreground="black",
                    background="white",
                    activeforeground="black",
                    activebackground="white")
    button.place(x=100, y=350)

    button2 = Button(window,
                     command=No,
                     text="No",
                     font=('Arial', 15, 'underline'),
                     foreground="black",
                     background="white",
                     activeforeground="black",
                     activebackground="white")
    button2.place(x=350, y=350)

    window.mainloop()

if __name__ == "__main__":
    main()
