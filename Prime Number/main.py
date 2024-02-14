# lil program to determine if a number entered by the user is Prime Number


user_no = int(input("Enter number you want to check: "))


def prime_checker(number=user_no):
    if number < 2:
        print(f"{number} is not a prime number")
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{number} is a prime number!")
        else:
            print(f"{number} is not a prime number")


prime_checker()
