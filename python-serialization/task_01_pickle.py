#!/usr/bin/env python3
"""
Module for serializing and deserializing custom objects using pickle.
"""
import pickle


class CustomObject:
    """
    A custom class representing a person with name, age, and student status.
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initializes the CustomObject instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a formatted layout.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current object instance and saves it to a file using pickle.

        Parameters:
        filename (str): The filename where the object will be saved.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, IOError, pickle.PickleError) as e:
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and deserializes an instance of CustomObject from a file.

        Parameters:
        filename (str): The filename of the pickled object file.

        Returns:
        CustomObject: The deserialized instance, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                
                # Verify that the loaded object is actually an instance of this class
                if isinstance(obj, cls):
                    return obj
                print("Error: Loaded object is not an instance of CustomObject.")
                return None
                
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, AttributeError) as e:
            print(f"Deserialization error: {e}")
            return None
