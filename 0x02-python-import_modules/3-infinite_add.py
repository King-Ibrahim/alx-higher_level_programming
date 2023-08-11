#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1

output = 0
i = 0
for arg in sys.argv:
    if i != 0:
        output += int(arg)
    else:
        i += 1
print("{:d}".format(output))

