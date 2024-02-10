guess = 20
user_guess = 0
while guess != user_guess:
    user_guess = int(input("Enter your first guess: "))
    if user_guess > guess:
        print('You guessed wrong, please try again')
    elif user_guess < guess:
        print('You guessed wrong, please try again')
    else:
        print('You made the right guess!')
        break
