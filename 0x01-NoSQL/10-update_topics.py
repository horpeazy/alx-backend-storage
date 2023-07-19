#!/usr/bin/python3
"""
this modules contains a Python function that changes
all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    updates docs in a collection

    Args:
        mongo_collection: pymongo collection object
        name: name fiedl to update
        topics: topics to insert

    Return:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
