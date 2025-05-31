from tkinter import *

def main():
    output = 'Error'

    window = Tk()
    window.geometry('400x400')
    window.config(bg="#4dd399")

    def board():
        board_label = Label(window,text=f"{output}",
                            height='5',
                            width='25',bg='white',fg='black',
                            font=('Cosmic Sans',20),
                            anchor='center')#s for bottom
        board_label.pack()
    board()

    #, def option():
        

    window.mainloop()
main()