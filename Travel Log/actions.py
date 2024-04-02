travel_log = []


def add_log(country_visited, times_visited, cities_visited):
    new_country = {"country_visited": country_visited, "times_visited": times_visited, "cities_visited": cities_visited}
    travel_log.append(new_country)


def view_log(country_visited):
    found = True
    for log_entry in travel_log:
        if log_entry["country_visited"] == country_visited:
            print(
                f"You visited {log_entry['country_visited']} {log_entry['times_visited']} times. Cities visited: {', '.join(log_entry['cities_visited'])}")
            found = True
    if not found:
        print("No record found for that country in your log")


def delete_log(country_visited):
    for log_entry in travel_log:
        if log_entry["country_visited"] == country_visited:
            travel_log.remove(log_entry)
            return print(f"Log entry for {country_visited} is no longer available")
        else:
            return print(f"Log entry for {country_visited} does not exist. Please try another entry")
