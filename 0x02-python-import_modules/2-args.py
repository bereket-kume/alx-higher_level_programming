#!/usr/bin/python3
import sys
def args(argv):
    l = argv.split()
    if l == 0:
        print("{:d} arguments.".format(l))
    else:
        for i , arg in enumerate(argv):
            print("{:d}: {}".format(i + 1, arg))
