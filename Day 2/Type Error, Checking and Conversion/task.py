# len = return the length(number of items) of an object
# the argument may be a sequence such as string, byte, tuple, list
#  or range. or a collection such as a dictionary, set, or frozen set
print(len("cat"))

# how to check the data type of a given variable. type(____)
print(type("abc"))
print(type(False))
print(type(1))
print(type(1.1))

# Type conversion/type casting
print(type(int("123")))

print(int("123") + int("456"))
int()
float()
str()
bool()

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)
print(type(input("Enter your name")))
print(type(length_of_name))
print("Number of letters in your name: " + str(len(input("Enter your name"))))