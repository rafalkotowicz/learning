"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from typing import Any

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one: list, list_two: list):
    if len(list_one) == len(list_two):
        if list_one == list_two:
            return EQUAL
        else:
            return UNEQUAL
    else:
        if len(list_one) < len(list_two):
            if __sublist(list_one, list_two):
                return SUBLIST
        else:
            if __sublist(list_two, list_one):
                return SUPERLIST

    return UNEQUAL


def __sublist(ls1: list[Any], ls2: list[Any]) -> bool:
    for i in range(0, len(ls2) - len(ls1) + 1):
        tmp_ls = ls2[i:i + len(ls1)]
        if tmp_ls == ls1:
            return True

    return False
