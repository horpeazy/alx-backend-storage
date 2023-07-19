#!/usr/bin/env python3
""" 
this module contains a Python function that inserts
a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    returns a list of all documents in a collection

    Args:
        mongo_collection: pymongo collection object
        kwargs: keywords for fields in document

    Return:
        id of inserted document
    """
    return mongo_collection.insert(kwargs)
