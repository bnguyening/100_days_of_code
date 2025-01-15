print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age <= 12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")