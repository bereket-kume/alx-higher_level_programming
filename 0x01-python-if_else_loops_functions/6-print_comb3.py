#!/usr/bin/python3
val = []
for i in range(100):
    if i < 10:
        val.append(i)
    elif i == int(str(i)[::-1]) or i > int(str(i)[::-1]):
        continue
    else:
        val.append(i)
print(", ".join(str(x).zfill(2) for x in val))


