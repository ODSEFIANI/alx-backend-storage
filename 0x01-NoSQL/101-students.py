#!/usr/bin/env python3
'''module used to update attribute in a monogo
documents'''

from pymongo import MongoClient

def top_students(mongo_collection):
    """Returns all students sorted by average score."""
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$scores.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    
    result = mongo_collection.aggregate(pipeline)
    return list(result)
