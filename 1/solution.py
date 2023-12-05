import re


file = open('input.txt', 'r')
document = file.readlines()
real_digits = {"one": "one1one", "two": "two2two", "three": "three3three",
               "four": "four4four", "five": "five5five", "six": "six6six",
               "seven": "seven7seven", "eight": "eight8eight",
               "nine": "nine9nine", "zero": "zero0zero"}

sum = 0
for line in document:
    for word, digit in real_digits.items():
        line = line.replace(word, digit)
    nums = re.sub('\D', '', line)
    calibration_value = int(f"{nums[0]}{nums[-1]}")
    sum += calibration_value

print(sum)