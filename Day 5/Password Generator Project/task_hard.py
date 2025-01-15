# Author: Brian Pham Nguyen
# GitHub username: bnguyening
# Date:
# Description:
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_bank = []
password = ""
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
# 52 letters
i = 0
while i < nr_letters:
    random_letter = random.randint(0, 51)
    password_letter = letters[random_letter]
    password_bank.append(password_letter)
    i += 1

nr_symbols = int(input(f"How many symbols would you like?\n"))
# 10 numbers
i = 0
while i < nr_symbols:
    random_symbol = random.randint(0, 8)
    password_symbol = symbols[random_symbol]
    password_bank.append(password_symbol)
    i += 1

nr_numbers = int(input(f"How many numbers would you like?\n"))
# 9 symbols
i = 0
while i < nr_numbers:
    random_number = random.randint(0, 9)
    password_number = numbers[random_number]
    password_bank.append(password_number)
    i += 1

password_bank_amt = len(password_bank)
random.shuffle(password_bank)
i = 0
for items in password_bank:
    password += items
    i += 1

print(f"Your password is {password}. Please write it down in a safe place." )