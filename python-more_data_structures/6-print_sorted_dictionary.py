#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_sorted = sorted(a_dictionary)
    for element in keys_sorted:
        print(f"{element}: {a_dictionary[element]}")
