#!/usr/bin/env python3
'''module used to fetch all monogo
documents'''

def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection.
    """
    documents = mongo_collection.find({})
    return list(documents)
