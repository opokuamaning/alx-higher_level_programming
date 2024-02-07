#!/usr/bin/python3
"""
a function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    Args: my_obj
    returns the JSON representation of an object
    """
    import json

    return(json.dumps(my_obj))
