import random
import time
from dataclasses import dataclass
from functools import wraps
from os import name, system


@dataclass
class GuessingGame:
    """Guessing Game class"""

    def __post_init__(self):
        """Initializes class variables"""
        self.game_status = None
        self.guesses_taken = []
        self.winning_number = random.randint(000, 999)

    def guess(self, number):
        """Takes a guess from the user"""
        if self.game_status is None:
            if self.guesses < 15:
                try:
                    number = int(number)
                    self.guesses_taken.append(number)

                    if self.last_guess == self.winning_number:
                        self.game_status = True
                    elif self.last_guess < self.winning_number:
                        print("ACCESS - DENIED  -code to low")
                    else:
                        print("ACCESS - DENIED  -code to high")
                except ValueError:
                    print("You must enter a number!")
            else:
                self.game_status = False

    @property
    def guesses(self):
        """Returns the number of guesses"""
        return len(self.guesses_taken) + 1

    @property
    def last_guess(self):
        """Returns the last guess taken"""
        return self.guesses_taken[-1]


def clear_screen() -> None:
    """Clears the screen"""
    _: int = system("cls" if name == "nt" else "clear")


def sleeper(func):
    """Wrapper function that adds a sleep delay to any function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(1)
        func(*args, **kwargs)

    return wrapper


@sleeper
def dots():
    """Prints three periods"""
    print("...")


def pauser(length: int = 3):
    """Pauses execution for the length amount of seconds

    It then prints three periods in between each pause
    """
    pause = 0
    while pause < length:
        dots()
        pause += 1


def initialize():
    """Initialization animation"""
    clear_screen()
    print("[--system--] enter code in 15 trys to avoid lockout\n")
    print("\nconnecting....")
    pauser()
    print("connection established\n")


@sleeper
def title_header(title: str, char: str = "-"):
    """Prints the title header"""
    clear_screen()
    title_line = f" {title} "
    title_length = len(title_line)
    border = char * title_length
    print(border)
    print(title_line)
    print(border)


def play_game():
    """Plays the game"""
    game = GuessingGame()
    try:
        while game.game_status is None:
            print("\nenter 3 digit access code..\n")
            guess = input("user:> ")
            authenticate()
            game.guess(guess)
    except KeyboardInterrupt:
        clear_screen()
        print("Game stopped by the user!")
        exit(0)

    return game


@sleeper
def authenticate():
    """Authenticating animation"""
    print("\nauthenticating ....")
    pauser(2)
    clear_screen()


@sleeper
def loose(number: int):
    """Prints the loose message"""
    print(f"\nSYSTEM LOCKED  -the code was {number}")
    print()


@sleeper
def win():
    """Prints the win message"""
    print("ACCESS - GRANTED")
    print("\nGAME OVER\n")


def main():
    """Entry point for the script"""
    initialize()
    title_header("MAINFRAME - LOGIN")
    game = play_game()

    if game.game_status is True:
        win()
    else:
        loose(game.winning_number)
    exit(0)


if __name__ == "__main__":
    main()
