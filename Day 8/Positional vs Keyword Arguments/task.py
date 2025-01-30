# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# functions with more than 1 input

def greet_with(name, location):
    print(f'Hello {name}.')
    print(f'What is it like in {location}?')

greet_with("Angela", "England")


# positional arguments
# def my_function(a, b, c):
# do this with a
# then do this with b
# finally do this with c

greet_with(location="england", name="angela")


def calculate_love_score(name1, name2):
    letter_list = []
    true_check = ["t", "r", "u", "e"]
    love_check = ["l", "o", "v", "e"]
    true_amt = 0
    love_amt = 0

    for letters in name1:
        letter_list.append(letters.lower())
    for letters in name2:
        letter_list.append(letters.lower())
    # print(letter_list)

    for char in letter_list:
        if char in true_check:
            true_amt += 1
        if char in love_check:
            love_amt += 1
    love_score = str(true_amt) + str(love_amt)
    # print(true_amt)
    # print(love_amt)
    print(love_score)


calculate_love_score("JACK", "TRINH")
calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score("Brad Pitt", "Jennifer Aniston")
calculate_love_score("Prince William", "Kate Middleton")
calculate_love_score("Brian Nguyen", "Emily Chan")