#!/usr/bin/python3
def print_last_digit(number):
    a = abs(number) % 10
    print(f"{a}", end="")
    return a
