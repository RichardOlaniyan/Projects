# Caesar Cipher lil program
import string

# message = input(f"What is your message? \n").lower()
# shift = int(input("What is the shift? \n")) % 26
# operation = input("Would you like to encode or decode this message? \n")


# Long Version
def caesar(original_message, shift_amt, which_operation):
    full_alpha = list(string.ascii_lowercase) + list(string.ascii_lowercase)
    if which_operation == 'encode':
        encoded_message = ""
        for alpha in original_message:
            position = full_alpha.index(alpha)
            new_position = position + shift_amt
            new_alpha = full_alpha[new_position]
            encoded_message += new_alpha
        return print(f"Your encoded message is: {encoded_message}")
    elif which_operation == "decode":
        decoded_message = ""
        for alpha in original_message:
            position = full_alpha.index(alpha)
            new_decoded_position = position - shift_amt
            new_alpha = full_alpha[new_decoded_position]
            decoded_message += new_alpha
        return print(f"Your decoded message is: {decoded_message}")
        pass
    else:
        print("Please enter a valid order: encode or decode.")


# Shortened version
def caesar_two(original_text, shift_amnt, cipher_operation):
    full_alpha = list(string.ascii_lowercase) + list(string.ascii_lowercase)
    new_message = ""
    if cipher_operation == "decode":
        shift_amnt *= -1
    for alpha in original_text:
        position = full_alpha.index(alpha)
        new_position = position + shift_amnt
        new_message += full_alpha[new_position]
    return print(f"Your {operation}d message is: {new_message}")


# Keeps the program running
will_continue = True

while will_continue:
    message = input(f"What is your message? \n").lower()
    shift = int(input("What is the shift? \n")) % 26
    operation = input("Would you like to encode or decode this message? \n")

    caesar_two(original_text=message, shift_amnt=shift, cipher_operation=operation)
    command = input("Would you like to continue? Type yes to continue or abort to end \n")
    if command == "abort":
        will_continue = False
else:
    print("Thank you for using the Caesar Cipher")
