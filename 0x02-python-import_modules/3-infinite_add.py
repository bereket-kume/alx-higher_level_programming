#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arglen = len(sys.argv)
    sumx = 0
    for i in range(arglen):
        if i != 0:
            sumx += int(sys.argv[i])
    print(sumx)
