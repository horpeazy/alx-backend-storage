#!/usr/bin/env python3
"""
this module contains a Python function
that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    returns a list of all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Return:
        a list of documents in the object
    """
    if not mongo_collection:
        return []
    return [doc for doc in mongo_collection.find()]
