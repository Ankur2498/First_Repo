import random
import argparse

def welcome_message(name,repeat):
    if not repeat:
        print(f"😊 Welcome {name} to Guess the number game.")
    else:
        print(f"😊 Welcome back {name} to Guess Game.")



def guess_game(name):
    SecretNumber = random.randint(0,7)
    try:
        User_input = int(input(f"{name}, Guess what number I am thinking?(0-7)🤫\nYou chose: "))
        if User_input == SecretNumber:
            print(f"\nHooray!🎉 You chosed the correct number.✅")
        elif User_input > 7 or User_input < 0:
            print(f"{name}, you should give number from(0-7) only.")
        else:
            print(f"{name}, you missed it❌, I chose {SecretNumber}.")
    except ValueError:
        print(f"{name}, you should give number from(0-7) only.")



def PLayAgain(name):
    while True:
        User_input = input(f"\n{name}, do you want to play again?🧐\ny for Yes\nq for Quit.\nYour choice: ").strip().lower()
        if User_input == 'y':
            return True
        elif User_input == 'q':
            print(f"\nThanks for playing {name}. See you later!🫡")
            return False
        else:
            print(f"\n\n⚠️Please choose y to play again or q to quit.")


def main(name):
    repeat = False
    while True:
        welcome_message(name,repeat)
        guess_game(name)
        if not PLayAgain(name):
            break
        repeat = True
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Creating a personalised game.')
    parser.add_argument(
        "-n","--name",metavar="name",required=True,help="Name of the player."
    )
    args = parser.parse_args()

    main(args.name)