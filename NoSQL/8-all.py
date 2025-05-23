#!/usr/bin/env python3
"""
Lists all documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """List all documents in the given collection"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
