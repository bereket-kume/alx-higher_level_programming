#!/usr/bin/python3
import sys
if __name == "__main__":
    exit()
mess = "{} argument"
arglen = len(sys.argv) - 1
if arglen == 0:
    mess += "s."
elif arglen == 1:
    mess += ":"
else:
    mess += "s:"
print(mess.format(arglen))
i = 0
for arg in sys.argv:
    if i != 0:
        print("{:d} {}".format(i, arg)
    i += 1
