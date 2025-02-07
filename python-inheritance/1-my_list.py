#!/usr/bin/python3
"""
Module documented: 1-my_list
"""


class MyList(list):
    """
    Class documented: MyList
    Inherits from list.
    """
    def print_sorted(self):
        """
        Method documented: print_sorted
        Prints the list, but sorted.
        """
        print(sorted(self))
