#!/usr/bin/env python3
"""script to list all documents in fonction"""


def list_all(mongo_collection):
    """Method to list all"""
    dic = []
    if mongo_collection.find():
        for data in mongo_collection.find():
            dic.append(data)

    return dic
