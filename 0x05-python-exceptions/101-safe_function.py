#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: " + str(err))
    return None
