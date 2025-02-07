capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

# Key contains alist as you cannot pair multiple values
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"],
}
# Print Lille
print(travel_log["France"][1])

# print D
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_logs = {
    "France" : {
        "total_visits" : 8,
        "cities_visited" : ["Paris", "Lille", "Dijon"],
    },
    "Germany" : {
        "total_visits" : 4,
        "cities_visited" : ["Stuttgart", "Berlin", "Hamburg"],
    },
}

print(travel_logs)
# print Stuttgart
print(travel_logs["Germany"]["cities_visited"][0])

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
print(final_dictionary)
