def format_name(f_name, l_name):
    # print(f_name.title())
    # print(l_name.title())
    # print(f_name + " " + l_name)
    formated_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(f'{formated_f_name} {formatted_l_name}')
    return f'{formated_f_name} {formatted_l_name}'

format_name("briSDan", "ngDSuyen")
formatted_string = format_name("BRIAN", "NGUYEN")
print(formatted_string)
# output = len("Brian")

def function_1(text):
    return text + text
def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)
