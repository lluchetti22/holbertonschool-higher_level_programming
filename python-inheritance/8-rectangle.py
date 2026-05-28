#!/usr/bin/python3
"""Module that defines the Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes Rectangle with validated width and height.

        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
