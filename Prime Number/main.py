# lil program to determine if a number entered by the user is Prime Number


user_no = int(input("Enter number you want to check: "))


def prime_checker(number=user_no):
    is_prime = True
    if number < 2:
        print(f"{number} is not a prime number")
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{number} is a prime number!")
        else:
            print(f"{number} is not a prime number")
    return is_prime


# Trying to prompt the user to enter another number if the previous number entered is not a prime number
to_continue = True
while to_continue:
    command = prime_checker(user_no)
    if command is False:
        user_command_first = int(input('Enter another number: \n'))
        prime_checker(user_command_first)
    elif command is True:
        user_command_second = input('Type Yes to continue or about to end \n')
        if user_command_second == "abort":
            to_continue = False
else:
    print("Thank you using the Prime Checker")
