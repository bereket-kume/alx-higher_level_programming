#!/usr/bin/python3
"""module for read_file"""


def read_file(filename=""):
<<<<<<< HEAD
    """read_file method"""

    with open(filename, encoding="UTF-8") as file:
        content = file.read()
        print(content, end="")
=======
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
>>>>>>> cb6ad5bb71caaf1aec3857fe6affa86b33d05121
