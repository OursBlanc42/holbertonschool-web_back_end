#!/usr/bin/env python3
"""
Update topics of a school document based on name
"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a school based on the name"""
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
