import random
import string

secret_number = ''.join(random.sample(string.digits, k=4))
print(secret_number)


def compare_lists(player_guess, secret_number):
    cow_count = 0
    bull_count = 0
    for i in range(4):
        if player_guess[i] == secret_number[i]:
            cow_count += 1
        elif player_guess[i] in secret_number[i]:
            bull_count += 1
    return cow_count, bull_count


guess_count = 0
correct_guess = True
while correct_guess:
    player_guess = input("Guess a 4 digit number: ")
    guess_count += 1
    if secret_number == player_guess:
        correct_guess = False
        print(f"{player_guess} is the correct guess")
        print(f"{guess_count} is the total number of guesses")
    else:
        cow_count, bull_count = compare_lists(player_guess, secret_number)
        print(f"{cow_count} cows and {bull_count} bulls")
        print(f"{guess_count} is the total number of guesses")
