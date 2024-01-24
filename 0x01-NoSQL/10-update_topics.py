#!/usr/bin/env python3
'''module used to update attribute in a monogo
documents'''

def update_topics(mongo_collection, name, topics):
    """Changes all topics depending on the name."""
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
