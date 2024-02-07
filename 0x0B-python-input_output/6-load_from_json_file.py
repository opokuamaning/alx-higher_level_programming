#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file
"""

def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    Args: filename
    """
    import json

    with open(filename, 'r', encoding='utf-8') as f:
        json.load(f)
