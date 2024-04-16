import random
from os import system, name


def main() -> None:
    print("Welcome to the Blackjack Game")
    print("The rules are simple: Try to get as close to 21 as possible without going over.")
    print("If you go over 21, you lose.")
    print("If you get 21, you win.")
    players_card = []
    dealers_card = []
    


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    main()
    clear()
