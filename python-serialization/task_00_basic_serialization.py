#!/usr/bin/env python3
"""
Module for basic JSON serialization and deserialization.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Parameters:
    data (dict): The Python dictionary containing data to serialize.
    filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file to recreate a Python dictionary.

    Parameters:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
