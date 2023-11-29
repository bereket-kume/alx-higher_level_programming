#!/usr/bin/python3
def fizzbuzz():
    o = []
    for i in range(100 + 1):
        if i % 3 == 0 and i % 5 == 0:
            o.append('FizzBuzz')
        elif i % 3 == 0:
            o.append('Fizz')
        elif i % 5 == 0:
            o.append("Buzz")
        else:
            o.append(str(i))
    print(' '.join(o))
