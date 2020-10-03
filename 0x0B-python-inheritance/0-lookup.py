#!/usr/bin/python3
""" contain lookup funcyion"""


def lookup(obj):
    """return list of attribute and methon for an object"""
    return list(dir(obj))
