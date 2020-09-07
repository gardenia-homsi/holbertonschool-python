#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    na = tuple_a + (0, 0)
    nb = tuple_b + (0, 0)
    new_tuple = ((na[0] + nb[0]), (na[1] + nb[1]))
    return(new_tuple)
