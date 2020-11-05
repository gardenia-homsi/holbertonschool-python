#!/usr/bin/env python3
"""
changes all topics of a school document based on the name
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update_topics
    """
    return mongo_collection.update_many({"name": name}, {
        "$set": {"topics": topics}})
