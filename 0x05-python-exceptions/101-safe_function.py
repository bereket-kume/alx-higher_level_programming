#!/usr/bin/python3

import sys

<<<<<<< HEAD
=======

>>>>>>> c634230afd718beb518114a5fe440fcbefd3ec5d
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
