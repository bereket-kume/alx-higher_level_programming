#!/usr/bin/python3
def weight_average(my_list=[]):
    n_sum = 0
    d_sum = 0
    for i in my_list:
        n_sum += i[0] * i[1]
        d_sum += i[1]
    result = n_sum / d_sum
    return result
