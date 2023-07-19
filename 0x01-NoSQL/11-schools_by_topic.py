#!/usr/bin/env python3
"""
this modules contains a Python function that
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    updates docs in a collection

    Args:
        mongo_collection: pymongo collection object
        name: name fiedl to update
        topics: topics to insert

    Return:
        None
    """
    return mongo_collection.find({"topics": topic})
