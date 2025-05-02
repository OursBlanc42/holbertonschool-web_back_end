#!/usr/bin/env python3
"""
Update topics of a school document based on name
"""

from typing import List
from pymongo.collection import Collection


def update_topics(
        mongo_collection: Collection, name: str, topics: List[str]) -> int:

    """Updates the topics of a school based on the name."""
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
