fruits = ["cherry", "apple", "pear"]
print(fruits)

# state_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
# print( states_of_america)
# order is important in lists. Order is defined by placement in list

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[49])
# printing out index/position according to offset/placement in list name_of_list[X]
# negative index is possible. -1 starts at the end of the list
print(states_of_america[-1])
print(states_of_america[1])

# can change by adding to index
states_of_america[1] = "PencilVania"
print(states_of_america[1])

# adding to lists. Would add to the end. name_of_list.append()
states_of_america.append("Thadland")
print(states_of_america[50])

states_of_america.extend(["Angelaland", "BrianLand"])
print(states_of_america[51])
print(states_of_america[52])