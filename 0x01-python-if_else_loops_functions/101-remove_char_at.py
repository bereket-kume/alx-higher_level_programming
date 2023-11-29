#!/usr/bin/python3
def remove_char_at(str, n):
    x = []
    for i in str:
        x.append(i)
    del x[n]
    print("{}".format("".join(x)))
