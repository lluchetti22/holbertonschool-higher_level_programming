#!/usr/bin/python3
"""Module for converting an object to its JSON string representation."""
import json


def from_json_string(my_str):
    """Return the JSON string representation of an object."""
    return json.loads(my_str)
