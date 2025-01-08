bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi)) #flooring round down
print(round(bmi)) # round up or down
print(round(3.9))
print(round(3.3))

# print(round()) can take 2 digits. the input and how many decimals
print(round(bmi, 2))

score = 0

#user scores a goal
print(score)
score += 2 # add 1 to the score count
print(score)
score -= 1 # subtract from score count
print(score)
score *= 2 # multiple score by
print(score)
score //= 2 # divide score by / for float // for int
print(score)

# f-strings
print("Your score is " + str(score))

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}")
print(f"Your Height is = {height}")
print(f"Your height is = {height}. Your score is = {score}. You are winning is {is_winning}")
