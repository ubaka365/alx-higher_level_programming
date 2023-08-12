#!/usr/bin/python3<F11>
import sys
if __name__ != "__main__":<F11>
    exit()
    argc = len(sys.argv) - 1<F11>
    i = 0
    result = 0
    for arg in sys.argv:
        if i ! = 0:
            result += int(arg)
        else:
            i += 1
            print("{:d}".format(result))
