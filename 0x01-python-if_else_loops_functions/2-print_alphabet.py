#!/usr/bin/python3
a = ''
for i in range(ord('a'), ord('z') + 1):
    a += chr(i)
print("{}".format(a), end='')
