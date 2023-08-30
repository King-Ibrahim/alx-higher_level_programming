#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argStr = "{:d} argument"
    argc = len(sys.argv) - 1
    if argc == 1:
        argStr += ':'
    elif argc == 0:
        argStr += 's.'
    else:
        argStr += 's:'
    print(argStr.format(argc))
    i = 0
    for arg in sys.argv:
        if i != 0:
            print("{:d}: {:s}".format(i, arg))
        i += 1
