# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
#     }
# print(programming_dictionary["Loop"])
#
# programming_dictionary["Key"] = "A identifying item with a definition attached"
# print(programming_dictionary)
#
# dictionary_to_be_filled = {}
#
# # wipe an existing dictionary
# #
# # programming_dictionary = {}
# #
# # print(programming_dictionary)
#
# # edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)
#
# # Loop through a dictionary
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if 100 >= student_scores[student] >= 91:
        student_grades[student] = "Outstanding"

    elif 90 >= student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"

    elif 80 >= student_scores[student] >= 71:
        student_grades[student] = "Acceptable"

    elif 70 >= student_scores[student]:
        student_grades[student] = "Fail"

print(student_grades)