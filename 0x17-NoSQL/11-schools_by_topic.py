#!/usr/bin/env python3
"""
returns the list of school having a specific topic
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    schools_by_topic
    """
    return mongo_collection.find({"topics": topic})
