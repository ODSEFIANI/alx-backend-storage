#!/usr/bin/env python3
'''module used to update attribute in a monogo
documents'''

def schools_by_topic(mongo_collection, topic):
    """Returns the array of schools with that topic."""
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
