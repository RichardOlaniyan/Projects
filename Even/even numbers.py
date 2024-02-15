# Sum of all the even numbers between 0 and input no
input_no = int(input("What is the number you have in mind? "))
even_sum = 0

for number in range(0, input_no + 1, 2):
    even_sum += number
print(f"The sum of even numbers between 0 and {input_no} is: {even_sum}")
