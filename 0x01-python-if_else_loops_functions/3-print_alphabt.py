#!/usr/bin/python3
a = ''
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        a += chr(i)
print("{}".format(a), end='')
