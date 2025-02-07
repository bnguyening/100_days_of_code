# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You did not input any names"
#
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"
#     print("this got printed")
# # return states the function is finished and to exit
# # print statement does not get called
#
# print(format_name(input("what is your first name?"), input("what is your last name")))

def is_leap_year(year):
    # Write your code here.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f'{year} is a leap year'
            else:
                return f'{year} is not a leap year'
        else:
            return f'{year} is a leap year'
    else:
        return f'{year} is not a leap year'



print(is_leap_year(int(input("What year would you like to check \n"))))

