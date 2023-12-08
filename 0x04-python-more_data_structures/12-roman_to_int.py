#!/usr/bin/python3
def roman_to_int(roman_string):
    m_d = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
            }
    d_sum = 0
    length = len(roman_string)
    for i in range(length):
        if i < length - 1 and m_d[roman_string[i]] < m_d[roman_string[i + 1]]:
            d_sum -= m_d[roman_string[i]]
        else:
            d_sum += m_d[roman_string[i]]
    return d_sum
