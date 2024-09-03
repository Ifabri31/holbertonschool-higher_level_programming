#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
str1 = "and is greater than 5"
str2 = "and is less than 6 and not 0"
if number < 0:
    last_digit *= -1
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} {str1}")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} {str2}")
