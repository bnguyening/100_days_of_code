import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
card_number = random.randint(0, 4)
print(card_number)

card_roulette = friends[card_number]
print(card_roulette)
# or
random_index = random.randint(0, 4)
print(friends[random_index])

# random.choice is the simplist way

print(random.choice(friends))

