# Nesting dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}
print(travel_log["France"]["cities_visited"])

# Nesting dictionary in a list
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]
print(travel_log[1]["cities"])


def add_new_country(country_visited, times_visited, cities_visited):
    travel_new = {
        "country": country_visited,
        "visits": times_visited,
        "cities": cities_visited
    }

    # travel_new = {}
    # travel_new["country"] = country_visited
    # travel_new["visits"] = times_visited
    # travel_new["cities"] = cities_visited

    travel_log.append(travel_new)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

