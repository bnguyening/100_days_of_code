print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# to get percentage ((tip / 100) + 1) for calculation = 1.tip%
tip_percent = tip / 100 + 1
# print(tip_percent)
split = round((bill * tip_percent ) / people, 2)
print(f"Each person should pay: ${split}")