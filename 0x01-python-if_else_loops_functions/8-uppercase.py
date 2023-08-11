#!/usr/bin/python3
def uppercase(str):
    for i in str:
        temp = ord(i)
        if temp >= 97 and temp <= 122:
            proto = chr(temp - 32)
        else:
            proto = i
        print('{}'.format(proto), end="")
    print()

