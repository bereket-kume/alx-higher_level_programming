#!/usr/bin/python3
def remove_char_at(str, n):
    x = []
    if n >= 0 and n < len(str):
        for i in str:
            x.append(i)
        del x[n]
        return ."".join(x)
    else:
        return str
