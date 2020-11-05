#!/usr/bin/env python3
"""
 lists all documents in a collection
"""


import pymongo


def list_all(mongo_collection):
    """
    list_all
    """
    if not mongo_collection:
        return []
    return mongo_collection.find()
