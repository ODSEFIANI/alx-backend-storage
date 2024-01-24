#!/usr/bin/env python3
'''module used to insert attribute in a monogo
documents'''

def insert_school(mongo_collection, **kwargs):
    """adds a new document in a MongoDB collection.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
