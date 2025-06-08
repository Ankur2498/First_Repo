import random
import argparse
import sys
from enum import Enum


def rps(name="Player"):
    # Class to manage points and game count
    class Umpire:
        def __init__(self, name, point):
            self.name = name
            self.point = point

        def add_point(self):
            self.point += 1

        def show_point(self):
            print(f"{self.name} wins = {self.point}")

        def show_game_count(self):
            print(f"Game count = {self.point}")

    # Create instances for Python, player, and total games
    python_player = Umpire("Python", 0)
    player = Umpire(name, 0)
    game_count = Umpire("Total Games", 0)

    # Game loop
    while True:
        print(f"\nWelcome {name} to Rock-Paper-Scissors!")

        # Get user's choice
        try:
            player_choice = int(input(
                f"\n{name}, choose an option:\n1 for Rock\n2 for Paper\n3 for Scissors\nYour choice: "))
            if player_choice not in [1, 2, 3]:
                sys.exit(f"\n{name}, you should enter a valid number (1-3).")
        except ValueError:
            sys.exit(f"\n{name}, you should enter a valid number (1-3).")

        # Determine the winner
        def main():
            python_choice = int(random.choice('123'))

            class RPS(Enum):
                Rock = 1
                Paper = 2
                Scissors = 3

            print(f"\n{name} chose {RPS(player_choice).name}, Python chose {RPS(python_choice).name}.")

            if python_choice == player_choice:
                print("It's a draw!")
            elif (python_choice == 1 and player_choice == 3) or \
                 (python_choice == 2 and player_choice == 1) or \
                 (python_choice == 3 and player_choice == 2):
                print(f"Python wins! {name}, you lose. 😭")
                python_player.add_point()
            else:
                print(f"Hooray! {name}, you won! 🎉")
                player.add_point()

            game_count.add_point()
            game_count.show_game_count()
            player.show_point()
            python_player.show_point()

        main()

        # Ask if user wants to play again
        def play_again():
            choice = input(f"\n{name}, do you want to play again? (y for yes / q for quit): ")
            if choice.lower() == 'y':
                return True
            elif choice.lower() == 'q':
                print("\nThanks for playing. Goodbye!")
                return False
            else:
                return play_again()

        if not play_again():
            break


# Entry point when run via terminal
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play a personalized Rock-Paper-Scissors game.')
    parser.add_argument(
        "-n", "--name", metavar="name", required=True,
        help="Your name for the game."
    )
    args = parser.parse_args()

    rps(args.name)
