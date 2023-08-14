#!/usr/bin/python3
def no_c(my_string):
    charsList = list(my_string)
    for char in charsList:
        if char == 'c' or char == 'C':
            charsList.remove(char)
    return("".join(charsList))
