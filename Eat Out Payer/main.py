import random

names = input("What are the names of your friends? Separate each name with a comma ")
list_name = names.split(", ")


def randomize():
    list_length = len(list_name)
    random_name = random.randint(0, list_length)
    return random_name, list_name[random_name]


print(f"The name of the person buying dinner is {randomize()}")
