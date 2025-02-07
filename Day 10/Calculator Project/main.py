import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
calculator = True
operations = {"+": add,
             "-": subtract,
             "*": multiply,
             "/": divide,
             }
output = ""
def calculations_continued(total):
    print("+\n" + "- \n" + "* \n" + "/")
    calc_1 = total
    operator = input("Pick one of the operations above.\n")
    calc_2 = float(input("What's the second number \n"))
    output = operations[operator](calc_1, calc_2)
    print(f'{calc_1} {operator} {calc_2} = {output}')
    continue_calc = input(f"Type 'yes' to continue calculating with {output}, or type 'no' to start a new calculation:  \n").lower()
    if continue_calc == "yes":
        calculator == False
        calculations_continued(output)

# # multiply 4 * 8 using the dictionary
# addition = operations["+"](4,8)
# print(addition)
# # printed 12

while calculator == True:
    calc_1 = float(input("Whats the first number?\n"))
    print("+\n" + "- \n" + "* \n" + "/")
    operator = input("Pick one of the operations above.\n")
    calc_2 = float(input("What's the second number \n"))
    output = operations[operator](calc_1, calc_2)
    print(f'{calc_1} {operator} {calc_2} = {output}')
    continue_calc = input(f"Type 'yes' to continue calculating with {output}, or type 'no' to start a new calculation:  \n").lower()
    if continue_calc == "yes":
        calculator == False
        calculations_continued(output)
