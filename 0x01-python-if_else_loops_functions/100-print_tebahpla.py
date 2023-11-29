#!/usr/bin/python3
a = ''
for i in range(ord('a'), ord('z') + 1):
    if i % 2 == 1:
        a += chr(i).capitalize()
    else:
        a += chr(i)
print("{}".format(a[::-1]), end='')
