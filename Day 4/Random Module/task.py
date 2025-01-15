import random
# import my_module

random_integer = random.randint(1, 10)

print(random_integer)
# print(my_module.my_favorite_number)

# prints our a random floating point number 0 - 1. input is itself ()
random_numner_0_to_1 = random.random() * 10 # multiply lower and upper by 10 0 x 10 1 x 10
print(random_numner_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

#  difference is that random.random will almost never include upper bound (1) random.uniform might include
#  she recommends using random.random

heads_tails = random.randint(1, 2)

if heads_tails == 1:
    print("Heads")
else:
    print("Tails")