# Create a program that adds to a travel log
from Actions import add_log, view_log, delete_log
print("Welcome to your travel log")
# Ask user if they would like to add, view or delete a log from their log.
user_action = input("Would you like to view, add, or delete a log? ")
travel_log = [
    {
        "country_visited": "Spain",
        "times_visited": 2,
        "cities_visited": ["Malaga", "Ibiza"]
    }
]
if user_action == "view":
    country_visited = input("Which country's log will you like to view? ")
    view_log(country_visited, travel_log)
    pass
elif user_action == "add":
    country_visited = input("Name of the country visited: ")
    times_visited = int(input("How many times did you visit? "))
    cities_visited = list(input("Which cities did you vist? "))
    add_log(country_visited, times_visited, cities_visited, travel_log)
    pass
elif user_action == "delete":
    country_visited = input("Which country's log will you like to delete? ")
    delete_log(country_visited, travel_log)
    pass
else:
    print("You've entered the wrong command")





