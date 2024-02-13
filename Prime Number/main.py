# lil program to determine if a number entered by the user is Prime Number

user_no = int(input("Enter number you want to check: "))


def prime_checker(number=user_no):
    if number % number == 0 and number % 1 == 0:
        print(f"{number} is a prime number!")
    else:
        print(f"{number} is not a prime number")


print(prime_checker())
