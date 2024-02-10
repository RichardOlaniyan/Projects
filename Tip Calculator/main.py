print('Welcome to the Tip Calculator')
total_bill = float(input('What was the total bill? $'))
no_of_people = int(input('How many people will split the bill? '))
tip = float(input('What is the % of tip you would like to give? 10, 12, or 15? '))


def single_pay():
    split_amount = total_bill / no_of_people
    individual_pay = (split_amount * (tip/100) + split_amount)
    return round(individual_pay, 1)


print(f"Each person should pay: ${single_pay()}")
