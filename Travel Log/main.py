# Create a program that adds to a travel log
from actions import add_log, view_log, delete_log


print("Welcome to your travel log")
# Ask user if they would like to add, view or delete a log from their log.


to_continue = True
while to_continue:
    user_action = input("Would you like to add, delete, or view a log? \n")
    if user_action == "view":
        country_visited = input("Which country's log will you like to view? \n")
        view_log(country_visited)

    elif user_action == "add":
        country_visited = input("Name of the country visited: \n")
        times_visited = int(input("How many times did you visit? \n"))
        cities_visited = (input("Which cities did you visit? Separate with a comma \n")).split(", ")
        add_log(country_visited, times_visited, cities_visited)
        print(f"You've successfully added {country_visited}'s entry into your log!")

    elif user_action == "delete":
        country_visited = input("Which country's log will you like to delete? \n")
        confirmation = input("Are you sure you want to delete the entry? Yes or No. You cannot undo this action. \n")
        if confirmation == "Yes":
            delete_log(country_visited)
        else:
            print("Deletion cancelled")
            to_continue = False

    else:
        print("You've entered the wrong command")

    user_action = input("Do you have other tasks to complete? Yes or No. \n")
    if user_action != "Yes":
        to_continue = False
