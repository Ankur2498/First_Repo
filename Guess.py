import random
import argparse
import sys
from time import sleep
from colorama import Fore, Style, init #change the color of text in terminal.
init(autoreset=True)

def choose_level(name):
    """Handles level selection and returns number of chances."""
    while True:
        try:
            ask = int(input(
                '\n\n⁉️ Which level do you want to play?\n1 for Easy\n2 for Medium\n3 for Hard\n4 for Info\nYour choice: '
            ))
            if ask == 1:
                print("You got 7 chances to guess.")
                return 7
            elif ask == 2:
                print("You got 5 chances to guess.")
                return 5
            elif ask == 3:
                print("You got 3 chances to guess.")
                return 3
            elif ask == 4:
                sys.exit("\nℹ️ Info....\nChances in each level:\nEasy = 7\nMedium = 5\nHard = 3.")
            else:
                print("\n⚠️ You should select from (1-4).")
        except ValueError:
            print("\n⚠️ You should select from (1-4).")


def welcome_message(name, repeat):
    """Displays welcome message."""
    if not repeat:
        sleep(1.5)
        print(f"\n😊 Welcome {name} to Guess the Number Game.")
    else:
        sleep(0.3)
        print(f"\n😊 Welcome back {name}!")


def guess_game(name):
    """Runs one round of guessing game. Returns True if guessed correctly."""
    secret_number = random.randint(0, 7)
    try:
        user_input = int(input(f"\n{name}, guess a number (0–7): "))
        if 0 <= user_input <= 7:
            if user_input == secret_number:
                sleep(1)
                print(Fore.GREEN + Style.BRIGHT + "\n🎉 Hooray! You chose the correct number ✅")
                return True
            else:
                sleep(1.5)
                print(Fore.RED + Style.BRIGHT + f"❌ Oops! I chose {secret_number}.")
        else:
            print("⚠️ Please enter a number between 0 and 7.")
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")
    return False


def play_again(name):
    """Asks user if they want to play again."""
    while True:
        sleep(1)
        user_input = input(f"\n{name}, do you want to play again? (y = Yes, q = Quit): ").strip().lower()
        if user_input == 'y':
            return True
        elif user_input == 'q':
            print(f"\nThanks for playing {name}. See you next time! 🫡")
            return False
        else:
            print("⚠️ Please choose 'y' to play again or 'q' to quit.")


def main(name):
    """Main game loop."""
    while True:
        chances = choose_level(name)
        won = 0
        repeat = False

        for i in range(chances):
            if i == chances - 1:
                print("This is your last chance.🤠".center(50, '-'))

            welcome_message(name, repeat)
            result = guess_game(name)
            if result:
                won += 1
            repeat = True

        print(Fore.CYAN + f"\n🫡 You won {won} out of {chances} rounds. 🎉")

        if not play_again(name):
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Personalized Number Guessing Game.')
    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="Name of the player."
    )
    args = parser.parse_args()
    main(args.name)