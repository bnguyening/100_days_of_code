# modulo operator is the remainder after division
print(6 % 3)
print(10 % 3)
print(16 % 7)

number = int(input("Please enter a number"))
even_or_odd = (number % 2)
if even_or_odd == 0:
    print("even")
else:
    print("Odd")