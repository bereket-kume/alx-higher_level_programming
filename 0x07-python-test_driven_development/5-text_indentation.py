#!/usr/bin/python3
"""module for 5-text_indentation.py"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':' character"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    for char in text:
        if char in ".?:":
            result += char + "\n\n"
        else:
            result += char

    print("\n".join(line.strip() for line in result.split("\n")))
