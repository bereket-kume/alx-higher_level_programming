#!/usr/bin/python3
def remove_char_at(str, n):
    x = []
    if n <= len(str):
        for i in str:
            x.append(i)
        del x[n]
    else:
        print("{}".format(str))
    print("{}".format("".join(x)))
